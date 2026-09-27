"""Week 7 第 2 章配图：企业价值本身会移动。

同一家公司在同一天被估出 20 元的保守价值，但五年后它可能值 27.5 元（通胀、
生意变好），也可能只值 12.5 元（通缩、生意变差）。所以"打五折"这件事，
必须放在"价值会动"的前提下思考。全部为简化示意数字。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, hline,
                             C_BLUE, C_GREEN, C_RED, C_ORANGE, C_GRAY)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(11.6, 6.6))

years = [0, 1, 2, 3, 4, 5]
up = [20, 21.5, 23, 24.5, 26, 27.5]
down = [20, 18.5, 17, 15.5, 14, 12.5]

ax.fill_between(years, [v - 1.5 for v in up], [v + 1.5 for v in up],
                color=C_GREEN, alpha=0.16, zorder=1)
ax.fill_between(years, [v - 1.5 for v in down], [v + 1.5 for v in down],
                color=C_RED, alpha=0.14, zorder=1)
ax.plot(years, up, color=C_GREEN, lw=2.6, marker="o", zorder=3)
ax.plot(years, down, color=C_RED, lw=2.6, marker="o", zorder=3)

hline(ax, 10, 0, 5.25, color=C_ORANGE, lw=2.0, ls="--", zorder=2)

label(ax, 0.06, 11.4, "你的买入价 10 元（当时正好是价值的一半）",
      fontsize=11.5, color=C_ORANGE, ha="left", weight="bold")
label(ax, 3.75, 29.6, "通胀路径：价值升到约 27.5 元\n你的 10 元买价相当于 64% 的折扣",
      fontsize=11.5, color=C_GREEN, ha="center")
label(ax, 3.85, 17.3, "通缩路径：价值跌到约 12.5 元\n这时折扣只剩 20%，可能根本不算便宜",
      fontsize=11.5, color=C_RED, ha="center")

ax.set_xlim(0, 5.6)
ax.set_ylim(5, 33)
ax.set_xticks(years)
style_axes(ax, xlabel="第几年（0 = 今天）", ylabel="每股价值（元，示意数字）",
           title="企业价值并不像刻在石头上的印记那样永恒不变（简化示意数字）")

fig.tight_layout(pad=1.5)
save(fig, "w7d2_value_is_moving.png")
