"""Week 2 第 5 章配图：安全边际——你可以在多大范围内估错还不亏。

真实坐标：横轴是每股价格（元）。蓝色区是"打折买到的空间"，
绿色区是估值区间。数字为教学用的简化示意数字。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, style_axes, label, brace, hline, vline,
                             C_BLUE, C_GREEN, C_ORANGE, C_GRAY)

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)

ax.axvspan(42, 60, color="#eaf2fa", zorder=0)
ax.axvspan(60, 80, color="#eaf6ec", zorder=0)

hline(ax, 5.0, 8, 94, color=C_GRAY, lw=1.2, zorder=2)
vline(ax, 42, 3.9, 6.0, color=C_ORANGE, lw=2.6, zorder=4)
vline(ax, 60, 3.9, 6.0, color=C_GREEN, lw=2.6, zorder=4)
vline(ax, 80, 3.9, 6.0, color=C_GREEN, lw=1.8, ls=(0, (4, 4)), zorder=4)

label(ax, 42, 6.85, "买入价 42 元", fontsize=11.5, color=C_ORANGE)
label(ax, 60, 6.85, "保守估值 60 元", fontsize=11.5, color=C_GREEN)
label(ax, 80, 6.85, "乐观估值 80 元", fontsize=11.5, color=C_GREEN)
label(ax, 70, 8.1, "估值区间：60 ~ 80 元", fontsize=12, color=C_GREEN)

brace(ax, 42, 60, 3.4, "18 元：这就是安全边际", color=C_BLUE, fontsize=11.5)

label(ax, 50, 2.55, "只要真实价值不低于 42 元，你就不亏", fontsize=11.5,
      color="#222222")
label(ax, 50, 1.6, "这就是「打折」的全部意义：为估错留出空间",
      fontsize=11.5, color="#222222")

style_axes(ax, xlabel="每股价格（元）",
           title="安全边际：买入价与保守估值之间的那段距离", grid_axis=None)
ax.set_yticks([])

save(fig, "w2d5_margin_zone.png")
