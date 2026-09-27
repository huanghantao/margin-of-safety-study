"""Week 8 第 3 章配图一：波动一样大，结局不一样。

两条股价走势（真实坐标折线图）：
  A 公司：生意没坏，价格跌下去又涨回来，期末 12.00 元；
  B 公司：生意真的变坏了，价格反弹过又跌回去，期末 6.00 元。
两条线的最高价都是 12.00 元、最低价都是 6.00 元 —— 按「波动」衡量，风险一模一样。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, style_axes, hline,
                             C_GREEN, C_RED, C_GRAY)

months = list(range(25))
price_a = [10.0, 9.4, 8.6, 7.6, 7.0, 6.4, 6.0, 6.6, 7.4, 8.2, 9.0,
           9.8, 10.6, 11.3, 11.8, 12.0, 11.4, 10.8, 11.2, 11.6, 11.9,
           12.0, 11.8, 12.0, 12.0]
price_b = [10.0, 10.6, 11.2, 11.8, 12.0, 11.4, 10.6, 9.6, 8.6, 7.6, 6.8,
           6.2, 6.0, 6.4, 7.0, 7.6, 8.2, 8.6, 8.2, 7.6, 7.0, 6.6, 6.2,
           6.0, 6.0]

fig, ax = plt.subplots(figsize=(11.6, 6.6))

ax.plot(months, price_a, color=C_GREEN, lw=2.6, zorder=4)
ax.plot(months, price_b, color=C_RED, lw=2.6, zorder=4)

hline(ax, 10.0, 0, 24, color=C_GRAY, lw=1.3, ls=(0, (5, 4)), zorder=1)
label(ax, 1.0, 10.55, "买入价 10.00 元", fontsize=10.5, color=C_GRAY,
      ha="left")

label(ax, 6.0, 5.35, "A 最低 6.00 元", fontsize=10.5, color=C_GREEN)
label(ax, 12.4, 5.35, "B 最低 6.00 元", fontsize=10.5, color=C_RED)

label(ax, 23.6, 12.7,
      "A 公司：生意没坏\n最高也到过 12.00 元，期末 12.00 元（+20%）",
      fontsize=10.5, color=C_GREEN, ha="right")

label(ax, 23.6, 4.35,
      "B 公司：生意真的变坏了\n最高也到过 12.00 元，期末 6.00 元（-40%）",
      fontsize=10.5, color=C_RED, ha="right")

ax.set_xlim(0, 24)
ax.set_ylim(3.6, 14.4)
ax.set_xticks([0, 4, 8, 12, 16, 20, 24])
style_axes(ax, xlabel="时间（月）", ylabel="股价（元）",
           title="波动一样大，结局不一样：最高价都是 12 元，最低价都是 6 元",
           grid_axis="y")

save(fig, "w8d3_volatility_vs_risk.png")
