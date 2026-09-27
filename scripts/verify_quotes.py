"""引文保真度检查：教程里标注了页码的"原书金句"，必须真的能在那一页找到。

为什么需要它：
  这个项目的教程由多个子 agent 撰写，规范要求「原书金句逐字引用并标注页码」。
  大模型很容易把大意"复述"成引文，或者页码张冠李戴——而这类错误对读者
  是最有欺骗性的（他没法核对，因为原书绝版）。这个脚本把这件事变成机器可验的。

识别规则：
  - 形如 `> "……"（p105）` 或 `> "……"（p105–107）` 的引用块行；
  - 或者行内出现 `"……"（p105）`。
  引文可能跨多行，脚本会把连续的引用块行拼起来再比对。

判定方式：
  - 把引文和原文都做"归一化"（去掉全部空白、标点、引号、破折号）；
  - 引文去掉省略号后，用**前 10 个归一化字符**去对应页范围里找；
  - 找不到就报 ✗，并把最接近的原文片段打出来供人工判断。

用法：
    python3 scripts/verify_quotes.py
    python3 scripts/verify_quotes.py --show-ok     # 连通过的一起列出来
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "安全边际-中文版"
GUIDE = ROOT / "learning-guide"

# 页码标注：p105 / P105 / p105-107 / p105–107 / p105、107
PAGE_RE = re.compile(r"[（(]\s*[pP]\s*(\d{1,3})\s*(?:[-–—~～,，、]\s*(\d{1,3})\s*)?[)）]")
# 引号：中文引号或英文双引号
QUOTE_RE = re.compile(r"[“\"]([^”\"]{6,})[”\"]")

# 归一化时丢弃的字符。
# 除了中英标点，还必须丢掉三类"非内容"字符，否则会造成假失败：
#   ① Markdown 标记：* _ ` > #（`> ` 是多行引用块的每行前缀，
#      不丢的话跨行引文里会混进 `>`，和原文对不上）
#   ② 各种项目符号/间隔号：· • ‧ ・ （原书用 •，作者常写成 ·，必须视为同一个字）
#   ③ 空白与破折号
DROP = set(
    " \t\r\n　"
    "，。、；：？！“”‘’\"'（）()《》〈〉【】〔〕[]{}"
    "—–-～~…．.,;:!?/\\|"
    "*_`>#"
    "·•‧・∙"
)


def norm(s: str) -> str:
    return "".join(ch for ch in s if ch not in DROP)


def page_text(n: int) -> str:
    """读第 n 页（原书页码 = 文件名编号）的归一化正文。"""
    f = RAW / f"page_{n:03d}.md"
    if not f.exists():
        return ""
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"<!--.*?-->", "", t, flags=re.DOTALL)
    t = re.sub(r"^>.*$", "", t, flags=re.MULTILINE)   # 去掉 "> 📄 第 N 页" 标记行
    return norm(t)


def range_text(a: int, b: int) -> str:
    return "".join(page_text(i) for i in range(a, min(b, a + 4) + 1))


def _units(lines):
    """把行分成"引用块"和"普通行"两类单元。

    多行引文在 markdown 里是连续的 `>` 行，必须合并后再找引号，
    否则跨行的引号配不成对（开引号在第一行、闭引号在第三行）。
    """
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith(">"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith(">"):
                j += 1
            yield i, "\n".join(lines[i:j])
            i = j
        else:
            yield i, lines[i]
            i += 1


def find_quotes(md: str):
    """抽出 (引文, 起始页, 结束页, 行号)。

    只有**紧跟在引文后面**的页码标注才算"引文出处"。
    像「……也就是"今天关门卖东西还能剩多少"，因为他承认自己没法算得更精确（p133）。」
    这种句子，页码是普通出处标注、引号里是作者自己的白话解释，**不该**拿去逐字核对——
    早期版本用"往前找最近的引号"配对，会把这类白话当成原书引文而误报。
    """
    out = []
    for start, text in _units(md.splitlines()):
        for m in QUOTE_RE.finditer(text):
            # 页码标注必须**紧贴**在闭引号之后，中间只允许有空白：
            #   `"……"（p105）`      → 是引文出处，要核对
            #   `"每个月分到的钱"里（p26）` → 引号是作者自己的说法，页码是句子出处，跳过
            # 注意：要在完整文本上匹配、再检查偏移量——先截断字符串会让
            # `（p105）` 这种标注被切断，正则根本匹配不上。
            pm = PAGE_RE.search(text, m.end())
            if not pm or text[m.end(): pm.start()].strip():
                continue
            # 引号里如果是**被否定的说法**，那不是引文，是作者在驳斥一个流行误解。
            # 例：`卡拉曼并不是说"流动性越高越好"（p224）` —— 这句话恰恰不在书里。
            # 注意：作者常把"不是说"写成 Markdown 粗体 `**并不是**说`，
            # 所以要先剥掉 * _ ` 再判断，否则否定词被星号切开就漏检。
            lead = re.sub(r"[*_`]", "", text[max(0, m.start() - 14): m.start()])
            if re.search(r"(并不是说|不是说|并非|而不是|不是|绝非|不同于|不等于|区别于)\s*$", lead):
                continue
            quote = m.group(1)
            if len(norm(quote)) < 6:
                continue
            a = int(pm.group(1))
            b = int(pm.group(2)) if pm.group(2) else a
            out.append((quote.strip(), a, b, start + 1))
    return out


def check_file(path: pathlib.Path, show_ok: bool) -> list:
    md = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    problems, oks = [], []
    for quote, a, b, lineno in find_quotes(md):
        hay = range_text(a, b)
        needle = norm(quote)
        if not hay:
            problems.append(f"  ✗ 第 {lineno} 行：原文页 p{a} 不存在或为空")
            continue
        # 省略号把引文切成几段，逐段验证（只验证长度 ≥ 8 的段）
        segs = [s for s in re.split(r"…+|\.\.\.+", quote) if len(norm(s)) >= 8]
        segs = segs or [quote]
        bad = [s for s in segs if norm(s)[:10] not in hay]
        if bad:
            problems.append(
                f"  ✗ 第 {lineno} 行（p{a}{'–' + str(b) if b != a else ''}）找不到引文："
                f"“{bad[0][:36]}…”"
            )
        else:
            oks.append(f"  ✓ 第 {lineno} 行（p{a}）“{quote[:28]}…”")
    print(f"— {rel}")
    for line in (problems + (oks if show_ok else [])):
        print(line)
    if not problems and not show_ok:
        print(f"  ✓ {len(oks)} 条引文全部核对通过")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--show-ok", action="store_true", help="连通过的引文一起列出")
    args = ap.parse_args()

    if not RAW.exists():
        print(f"❌ 找不到原书目录 {RAW}（请先跑 scripts/pdf_to_pages.py）")
        return 1

    files = sorted(GUIDE.glob("**/*.md"))
    if not files:
        print("⚠️ learning-guide/ 下还没有任何 markdown")
        return 0

    total = 0
    for f in files:
        total += len(check_file(f, args.show_ok))

    print()
    if total:
        print(f"❌ 共 {total} 条引文对不上原文（可能页码错、或者引文被改写/编造）")
        return 1
    print("✅ 所有标注页码的引文都能在原文对应页找到")
    return 0


if __name__ == "__main__":
    sys.exit(main())
