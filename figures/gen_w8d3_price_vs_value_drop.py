"""Week 8 第 3 章配图二：价格跌了 40%，可能是礼物，也可能是陷阱。

左右两个子图里，橙色的价格线完全一样（10 元跌到 6 元）；
唯一不同的是那条绿色的内在价值线。
真实坐标，横轴时间（月），纵轴元/股。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (fig_multi, save, label, plain, style_axes,
                             C_GREEN, C_ORANGE)

months = list(range(13))
price = [10.0, 9.4, 8.7, 8.0, 7.4, 6.9, 6.5, 6.2, 6.0, 6.0, 6.0, 6.0, 6.0]
value_flat = [10.0] * 13
value_down = [10.0, 9.6, 9.0, 8.2, 7.4, 6.8, 6.2, 5.6, 5.2, 4.8, 4.5,
              4.2, 4.0]

fig, axes = fig_multi(1, 2, width=13.4, height=6.4)
axL, axR = axes

for ax, value, title in ((axL, value_flat, "A：价格跌了，价值没跌"),
                         (axR, value_down, "B：价格跌了，价值跌得更多")):
    ax.plot(months, value, color=C_GREEN, lw=2.6, ls=(0, (6, 4)), zorder=3)
    ax.plot(months, price, color=C_ORANGE, lw=2.8, zorder=4)
    ax.set_xlim(-0.4, 12.4)
    ax.set_ylim(-0.6, 13.4)
    ax.set_xticks([0, 3, 6, 9, 12])
    style_axes(ax, xlabel="时间（月）", ylabel="元 / 股", title=title,
               grid_axis="y")

label(axL, 12.1, 10.8, "内在价值 10.00 元（没变）", fontsize=10.5,
      color=C_GREEN, ha="right")
label(axL, 12.1, 4.6, "价格 6.00 元（跌了 40%）", fontsize=10.5,
      color=C_ORANGE, ha="right")
plain(axL, 0.3, -1.55, "比较：价格比价值低 4.00 元，等于打了六折 → 波动是礼物",
      fontsize=11, color="#444444", ha="left", va="center")

label(axR, 12.1, 2.9, "内在价值只剩 4.00 元", fontsize=10.5,
      color=C_GREEN, ha="right")
label(axR, 12.1, 6.9, "价格 6.00 元（也跌了 40%）", fontsize=10.5,
      color=C_ORANGE, ha="right")
plain(axR, 0.3, -1.55, "比较：价格比价值还高 2.00 元，等于贵了五成 → 波动是陷阱",
      fontsize=11, color="#444444", ha="left", va="center")

fig.suptitle("同一段价格下跌，两种完全不同的风险：只看价格，这两张图一模一样",
             fontsize=14, weight="bold", y=1.0)

save(fig, "w8d3_price_vs_value_drop.png")
