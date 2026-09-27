"""Week 7 第 3 章核心配图（★）：安全边际的定义，精确到坐标。

同一家公司：
  保守估算的价值下沿 20 元，价值区间上沿 26 元；
  你付出的买入价 14 元，安全边际 = 20 - 14 = 6 元。
再补一条 22 元的红线：注意它仍然低于价值区间上沿 26 元，
但已经高过保守下沿 20 元 —— 安全边际变成 -2 元。

基准只有一条：**保守下沿**。正例反例都用它减，读者不会算糊涂。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, hline,
                             vline, money_bar,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GOLD, C_GRAY,
                             F_GREEN)

fig, ax = fig_ax(12, 7.4, xlim=(0, 10), ylim=(0, 31))

plain(ax, 5.0, 30.2, "安全边际 = 保守估算的价值 - 买入价（示例：20 - 14 = 6 元）",
      fontsize=14, weight="bold")

# ── 纵轴：元 ────────────────────────────────────────────────────────
vline(ax, 1.1, 0, 27.4, color="#333333", lw=1.4)
for y in (0, 5, 10, 14, 20, 22, 26):
    hline(ax, y, 0.92, 1.1, color="#333333", lw=1.2)
    plain(ax, 0.82, y, f"{y}", fontsize=11, ha="right", va="center")
plain(ax, 0.82, 28.0, "元", fontsize=11, ha="right", va="center")

# ── 两根柱子：买入价 vs 保守价值 ────────────────────────────────────
money_bar(ax, 2.1, 0, 1.6, 14, "买入价\n14 元", fc=C_GOLD, fontsize=12.5)
money_bar(ax, 4.2, 0, 1.6, 20, "保守价值\n20 元", fc="#9ecfa5", ec=C_GREEN,
          fontsize=12.5)

# ── 价值区间上沿（20 ~ 26 元） ──────────────────────────────────────
box(ax, 4.2, 20, 1.6, 6, "", fc=F_GREEN, ec=C_GREEN)
plain(ax, 5.0, 24.9, "上沿\n26 元", fontsize=11.5, color=C_GREEN)
label(ax, 6.15, 24.6, "价值区间：20 元 ~ 26 元\n（同一家公司，换个假设就换个价）",
      fontsize=11.5, color=C_GREEN, ha="left")

# ── 那 6 元：安全边际（基准 = 保守下沿 20 元） ──────────────────────
hline(ax, 14, 3.7, 7.4, color=C_GOLD, lw=1.2, ls=":", zorder=2)
hline(ax, 20, 5.8, 7.4, color=C_GREEN, lw=1.2, ls=":", zorder=2)
arrow(ax, (7.0, 14.4), (7.0, 19.6), color=C_GREEN, lw=2.2, style="<|-|>", zorder=4)
label(ax, 7.55, 17.0, "安全边际 = 6 元\n相当于保守价值的 30%",
      fontsize=12, color=C_GREEN, ha="left", weight="bold")

# ── 价格高过保守下沿：安全边际变成负数（基准还是 20 元） ────────────
hline(ax, 22, 2.1, 9.4, color=C_RED, lw=1.8, ls="--", zorder=2)
label(ax, 2.95, 23.7,
      "如果出价 22 元：\n比保守价值 20 元还高 2 元\n安全边际变成 -2 元（危险边际）",
      fontsize=11.5, color=C_RED)

# ── 价格再低一点：安全边际更厚 ──────────────────────────────────────
money_bar(ax, 7.3, 0, 1.4, 10, "若只出价\n10 元", fc="#f3e2b8", ec=C_GOLD,
          fontsize=11.5)
label(ax, 8.85, 12.0, "价格越低，\n安全边际越厚", fontsize=11.5, color=C_BLUE,
      ha="center")

save(fig, "w7d3_margin_defined.png")
