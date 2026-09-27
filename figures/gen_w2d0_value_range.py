"""Week 2 第 0 章配图：价值是一个区间，价格只是区间外的一个点。

真实坐标：横轴是"每股价值 / 价格（元）"，几何比例自己说话。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from figures._common import (save, style_axes, label, brace, hline, vline,
                             C_BLUE, C_GREEN, C_ORANGE, F_GREEN, F_BLUE)

fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)
style_axes(ax, xlabel="每股价值 / 价格（元）",
           title="价值是一个区间，价格只是区间外的一个点", grid_axis="x")
ax.set_yticks([])

# 估值区间（60 ~ 80 元）
ax.add_patch(Rectangle((60, 5.0), 20, 1.0, fc=F_GREEN, ec=C_GREEN, lw=1.6,
                       zorder=3))
ax.plot([60, 70, 80], [5.5, 5.5, 5.5], "o", color=C_GREEN, ms=9, zorder=5)

label(ax, 60, 6.55, "保守 60 元", fontsize=11, color=C_GREEN)
label(ax, 70, 7.55, "中性 70 元", fontsize=11, color=C_GREEN)
label(ax, 80, 6.55, "乐观 80 元", fontsize=11, color=C_GREEN)
label(ax, 76, 4.6, "同一家公司，三种假设算出的三个数字",
      fontsize=11.5, color="#222222")

# 今天的市价（42 元）
ax.plot([42], [2.6], marker="D", color=C_ORANGE, ms=11, zorder=5)
label(ax, 42, 1.85, "今天的市价 42 元", fontsize=11.5, color=C_ORANGE)

brace(ax, 42, 60, 3.5, "18 元的安全边际", color=C_BLUE, fontsize=11)

save(fig, "w2d0_value_range.png")
