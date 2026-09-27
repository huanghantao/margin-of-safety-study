"""W4 第 1 章图：为什么研报几乎只有「买入」。

左：写「买入」和写「卖出」各自会触发什么（原书 p37-p38 的机制）；
右：行情好坏直接决定华尔街的收入（原书 p36-p37），真实坐标柱状图。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, box, plain, label, style_axes, vline,
                             C_BLUE, C_GREEN, C_GRAY, C_RED, C_ORANGE,
                             F_BLUE, F_GREEN, F_RED, F_GRAY)

fig, axes = plt.subplots(1, 2, figsize=(13.8, 7.4),
                         gridspec_kw={"width_ratios": [1.32, 1.0]})
fig.subplots_adjust(top=0.84, bottom=0.14, left=0.04, right=0.97, wspace=0.13)

# ══════════════════════════════════════════════════════════════════
#  左：一句话的代价与收益
# ══════════════════════════════════════════════════════════════════
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

plain(ax, 5.0, 9.72, "同一份研究，写成「买入」和写成「卖出」的差别",
      fontsize=13.5, weight="bold", color="#222222")

box(ax, 0.15, 8.50, 4.45, 0.88, "写成「买入」", fc=F_GREEN, ec=C_GREEN,
    fontsize=12.5, weight="bold")
box(ax, 5.40, 8.50, 4.45, 0.88, "写成「卖出」", fc=F_RED, ec=C_RED,
    fontsize=12.5, weight="bold")

buy_rows = [
    "手上拿着现金的人都能买，\n潜在客户是全体股民",
    "投行部门正在给这家公司办事，\n说坏话等于砸自家生意",
    "管理层爱听，\n以后更容易约到调研",
]
sell_rows = [
    "只有已经拿着这只股票的人才能卖，\n客户池小得多",
    "可能得罪投行客户，\n把赚钱的生意推走",
    "原书 p37：1990 年一位分析师\n因对大客户写负面报告而丢了工作",
]
for i, y in enumerate((7.10, 5.35, 3.60)):
    box(ax, 0.15, y, 4.45, 1.10, buy_rows[i], fc=F_GREEN, ec=C_GREEN,
        fontsize=10.5)
    box(ax, 5.40, y, 4.45, 1.10, sell_rows[i], fc=F_RED, ec=C_RED,
        fontsize=10.5)

vline(ax, 5.00, 3.30, 8.35, color=C_GRAY, lw=1.4, ls=":")

box(ax, 0.15, 1.55, 9.70, 1.30,
    "结果：研报一边倒地看涨。\n"
    "这不是阴谋，是激励结构——每个人单独看都很合理。",
    fc="#f7f7f7", ec=C_GRAY, fontsize=12, weight="bold")

# ══════════════════════════════════════════════════════════════════
#  右：行情好坏 = 收入好坏
# ══════════════════════════════════════════════════════════════════
ax = axes[1]
names = ["行情好的年份", "行情差的年份"]
vals = [100, 40]
colors = [C_GREEN, C_RED]

ax.bar(range(2), vals, width=0.44, color=colors, zorder=3)
for i, v in enumerate(vals):
    plain(ax, i, v + 3.5, f"{v}", fontsize=13.5, color=colors[i],
          weight="bold", va="bottom", ha="center")

ax.set_xticks(range(2))
ax.set_xticklabels(names, fontsize=12)
ax.set_ylim(0, 132)
ax.set_xlim(-0.66, 1.66)
style_axes(ax, ylabel="承销 + 经纪 + 交易收入（示意指数）",
           title="市场涨，它赚得多；市场跌，它赚得少", grid_axis="y")
plain(ax, -0.64, -18,
      "原书 p36-p37：行情好时能完成更多承销、更多经纪业务，",
      fontsize=10, color=C_GRAY, ha="left", va="top")
plain(ax, -0.64, -31,
      "客户也更开心。以下为示意数字，用于说明方向。",
      fontsize=10, color=C_GRAY, ha="left", va="top")
plain(ax, -0.64, -44,
      "行情差时，三块收入一起缩水。",
      fontsize=10, color=C_GRAY, ha="left", va="top")

save(fig, "w4d1_bullish_bias.png")
