#!/usr/bin/env python3
"""把《安全边际》PDF 按页抽取成结构化 markdown。

为什么不用 marker-pdf：
  - 本书是 WPS 导出的**文字版 PDF**（非扫描件），字体信息完整（SimSun 正文 14pt /
    SimHei 小标题 15.9pt / 章标题 21.9pt），PyMuPDF 能拿到全部结构；
  - marker 在本机 anaconda 环境有依赖冲突，且 281 页 CPU 推理很慢；
  - 用字体 + 缩进判定结构，秒级完成，且页码与 PDF 页码严格对齐，方便写教程时引用。

排版规律（已逐页验证）：
  - 页码：TimesNewRomanPSMT 9pt，丢弃；
  - 部分扉页 / 章标题：21.9pt，居中 → `#`；
  - 一级小节：SimHei 15.9pt，左对齐 x≈89.8 → `##`；
  - 二级小节：SimSun 15.9pt，左对齐 x≈89.8 → `###`；
  - 正文：SimSun 14pt；段落首行缩进两个汉字（x≈117.7，正文左边界 x≈89.8）；
  - 伪粗体标题被重复绘制 3~4 遍，且存在"叠字合并"行，脚本做了同行去重与包含折叠。

用法：
    python3 scripts/pdf_to_pages.py <pdf> <out_dir>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

# ---- 版式常量（来自对本书的实际测量） ----
LEFT_MARGIN = 89.8          # 正文左边界
INDENT = 117.7              # 段落首行缩进位置
BODY_SIZE = 14.0            # 正文字号
BODY_MAX_W = 415.4          # 正文整行最大宽度
SHORT_LINE_W = 366.0        # 短于此宽度视为段末
PAGENO_FONTS = ("TimesNewRomanPSMT", "TimesNewRomanPS")
HEAD_SIZES = {"part": 21.9, "h2": 15.9}


def _line_items(line: dict) -> list[tuple[float, str, float]]:
    """把一条 line 的 spans 压成 [(x0, text, size)]：同行去重 + 叠字折叠。

    两种反复出现的伪影：
      A. 伪粗体：整行被原样画 3~4 遍（起点 x 相同）→ 同起点取一份；
      B. 叠字合并：除正常片段外，还多画一条"把前面若干片段粘在一起"的长串
         （如 `第九章` + `第九章投资研究：…` + `投资研究：…`）→ 丢掉被长串包住的那份。

    注意：中文标点常因"标点挤压"被单独画成**更小字号**的 span（如 11.4pt 的 `。`），
    它和主 span 的 x 区间有少量重叠，且恰好是主串里的某个字符——
    所以"子串即丢弃"的规则**必须排除单字符**，否则会吃掉句末标点。
    """
    raw: list[tuple[float, str, float]] = []
    seen: set[tuple[str, int]] = set()
    for s in line["spans"]:
        t = s["text"]
        if not t.strip():
            continue
        key = (t, round(s["bbox"][0]))
        if key in seen:                 # 伪影 A
            continue
        seen.add(key)
        raw.append((s["bbox"][0], t, s["size"]))

    raw.sort(key=lambda r: r[0])
    merged: list[tuple[float, str, float]] = []
    for x0, t, size in raw:
        if merged:
            px0, pt, psize = merged[-1]
            same_start = abs(x0 - px0) <= 3
            if same_start:
                # 同一起点：整行重画，保留更长的那个版本
                if len(t) > len(pt):
                    merged[-1] = (px0, t, size)
                continue
            # 起点更靠后：若整段被已累积文本包住（且不止一个字），是伪影 B
            if len(t) > 1 and t in pt:
                continue
        merged.append((x0, t, size))
    return merged


def _visual_lines(page) -> list[dict]:
    """把 PDF 的 line 还原成"视觉上的一行"。

    WPS/PDFlib 的伪粗体会把同一行文字画 3~4 遍，PyMuPDF 把它们报成**同一 block 内
    y 几乎重合的多条 line**。这里先按 y 中心聚类，再把同簇的片段拼成一行。
    """
    out: list[dict] = []
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue

        # 按 y 中心聚类：同一视觉行的 line 归为一簇
        clusters: list[list[dict]] = []
        for line in sorted(b["lines"], key=lambda l: (l["bbox"][1] + l["bbox"][3]) / 2):
            yc = (line["bbox"][1] + line["bbox"][3]) / 2
            if clusters:
                prev = clusters[-1]
                pyc = sum((l["bbox"][1] + l["bbox"][3]) / 2 for l in prev) / len(prev)
                if abs(yc - pyc) < 7:
                    prev.append(line)
                    continue
            clusters.append([line])

        for cluster in clusters:
            spans = [s for line in cluster for s in line["spans"]]
            if not spans:
                continue
            items = _line_items({"spans": spans})
            if not items:
                continue
            text = "".join(t for _, t, _ in items)
            if not text.strip():
                continue
            size = max(s for _, _, s in items)
            fonts = {s["font"] for s in spans}
            if any(f.startswith(PAGENO_FONTS) for f in fonts) and size < 10:
                continue                                   # 页码
            if re.fullmatch(r"\d{1,4}", text.strip()) and size < 10:
                continue                                   # 页码（字体缺失时的兜底）
            out.append({
                "x0": items[0][0],
                "size": size,
                "font": sorted(fonts)[0],
                "fonts": fonts,
                "text": text.rstrip(),
                "w": max(l["bbox"][2] for l in cluster) - min(l["bbox"][0] for l in cluster),
            })
    # 按 y 排序输出，保证阅读顺序
    return out


def _classify(ln: dict) -> str:
    if ln["size"] >= 20:
        return "h1"
    if abs(ln["size"] - HEAD_SIZES["h2"]) < 0.6:
        return "h2" if ln["font"].startswith("SimHei") else "h3"
    return "body"


def _norm(s: str) -> str:
    """归一化用于标题比对：去掉空白与常见标点。"""
    return re.sub(r"[\s•·、，。：:；;（）()《》\"'’“”\-—…\.]", "", s)


def _render_page(lines: list[dict]) -> str:
    """把行序列渲染成 markdown：标题独立成行，正文按段落合并。"""
    blocks: list[str] = []
    para: list[str] = []
    head_buf: list[str] = []      # 连续的同类标题行（长标题会折行，需要拼回去）
    head_lvl = 0
    head_w = 0.0                  # 缓冲区里最后一行的宽度

    def flush_para():
        if para:
            blocks.append("".join(para))
            para.clear()

    def flush_head():
        nonlocal head_lvl, head_w
        if head_buf:
            blocks.append("#" * head_lvl + " " + "".join(head_buf))
            head_buf.clear()
        head_lvl = 0
        head_w = 0.0

    for ln in lines:
        kind = _classify(ln)
        is_bullet = any(f.startswith("Wingdings") for f in ln["fonts"])

        if kind != "body" and not is_bullet:
            flush_para()
            lvl = {"h1": 1, "h2": 2, "h3": 3}[kind]
            # 同一标题的折行判定：前一行几乎占满整行，且本行不是从左侧正文边界起排
            wrapped = (
                head_buf
                and lvl == head_lvl
                and head_w >= 0.72 * BODY_MAX_W
                and ln["x0"] > LEFT_MARGIN + 20
            )
            if wrapped:
                head_buf.append(ln["text"].strip())
            else:
                flush_head()
                head_lvl = lvl
                head_buf.append(ln["text"].strip())
            head_w = ln["w"]
            continue

        flush_head()

        if is_bullet:
            # Wingdings 的项目符号（z / 私用区字符）在文本层没有意义，换成 markdown 列表
            txt = re.sub(r"^[\sz\uE000-\uF8FF]", "", ln["text"].strip()).strip()
            blocks.append(f"- {txt}")
            continue

        indented = ln["x0"] >= INDENT - 3
        if indented and para:
            flush_para()                                   # 缩进 = 新段落开头
        para.append(ln["text"].strip())
        if ln["w"] < SHORT_LINE_W:                         # 不足一行 = 段末
            flush_para()

    flush_para()
    flush_head()
    return "\n\n".join(b for b in blocks if b.strip())


# 章 / 部分标题的文本特征（本书的章标题字号在各章之间并不统一）
CHAP_RE = re.compile(r"^第[一二三四五六七八九十]+(章|部分)")
FRONT_RE = re.compile(r"^(导言|前言|序言|附录[一二三四五六七八九十]?|编后记|卡拉曼访谈)")


def _promote_chapter(page_md: str, toc_title: str | None) -> str:
    """把某一页的章/部分标题统一提升为 `#`。

    本书章标题的字号在不同章之间不统一（有的 21.9pt，有的 15.9pt SimHei），
    因此不能只靠字号判定，改用「标题文本特征 + PDF 书签」双重兜底。
    """
    lines = page_md.split("\n")
    key = _norm(toc_title)[:6] if toc_title else ""
    for i, ln in enumerate(lines):
        if not ln.startswith("#"):
            continue
        core = _norm(ln.lstrip("# "))
        if CHAP_RE.match(core) or FRONT_RE.match(core) or (key and key in core):
            lines[i] = f"# {ln.lstrip('# ').strip()}"
            return "\n".join(lines)
    return page_md


def convert(pdf_path: Path, out_dir: Path) -> int:
    doc = fitz.open(str(pdf_path))
    out_dir.mkdir(parents=True, exist_ok=True)

    # TOC 中 level-1 的条目 = 部分扉页 / 章标题（本书章标题字号在不同章之间不统一）
    level1: dict[int, str] = {}
    for lvl, title, page in doc.get_toc():
        if lvl == 1:
            level1.setdefault(page, title)

    parts: list[str] = []
    for i in range(doc.page_count):
        body = _render_page(_visual_lines(doc[i]))
        body = _promote_chapter(body, level1.get(i + 1))
        page_md = f"<!-- Page {i + 1} -->\n\n> 📄 《安全边际》第 {i + 1} 页\n\n{body}\n"
        (out_dir / f"page_{i + 1:03d}.md").write_text(page_md, encoding="utf-8")
        parts.append(f"\n\n<!-- ===== Page {i + 1} ===== -->\n\n{body}")

    (out_dir / "BOOK.md").write_text(
        f"# 《安全边际》全文（PyMuPDF 抽取，共 {doc.page_count} 页）\n"
        + "".join(parts), encoding="utf-8")

    toc_lines = ["# 《安全边际》目录（来自 PDF 书签）\n"]
    for lvl, title, page in doc.get_toc():
        toc_lines.append(f"{'  ' * (lvl - 1)}- [{title}](page_{page:03d}.md)  `p{page}`")
    (out_dir / "TOC.md").write_text("\n".join(toc_lines) + "\n", encoding="utf-8")

    return doc.page_count


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    n = convert(Path(sys.argv[1]), Path(sys.argv[2]))
    print(f"✅ {n} pages -> {sys.argv[2]}")


if __name__ == "__main__":
    main()
