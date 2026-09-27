"""Week 8 第 4 章配图一：Beta 的几何含义。

横轴：大盘涨跌幅；纵轴：这只基金（或股票）的涨跌幅。
三条过原点的直线，斜率就是 Beta：1.5 / 1.0 / 0.5。
真实坐标，带刻度。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, style_axes, vline,
                             C_BLUE, C_GREEN, C_RED)

fig, ax = plt.subplots(figsize=(11.6, 7.0))

xs = [-18, 18]
for beta, color, name in ((1.5, C_RED, "Beta = 1.5"),
                          (1.0, C_BLUE, "Beta = 1.0"),
                          (0.5, C_GREEN, "Beta = 0.5")):
    ax.plot(xs, [beta * x for x in xs], color=color, lw=2.6, zorder=3)
    ax.plot([18], [beta * 18], "o", color=color, ms=8, zorder=5)
    label(ax, 19.4, beta * 18, name, fontsize=11.5, color=color, ha="left")

vline(ax, 10, 0, 15, color="#888888", lw=1.4, ls=(0, (4, 4)), zorder=2)
for beta, color in ((1.5, C_RED), (1.0, C_BLUE), (0.5, C_GREEN)):
    ax.plot([10], [beta * 10], "o", color=color, ms=9, zorder=6)

label(ax, -19.4, 28.6,
      "怎么读这张图\n"
      "横轴：大盘（指数）涨跌了多少\n"
      "纵轴：这只基金涨跌了多少\n"
      "斜率（纵轴变化 除以 横轴变化）= Beta\n"
      "大盘涨 10% 时：Beta 1.5 的涨 15%，Beta 1.0 的涨 10%，"
      "Beta 0.5 的只涨 5%",
      fontsize=11, color="#333333", ha="left", va="top")

label(ax, 0, -24.5,
      "大盘跌 10% 时同理：Beta = 1.5 的那只平均跌 15%。",
      fontsize=11, color="#444444")

ax.set_xlim(-21, 25)
ax.set_ylim(-30, 31)
ax.set_xticks([-20, -10, 0, 10, 20])
ax.set_xticklabels(["-20%", "-10%", "0", "+10%", "+20%"])
ax.set_yticks([-30, -15, 0, 15, 30])
ax.set_yticklabels(["-30%", "-15%", "0", "+15%", "+30%"])
style_axes(ax, xlabel="大盘（指数）的涨跌幅", ylabel="这只基金的涨跌幅",
           title="Beta 就是这条线的斜率：大盘涨 10%，它平均涨多少",
           grid_axis="both")

save(fig, "w8d4_beta_geometry.png")
