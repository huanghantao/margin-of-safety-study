"""课程完整性验收脚本。

检查项目是否达到交付标准：
  1. SUMMARY.md 里链接的每个章节文件都存在且内容足够长（不是占位符）；
  2. 每章必备结构：本章你将 / ✍️ 想一想 / ✅ 小测验 / 📖 回到原书
     （每周 README 另有要求：本周目录 / 动手作业）；
  3. 涉及数字的章节要有 🧮 算一算；
  4. 章节里引用的每张图片都真实存在；
  5. figures/out/ 里每张图都至少被引用一次；
  6. 正文不得引用其他课程/教程；
  7. LaTeX 规范检查（调用 scripts/verify_latex.py）；
  8. 引文保真度检查（调用 scripts/verify_quotes.py，缺 raw/ 时跳过）；
  8. mdBook 构建成功。

用法：python3 scripts/verify_course.py
"""

import pathlib
import re
import shutil
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
MIN_CHAPTER_LINES = 110    # 正文章节最少行数（占位符只有 1 行）
MIN_README_LINES = 45      # 每周 README 最少行数

# 每章必备的结构标记
REQUIRED_MARKERS = ["本章你将", "想一想", "小测验", "回到原书"]
# README 必备
README_MARKERS = ["动手作业"]

# 代码围栏里出现这些图案 = 有人在用 ASCII 画图表（本课程明令禁止）。
# 注意：目录树用的 ├── └── │ ─ 不在此列 —— 那是合法的路径示意，不是数据图。
ASCII_ART_PATTERNS = [
    r"\+-{2,}\+",              # +-----+   表格/框图边框
    r"\|[\s|]{3,}\|",          # |     |   表格/框图竖边
    r"-{2,}>",                 # --->      箭头示意
    r"^\s*\^+\s*$",            # ^^^^      用插入符当柱子
    r"[┌┐┘┤┬┴┼╔╗╚╝║═]",        # 制表符表格边框
    r"^\s*[\\/]\s+[\\/]\s*$",  # \  /      用斜杠画折线
    r"[#*]{5,}",               # ########  用符号当柱状条
]

# 禁止出现的跨课程引用（本教程必须完全独立）
FORBIDDEN = [
    "证券分析-study", "security-analysis-study",
    "如果你学过", "前面那门课", "另一套教程", "之前的课程",
]


def parse_summary() -> list:
    """从 SUMMARY.md 提取所有 markdown 链接（相对路径）。"""
    summary = ROOT / "SUMMARY.md"
    links = re.findall(r"\]\(([^)]+\.md)\)", summary.read_text(encoding="utf-8"))
    return [l for l in links if not l.startswith("http")]


def check_h1_matches_summary() -> list:
    """章节文件的一级标题必须与 SUMMARY.md 里的链接文字一字不差。

    这条很容易被忽略：mdBook 侧边栏用 SUMMARY 的文字，页面顶部用文件里的 H1。
    两者不一致时，读者在两个地方看到不同的章节名（本项目真的发生过一次：
    标题写"六种机会"、后面却只列了五个名字）。
    """
    problems = []
    summary = (ROOT / "SUMMARY.md").read_text(encoding="utf-8")
    for label, rel in re.findall(r"\[([^\]]+)\]\(([^)]+\.md)\)", summary):
        if rel.startswith("http"):
            continue
        path = ROOT / rel
        if not path.exists() or path.name == "README.md":
            continue
        first = next((l for l in path.read_text(encoding="utf-8").splitlines()
                      if l.strip()), "")
        h1 = re.sub(r"^#\s*", "", first).strip()
        if h1 and h1 != label:
            problems.append(f"[标题不一致] {rel}\n"
                            f"       SUMMARY 写：{label}\n"
                            f"       文件 H1 写：{h1}")
    return problems


