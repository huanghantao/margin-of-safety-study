"""W5 第 2 章配图：没有裁判喊好球 —— 12 个投过来的球，只挥 3 棒。

真实坐标柱状图：纵轴是"价格比你估的价值便宜多少（%）"。
绿色带是"好球区"（便宜 20% 以上），落在带里的柱只有 3 根。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, label, plain, style_axes,
                             C_GREEN, C_GRAY, C_DARK)

fig, ax = plt.subplots(figsize=(11.5, 6.6))

discount = [8, 5, 22, 12, 3, 30, 14, 6, 2, 25, 9, 4]   # 每个机会的折扣（%）
x = list(range(1, 13))
colors = [C_GREEN if d >= 20 else "#c9c9c9" for d in discount]

ax.axhspan(20, 33, color=C_GREEN, alpha=0.13, zorder=1)
ax.axhline(20, color=C_GREEN, lw=1.6, ls="--", zorder=2)
ax.bar(x, discount, width=0.62, color=colors, edgecolor="white", zorder=3)

for xi, d in zip(x, discount):
    plain(ax, xi, d + 0.7, str(d), fontsize=10.5, color=C_DARK, va="bottom")

label(ax, 0.55, 30.4, "好球区：价格比你保守估的价值低 20% 以上",
      color=C_GREEN, fontsize=12, ha="left", va="center", weight="bold")
label(ax, 6.5, -8.5,
      "机构：场上一直有裁判在喊好球——12 个球全得挥（永远满仓）\n"
      "你：没有裁判——12 个球里只挥第 3、6、10 个，其余 9 个可以放过",
      color=C_DARK, fontsize=11.5, ha="center", va="center")

ax.set_xlim(0.3, 12.7)
ax.set_ylim(-13.5, 35)
ax.set_xticks(x)
style_axes(ax, xlabel="一年里飞过来的 12 个投资机会",
           ylabel="价格比价值便宜多少（%）",
           title="没有裁判喊好球：放过 9 个球，不算你输",
           grid_axis="y")
plain(ax, 12.65, -11.8, "数字为简化示意，用于教学", fontsize=10.5, color=C_GRAY,
      ha="right", va="center")

save(fig, "w5d2_full_swing.png")
