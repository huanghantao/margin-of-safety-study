"""W4 第 0 章图二：同一笔 1 亿美元的证券，承销费是二级市场佣金的 4~16 倍。

左图用原书 p32 的数字直接推算（2%~8% 承销总费用、5 美分/股机构佣金、股价 10 美元）；
右图是"谁出钱、谁承担结果、谁先拿到钱"的错位对照。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, box, plain, label, style_axes, vline,
                             C_BLUE, C_ORANGE, C_GREEN, C_GRAY, C_RED,
                             F_BLUE, F_GREEN, F_ORANGE, F_RED)

fig, axes = plt.subplots(1, 2, figsize=(13.6, 7.2),
                         gridspec_kw={"width_ratios": [1.0, 1.05]})
fig.subplots_adjust(top=0.83, bottom=0.17, left=0.07, right=0.97, wspace=0.20)

# ══════════════════════════════════════════════════════════════════
#  左：承销费 vs 二级市场佣金（原书 p32 数字推算）
# ══════════════════════════════════════════════════════════════════
ax = axes[0]
names = ["二级市场\n交易佣金", "承销费\n（下限 2%）", "承销费\n（上限 8%）"]
vals = [50, 200, 800]
colors = [C_BLUE, C_ORANGE, C_RED]

ax.bar(range(3), vals, width=0.52, color=colors, zorder=3)
for i, v in enumerate(vals):
    plain(ax, i, v + 22, f"{v} 万", fontsize=12.5, color=colors[i],
          weight="bold", va="bottom", ha="center")

ax.set_xticks(range(3))
ax.set_xticklabels(names, fontsize=11)
ax.set_ylim(0, 950)
ax.set_xlim(-0.62, 2.62)
style_axes(ax, ylabel="同一笔 1 亿美元证券的费用（万美元）",
           title="卖一只新股，比倒一次手赚得多得多（相差 4~16 倍）",
           title_size=12.5, grid_axis="y")
plain(ax, -0.60, -160,
      "按原书 p32 的数字推算：承销总费用为融资额的 2%~8%；",
      fontsize=10, color=C_GRAY, ha="left", va="top")
plain(ax, -0.60, -240,
      "机构二级市场佣金 5 美分/股，股价按 10 美元算即 0.5%。",
      fontsize=10, color=C_GRAY, ha="left", va="top")

# ══════════════════════════════════════════════════════════════════
#  右：谁出钱、谁承担结果
# ══════════════════════════════════════════════════════════════════
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

plain(ax, 5.0, 9.75, "钱先到手的人，和结果全扛的人", fontsize=13.5,
      weight="bold", color="#222222")

box(ax, 0.10, 8.35, 4.25, 0.95, "华尔街（收费方）", fc=F_ORANGE,
    ec=C_ORANGE, fontsize=12, weight="bold")
box(ax, 5.65, 8.35, 4.25, 0.95, "你（出钱方）", fc=F_BLUE,
    ec=C_BLUE, fontsize=12, weight="bold")

rows_w = ["费用先收，交易成不成、\n后来涨不涨，都不退",
          "不拿你的股票，\n价格跌了不关它的事",
          "你交易越多、发行越多，\n它的收入越多"]
rows_y = ["费用先付，钱一出手\n就已经少了一截",
          "股票在你账上，\n涨跌全部归你",
          "你越少动手，\n它收入越少——它的话要打折听"]
for i, y in enumerate((6.62, 4.77, 2.92)):
    box(ax, 0.10, y, 4.25, 1.20, rows_w[i], fc=F_ORANGE, ec=C_ORANGE,
        fontsize=10.5)
    box(ax, 5.65, y, 4.25, 1.20, rows_y[i], fc=F_BLUE, ec=C_BLUE,
        fontsize=10.5)

vline(ax, 5.00, 2.55, 9.30, color=C_GRAY, lw=1.4, ls=":")

box(ax, 0.10, 1.05, 9.80, 1.10,
    "同一笔钱，一方拿的是确定的现金，一方扛的是不确定的结果。",
    fc="#f7f7f7", ec=C_GRAY, fontsize=12, weight="bold")

save(fig, "w4d0_underwriting_vs_trading.png")
