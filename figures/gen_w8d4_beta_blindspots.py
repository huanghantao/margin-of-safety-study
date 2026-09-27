"""Week 8 第 4 章配图二：Beta 看不见的那根轴。

横轴 = 过去的价格波动（Beta 只看这根轴）；
纵轴 = 本金永久损失的可能性（Beta 不看这根轴）。
四个象限各放一个例子。真实坐标 + 虚线十字。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, plain, style_axes, hline, vline,
                             C_GREEN, C_RED, C_BLUE, C_ORANGE, C_GRAY)

fig, ax = plt.subplots(figsize=(11.6, 7.2))

vline(ax, 5, 0, 10, color=C_GRAY, lw=1.3, ls=(0, (5, 4)), zorder=1)
hline(ax, 5, 0, 10, color=C_GRAY, lw=1.3, ls=(0, (5, 4)), zorder=1)

points = [
    (2.0, 2.0, C_GREEN, "A  稳定的公用事业股，买价还打了折\n（波动小，也真的安全）"),
    (2.0, 8.0, C_RED, "B  慢慢阴跌的没落公司\n（波动小，本金却在一点点消失）"),
    (7.8, 2.0, C_BLUE, "C  现金比市值还多的周期股\n（波动大，但下跌有底）"),
    (7.8, 8.0, C_ORANGE, "D  靠概念和杠杆撑起来的热门股\n（波动大，也可能亏光）"),
]
for x, y, color, text in points:
    ax.plot([x], [y], "o", color=color, ms=13, zorder=5)
    ax.plot([x], [y], "o", color="white", ms=5, zorder=6)

label(ax, 2.0, 0.95, points[0][3], fontsize=10.5, color=C_GREEN)
label(ax, 2.0, 9.15, points[1][3], fontsize=10.5, color=C_RED)
label(ax, 7.8, 0.95, points[2][3], fontsize=10.5, color=C_BLUE)
label(ax, 7.8, 9.15, points[3][3], fontsize=10.5, color=C_ORANGE)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([2, 8])
ax.set_xticklabels(["波动小", "波动大"], fontsize=11.5)
ax.set_yticks([2, 8])
ax.set_yticklabels(["亏钱的可能小", "亏钱的可能大"], fontsize=11.5)
style_axes(ax, xlabel="过去的价格波动有多大 —— Beta 只看这一根轴",
           ylabel="本金永久损失的可能性有多大 —— Beta 不看这一根轴",
           title="Beta 只在横轴上排座次，钱却是在纵轴上亏掉的",
           grid_axis=None)

save(fig, "w8d4_beta_blindspots.png")
