"""W3 第 3 章图一：亏掉多少，就要涨回多少才回本（真实坐标柱状图）。

左图：亏 10%~70% 对应的回本涨幅；右图：亏 80%、90% 的情况（纵轴刻度完全不同）。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, style_axes,
                             C_RED, C_ORANGE, C_GOLD, C_GREEN, C_GRAY, C_DARK)

fig, axes = plt.subplots(1, 2, figsize=(12.4, 6.4))
fig.subplots_adjust(top=0.80, wspace=0.28)

lossA = ["10%", "20%", "30%", "40%", "50%", "60%", "70%"]
needA = [11, 25, 43, 67, 100, 150, 233]
colorsA = [C_GREEN, C_GREEN, C_GOLD, C_GOLD, C_ORANGE, C_RED, C_RED]

ax = axes[0]
bars = ax.bar(range(len(lossA)), needA, width=0.62, color=colorsA, zorder=3)
for i, v in enumerate(needA):
    plain(ax, i, v + 8, f"+{v}%", fontsize=12, color=colorsA[i],
          weight="bold", va="bottom", ha="center")
ax.axhline(100, color=C_GRAY, lw=1.4, ls="--", zorder=1)
plain(ax, -0.42, 118, "涨 100% = 翻一倍", fontsize=10.5, color=C_GRAY,
      ha="left", va="bottom")
ax.set_xticks(range(len(lossA)))
ax.set_xticklabels([f"亏 {x}" for x in lossA], fontsize=11)
ax.set_ylim(0, 300)
style_axes(ax, ylabel="回本需要上涨的幅度", title="A：亏 10%～70%",
           grid_axis="y")

lossB = ["80%", "90%"]
needB = [400, 900]
ax = axes[1]
ax.bar(range(len(lossB)), needB, width=0.45, color=[C_RED, "#7f1010"], zorder=3)
for i, v in enumerate(needB):
    plain(ax, i, v + 30, f"+{v}%", fontsize=13, color=C_RED,
          weight="bold", va="bottom", ha="center")
ax.set_xticks(range(len(lossB)))
ax.set_xticklabels([f"亏 {x}" for x in lossB], fontsize=11)
ax.set_xlim(-0.7, 1.7)
ax.set_ylim(0, 1150)
style_axes(ax, ylabel="回本需要上涨的幅度", title="B：亏 80% 和 90%",
           grid_axis="y")

fig.suptitle("亏钱是复利的反面：亏得越多，回本需要的涨幅涨得越不成比例",
             fontsize=14, weight="bold", y=0.96)
plain(axes[1], 1.62, -170, "两幅图的纵轴刻度完全不同，注意对比", fontsize=10.5,
      color=C_GRAY, ha="right", va="center")
plain(axes[0], -0.42, -30, "以下柱标为取整后的数字（精确值见正文表格），由「亏损 p 之后回本需涨 p/(1-p)」算出",
      fontsize=10.5, color=C_GRAY, ha="left", va="center")

save(fig, "w3d3_loss_recovery.png")
