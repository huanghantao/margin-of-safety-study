"""Week 2 第 3 章配图：复利——100 元按每年 10% 长大。

真实坐标柱状图，柱子高度就是当年的金额。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, style_axes, label, hline,
                             C_BLUE, C_GOLD, C_GRAY)

fig, ax = plt.subplots(figsize=(11, 6))

years = [0, 1, 2, 3]
values = [100, 110, 121, 133.1]
xticks = ["今天", "第 1 年", "第 2 年", "第 3 年"]
colors = [C_BLUE, C_GOLD, C_GOLD, C_GOLD]

ax.bar(years, values, width=0.5, color=colors, zorder=3)
for x, v in zip(years, values):
    label(ax, x, v + 3.5, f"{v:g} 元", fontsize=11.5, color="#222222")

# 相邻两根柱子之间，说明乘了几次
for i in range(3):
    mid = (values[i] + values[i + 1]) / 2
    label(ax, i + 0.5, mid, "乘 1.1", fontsize=10.5, color=C_GRAY)

hline(ax, 100, -0.4, 3.4, color=C_GRAY, lw=1.1, ls=(0, (4, 4)), zorder=1)
label(ax, -0.5, 150, "虚线 = 本金 100 元", fontsize=11, color=C_BLUE, ha="left")

ax.set_xlim(-0.6, 3.6)
ax.set_ylim(0, 158)
ax.set_xticks(years)
ax.set_xticklabels(xticks, fontsize=11.5)
style_axes(ax, ylabel="手上的钱（元）",
           title="复利：每一年的利息，下一年也跟着生利息")

save(fig, "w2d3_compound.png")