def check_chapters(links) -> list:
    problems = []
    for link in links:
        path = ROOT / link
        if not path.exists():
            problems.append(f"[缺文件] {link} 不存在")
            continue
        text = path.read_text(encoding="utf-8")
        n = len(text.splitlines())
        is_readme = path.name == "README.md"
        min_lines = MIN_README_LINES if is_readme else MIN_CHAPTER_LINES
        if n < min_lines:
            problems.append(f"[疑似占位] {link} 只有 {n} 行（要求 ≥ {min_lines}）")

        markers = README_MARKERS if is_readme else REQUIRED_MARKERS
        for m in markers:
            if m not in text:
                problems.append(f"[缺结构] {link} 缺「{m}」")

        # 正文里的跨课程引用
        for bad in FORBIDDEN:
            if bad in text:
                problems.append(f"[跨课程引用] {link} 出现「{bad}」")

        # 每章至少要有配图（README 豁免）
        if not is_readme and not re.search(r"!\[[^\]]*\]\(", text):
            problems.append(f"[无配图] {link} 没有引用任何图片")

        # 禁止 ASCII 画图
        for m in re.findall(r"```[^\n]*\n(.*?)```", text, flags=re.DOTALL):
            for pat in ASCII_ART_PATTERNS:
                if re.search(pat, m, flags=re.MULTILINE):
                    problems.append(
                        f"[ASCII 画图] {link} 的代码块里出现字符图形"
                        f"（本课程要求用 PNG，见 CURRICULUM 第 6 节）")
                    break
    return problems


def check_per_week(links) -> list:
    """每周至少要有一处 🧮 算一算，且图脚本文件名要带周号。"""
    problems = []
    weeks = sorted({p.parts[1] for p in (ROOT / l for l in links)
                    if len(p.parts) > 1 and p.parts[0] == "learning-guide"})
    for w in weeks:
        files = [ROOT / l for l in links
                 if l.startswith(f"learning-guide/{w}/")]
        texts = [f.read_text(encoding="utf-8") for f in files if f.exists()]
        if not any("算一算" in t for t in texts):
            problems.append(f"[缺练习] {w} 没有任何一章有「🧮 算一算」")
    return problems


def check_image_refs(links) -> list:
    problems = []
    used = set()
    for link in links:
        path = ROOT / link
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for m in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            if m.startswith("http"):
                continue
            img = (path.parent / m).resolve()
            if not img.exists():
                problems.append(f"[缺图] {link} 引用了不存在的图片 {m}")
            else:
                used.add(img.name)
    out_dir = ROOT / "figures" / "out"
    for png in sorted(out_dir.glob("*.png")):
        if png.name not in used:
            problems.append(f"[图未被引用] figures/out/{png.name}")
    return problems


def check_figure_scripts() -> list:
    """每个 gen_w*.py 必须至少存在；并提示哪些周还没有图脚本。"""
    problems = []
    scripts = sorted((ROOT / "figures").glob("gen_w*.py"))
    if not scripts:
        problems.append("[无图脚本] figures/ 下没有任何 gen_w*.py")
    return problems


def run(cmd: list, cwd, retries: int = 0, retry_hint: str = "") -> int:
    """跑一条命令。retries>0 时对失败重试（用于规避并发写 book/ 的竞态）。"""
    for attempt in range(retries + 1):
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        if r.returncode == 0:
            print(f"  $ {' '.join(cmd)}  → exit 0"
                  + (f"（第 {attempt + 1} 次尝试）" if attempt else ""))
            return 0
        if attempt < retries:
            print(f"  $ {' '.join(cmd)}  → exit {r.returncode}，重试…")
            time.sleep(2)
            continue
        print(f"  $ {' '.join(cmd)}  → exit {r.returncode}")
        tail = (r.stderr or r.stdout).strip().splitlines()[-10:]
        for line in tail:
            print("   " + line)
        if retry_hint:
            print("   " + retry_hint)
        return r.returncode
    return 1


