"""Week 10 第 2 章配图：内部人士买与卖的信息量不对称（原书 p170）。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_GREEN, C_RED, C_GRAY,
                             F_BLUE, F_GREEN, F_RED, F_GRAY)

fig, ax = fig_ax(13.4, 8.0, xlim=(0, 12), ylim=(0, 10))

plain(ax, 6.0, 9.62, "内部人士买与卖，信息量完全不对称",
      fontsize=15, weight="bold", color="#222222")
plain(ax, 6.0, 9.15, "（《安全边际》第九章，原书 p170）",
      fontsize=10.5, color=C_GRAY)

# ── 左：卖出 ─────────────────────────────────────────────────────────
box(ax, 0.35, 8.05, 5.60, 0.90, "内部人士卖出：理由可能有一万个",
    fc=F_RED, ec=C_RED, fontsize=12.5, weight="bold")

SELL = ["要交税", "买房换车", "离婚分割",
        "子女教育", "分散投资", "还债做慈善"]
for i, t in enumerate(SELL):
    col, row = divmod(i, 3)
    x = 0.35 + col * 2.90
    y = 7.30 - row * 0.90
    box(ax, x, y, 2.70, 0.72, t, fc="white", ec=C_RED, fontsize=10.5)

box(ax, 0.35, 4.45, 5.60, 0.75, "→ 结论：卖出是弱信号",
    fc="#f7f7f7", ec=C_GRAY, fontsize=11.5, weight="bold")

# ── 右：买入 ─────────────────────────────────────────────────────────
box(ax, 6.05, 8.05, 5.60, 0.90, "内部人士买入：理由只剩一个",
    fc=F_GREEN, ec=C_GREEN, fontsize=12.5, weight="bold")

box(ax, 6.05, 5.50, 5.60, 2.52,
    "他觉得这只股票现在便宜，\n"
    "愿意拿自己的真金白银下注。\n\n"
    "在多数情况下，没有一个人能比\n"
    "管理层更了解一家企业及其前景。",
    fc="white", ec=C_GREEN, fontsize=11, tc="#333333")

box(ax, 6.05, 4.45, 5.60, 0.75, "→ 结论：买入是强信号",
    fc=F_GREEN, ec=C_GREEN, fontsize=11.5, weight="bold")

# ── 底部：四道加试题 ─────────────────────────────────────────────────
plain(ax, 6.0, 3.90, "看到内部人买入，再追加四道题——四条都过才是强信号",
      fontsize=12, weight="bold", color="#222222")

QUIZ = [
    "是公开市场买入吗？\n（不是期权行权，\n也不是参加增发）",
    "是多人一起买吗？\n（只有一位高管，\n可能只是巧合）",
    "金额相对他的年薪\n大吗？（买 1 万股\n和买 100 万股不同）",
    "是连着买了好几次吗？\n（一次性买入可能是\n被安排的）",
]
for i, t in enumerate(QUIZ):
    x = 0.35 + i * 2.92
    box(ax, x, 1.35, 2.72, 2.25, t, fc=F_BLUE, ec=C_BLUE, fontsize=10)

save(fig, "w10d2_insider_signal.png")
