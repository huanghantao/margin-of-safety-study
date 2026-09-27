"""Week 11 第 2 章配图：破产投资的三个阶段——价格带与最终偿付。

纵轴是"每 100 元面值的债券价格（元）"。三段时间里，市场给出的价格区间
（带子）越往后越窄：不确定性在变小，但离最终偿付也越来越近。

**全部是简化示意数字，用于教学，不是任何一只真实债券的报价。**
最终偿付 70 元也是示意，对应后文"算一算"里 70 元的结果。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, hline, vline,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY)

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# (x 起点, x 终点, 价格下沿, 价格上沿, 颜色, 阶段名)
BANDS = [
    (0.0, 3.0, 10, 35, C_RED, "第一阶段"),
    (3.0, 9.0, 30, 58, C_ORANGE, "第二阶段"),
    (9.0, 12.0, 55, 66, C_BLUE, "第三阶段"),
]
PAYOUT = 70

fig, ax = plt.subplots(figsize=(13.0, 7.6))

for x0, x1, lo, hi, color, name in BANDS:
    ax.add_patch(Rectangle((x0, lo), x1 - x0, hi - lo, fc=color, alpha=0.22,
                           ec=color, lw=2.0, zorder=2))
    label(ax, (x0 + x1) / 2, (lo + hi) / 2,
          f"{name}\n{lo} ~ {hi} 元", fontsize=12, color=color, weight="bold",
          zorder=6)

hline(ax, PAYOUT, -0.35, 12.35, color=C_GREEN, lw=2.2, ls="--", zorder=4)
label(ax, 0.10, PAYOUT + 3.4, "最终偿付：每 100 元面值拿回 70 元（示意）",
      fontsize=11.5, color=C_GREEN, ha="left", zorder=6)

plain(ax, 0.05, 92,
      "第一阶段：最乱，也最便宜",
      fontsize=12, weight="bold", color=C_RED, ha="left")
plain(ax, 0.05, 86.5,
      "财报推迟或干脆没有\n表外负债看不清\n持有人被迫不计价格卖出",
      fontsize=10.5, ha="left", va="top", color="#333333")

plain(ax, 6.0, 92,
      "第二阶段：开始谈重组计划",
      fontsize=12, weight="bold", color=C_ORANGE, ha="center")
plain(ax, 6.0, 86.5,
      "分析师把生意和账翻清楚了\n价格里装进了更多信息\n但计划长什么样仍不确定",
      fontsize=10.5, ha="center", va="top", color="#333333")

plain(ax, 11.95, 92,
      "第三阶段：计划已定，等生效",
      fontsize=12, weight="bold", color=C_BLUE, ha="right")
plain(ax, 11.95, 86.5,
      "通常 3 个月到 1 年\n最像风险套利\n回报最低，但最可预测",
      fontsize=10.5, ha="right", va="top", color="#333333")

style_axes(ax, xlabel="时间（月，示意）", ylabel="每 100 元面值的价格（元）",
           title="破产的三个阶段：不确定性在缩小，回报空间也在缩小", grid_axis="y")

ax.set_xlim(-0.4, 12.4)
ax.set_ylim(0, 100)
ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_xticks([0, 3, 6, 9, 12])
ax.set_xticklabels(["0\n申请破产", "3\n开始谈计划", "6", "9\n计划获批",
                    "12\n摆脱破产"], fontsize=10)

save(fig, "w11d2_three_stages.png")
