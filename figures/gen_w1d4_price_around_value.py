"""Week 1 第 4 章配图之一：价格围绕价值中枢上下波动（真实坐标折线图）。

橙线 = 每天跳动的报价；绿线 = 内在价值的中枢；浅绿带 = 价值的合理范围。
曲线是**示意数据**，只用来表现"价格波动远大于价值变化"这个结构。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

fig, ax = plt.subplots(figsize=(11.5, 6.4))

t = np.arange(0, 121)
value = 10.0 + 0.022 * t
price = (value
         + 2.6 * np.sin(t / 6.5)
         + 1.1 * np.sin(t / 2.9 + 1.0)
         + 0.7 * np.sin(t / 1.6 + 2.0))

ax.fill_between(t, value * 0.88, value * 1.12, color=F_GREEN, zorder=1)
ax.plot(t, value, color=C_GREEN, lw=2.4, zorder=3)
ax.plot(t, price, color=C_ORANGE, lw=1.8, zorder=4)

# 低点 / 高点
win_lo = (t >= 25) & (t <= 70)
win_hi = (t >= 80) & (t <= 118)
i_lo = int(np.argmin(np.where(win_lo, price, 1e9)))
i_hi = int(np.argmax(np.where(win_hi, price, -1e9)))

ax.plot([t[i_lo]], [price[i_lo]], marker="o", ms=9, color=C_RED, zorder=6)
label(ax, t[i_lo], 5.35, "最悲观的时候：报价约 8 元\n比价值中枢低一大截",
      fontsize=10.5, color=C_RED)
arrow(ax, (t[i_lo], 6.05), (t[i_lo], price[i_lo] - 0.35), color=C_RED, lw=1.5)

ax.plot([t[i_hi]], [price[i_hi]], marker="o", ms=9, color=C_BLUE, zorder=6)
label(ax, t[i_hi], 19.05, "最乐观的时候：报价约 17 元\n比价值中枢高出五成",
      fontsize=10.5, color=C_BLUE)
arrow(ax, (t[i_hi], 18.35), (t[i_hi], price[i_hi] + 0.35), color=C_BLUE, lw=1.5)

handles = [
    Line2D([], [], color=C_ORANGE, lw=2.2, label="市场价格：每天跳来跳去"),
    Line2D([], [], color=C_GREEN, lw=2.4, label="内在价值的中枢：变化慢得多"),
    Patch(facecolor=F_GREEN, edgecolor="none", label="价值的合理范围"),
]
ax.legend(handles=handles, loc="upper left", fontsize=10.5, framealpha=0.95)

style_axes(ax, xlabel="交易日（示意，共约半年）", ylabel="每股价格（元）",
           title="同一家公司：价格天天在变，价值慢得多",
           grid_axis="y", fontsize=11, title_size=13)
ax.set_xlim(0, 165)
ax.set_ylim(3, 20.6)

save(fig, "w1d4_price_around_value.png")