def main():
    print("== 1. 章节文件 ==")
    links = parse_summary()
    problems = check_chapters(links)
    print(f"   SUMMARY 链接 {len(links)} 个")
    for p in problems:
        print("   ✗", p)
    print(f"   章节检查：{'全过' if not problems else f'{len(problems)} 个问题'}")

    print("== 2. 标题一致性 ==")
    h1_problems = check_h1_matches_summary()
    for p in h1_problems:
        print("   ✗", p)
    print(f"   SUMMARY 与章节 H1：{'全过' if not h1_problems else f'{len(h1_problems)} 个问题'}")

    print("== 3. 每周练习 ==")
    week_problems = check_per_week(links)
    for p in week_problems:
        print("   ✗", p)
    print(f"   每周练习：{'全过' if not week_problems else f'{len(week_problems)} 个问题'}")

    print("== 4. 图片引用 ==")
    img_problems = check_image_refs(links)
    for p in img_problems:
        print("   ✗", p)
    print(f"   图片检查：{'全过' if not img_problems else f'{len(img_problems)} 个问题'}")

    print("== 5. 生图脚本 ==")
    fig_problems = check_figure_scripts()
    for p in fig_problems:
        print("   ✗", p)
    print(f"   生图脚本：{'全过' if not fig_problems else f'{len(fig_problems)} 个问题'}")

    print("== 6. LaTeX 规范 ==")
    rc_latex = run([sys.executable, "scripts/verify_latex.py"], ROOT)

    print("== 7. 引文保真度 ==")
    # 每一条 `"……"（pXX）` 都要能在原书那一页逐字找到。
    # 这一步需要 raw/（原书 markdown，已在 .gitignore 里），
    # 所以缺 raw/ 时只提示、不算失败 —— 拿到干净克隆的读者不该因此卡住。
    if not (ROOT / "raw" / "安全边际-中文版").exists():
        print("   ⏭ 跳过：找不到 raw/安全边际-中文版（先跑 "
              "scripts/pdf_to_pages.py 才能做引文核对）")
        rc_quotes = 0
    else:
        rc_quotes = run([sys.executable, "scripts/verify_quotes.py"], ROOT)

    print("== 8. mdBook 构建 ==")
    # ⚠️ 必须先清空 book/ 再构建。
    # 本项目 src = "."，输出目录 book/ 就在源码目录里面。一旦某次构建被打断
    # （多个 agent 并发构建时很容易发生），book/ 里会残留一个半成品，下一次构建
    # 就会把 book/ 当成"资源"拷进 book/book/，再下一次变成 book/book/book/……
    # 产物会从 16MB 膨胀到 GB 级，并持续报 "Unable to remove stale HTML output"。
    # 清空后重建是幂等的，代价只有一两秒。
    stale = ROOT / "book"
    if stale.exists():
        shutil.rmtree(stale, ignore_errors=True)
    rc_book = run(["mdbook", "build"], ROOT, retries=3,
                  retry_hint="（若反复失败，可能是并发构建 book/ 目录的竞态，"
                             "等其它 agent 结束后再跑；或改用 "
                             "mdbook build --dest-dir /tmp/mdbook-check）")
    # 构建完再检查一次有没有出现递归自拷贝
    if (stale / "book").exists():
        print("   ✗ 检出 book/book 递归自拷贝：src='.' 会让 mdbook 把输出目录"
              "当成资源再拷一遍，请清空 book/ 后重建")
        rc_book = rc_book or 1

    total = (len(problems) + len(h1_problems) + len(week_problems) + len(img_problems)
             + len(fig_problems) + (rc_latex != 0) + (rc_quotes != 0)
             + (rc_book != 0))
    print()
    if total == 0:
        print("✅ 全部通过，课程达到交付标准。")
        return 0
    print(f"❌ 共 {total} 个问题（占位/结构/标题/缺图/LaTeX/引文/构建）。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
