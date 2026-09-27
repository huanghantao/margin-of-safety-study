"""W4 第 0 章图一：你的一次买入，钱流向了谁（佣金流向图 + 换手次数放大效应）。

左图：10 万元买入的现金流向（概念流程）；
右图：一年买卖 N 个回合，显性费用线性增长（真实坐标柱状图）。
费率取常见量级，属于"标注过的约数"，正文另有说明。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, box, arrow, plain, label, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_GRAY, C_RED,
                             F_BLUE, F_GREEN, F_ORANGE, F_RED)

fig, axes = plt.subplots(1, 2, figsize=(13.6, 7.0),
                         gridspec_kw={"width_ratios": [1.22, 1.0]})
fig.subplots_adjust(top=0.84, bottom=0.13, left=0.05, right=0.97, wspace=0.12)

# ══════════════════════════════════════════════════════════════════
#  左：钱流图
# ══════════════════════════════════════════════════════════════════
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

plain(ax, 5.0, 9.72, "你按下「买入」，10 万元是这样走掉的", fontsize=13.5,
      weight="bold", color="#222222")
plain(ax, 5.0, 9.18, "（单次买入，费率取常见量级，用于说明结构）", fontsize=10.5,
      color=C_GRAY)

box(ax, 0.15, 7.55, 6.10, 1.18,
    "你：输入「买入 10 万元」", fc=F_BLUE, ec=C_BLUE, fontsize=12.5,
    weight="bold")
box(ax, 0.15, 5.75, 6.10, 1.18,
    "券商：佣金 约 0.025%", fc=F_ORANGE, ec=C_ORANGE, fontsize=12.5)
box(ax, 0.15, 3.95, 6.10, 1.18,
    "交易所 + 登记结算：经手费、过户费", fc=F_RED, ec=C_RED, fontsize=12.5)
box(ax, 0.15, 2.05, 6.10, 1.30,
    "剩下的钱，才真正买到股票", fc=F_GREEN, ec=C_GREEN, fontsize=12.5,
    weight="bold")

for y0, y1 in ((7.55, 6.93), (5.75, 5.13), (3.95, 3.35)):
    arrow(ax, (3.20, y0), (3.20, y1), color=C_GRAY, lw=1.8)

label(ax, 7.55, 6.34, "扣 25 元", fontsize=12.5, color=C_ORANGE,
      weight="bold", ha="left")
label(ax, 7.55, 4.54, "扣 约 4 元", fontsize=12.5, color=C_RED,
      weight="bold", ha="left")
label(ax, 7.55, 2.70, "余 约 99 971 元", fontsize=12.5, color=C_GREEN,
      weight="bold", ha="left")

plain(ax, 0.15, 1.34,
      "费用按「你动手的次数」收，不按「你赚不赚钱」收——\n"
      "这笔交易哪怕一年后亏 20%，上面每一笔费用一分都不会少。",
      fontsize=11.5, color="#222222", ha="left", va="top")

# ══════════════════════════════════════════════════════════════════
#  右：换手次数放大效应
# ══════════════════════════════════════════════════════════════════
ax = axes[1]
rounds = [1, 5, 10, 20]
fees = [109, 545, 1090, 2180]
colors = [C_GREEN, C_ORANGE, C_RED, "#7f1010"]

bars = ax.bar(range(len(rounds)), fees, width=0.56, color=colors, zorder=3)
for i, v in enumerate(fees):
    plain(ax, i, v + 55, f"{v:,} 元", fontsize=12, color=colors[i],
          weight="bold", va="bottom", ha="center")

ax.set_xticks(range(len(rounds)))
ax.set_xticklabels([f"{r} 个回合" for r in rounds], fontsize=11.5)
ax.set_ylim(0, 2650)
ax.set_xlim(-0.65, 3.65)
style_axes(ax, ylabel="一年累计的显性费用（元）",
           title="同样 10 万元，动手越多，费用越高", grid_axis="y")
plain(ax, -0.62, -230,
      "1 个回合 = 买一次 + 卖一次；仅含佣金、印花税、经手费、过户费。",
      fontsize=10, color=C_GRAY, ha="left", va="top")
plain(ax, -0.62, -360,
      "未含买卖价差。为简化示意数字，不是真实账单。",
      fontsize=10, color=C_GRAY, ha="left", va="top")

save(fig, "w4d0_fee_flow.png")
