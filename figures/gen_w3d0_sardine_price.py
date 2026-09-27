"""W3 第 0 章图一：交易用沙丁鱼的价格一路被哄抬（真实坐标折线）。

教学用简化示意数字：一罐能吃的沙丁鱼大约值 10 元；被当成"筹码"炒作的
罐头价格被一路抬到 200 元，直到最后一个买家打开它。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, label, plain, style_axes,
                             C_GRAY, C_ORANGE, C_RED, C_GREEN, C_BLUE, C_DARK)

fig, ax = plt.subplots(figsize=(11, 6.6))

days = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [10, 14, 20, 32, 50, 72, 100, 140, 175, 200, 200]
after_days = [10, 10.6, 11.4]
after_price = [200, 90, 12]

# 内在价值参考线：一罐真的能吃的沙丁鱼
ax.axhline(10, color=C_GREEN, lw=2.0, ls="--", zorder=1)
label(ax, 0.25, 16, "一罐真能吃的沙丁鱼 = 10 元（食用价值）",
      color=C_GREEN, fontsize=12, ha="left", va="bottom", weight="bold")

# 价格折线
ax.plot(days, price, color=C_ORANGE, lw=2.8, marker="o", ms=6, zorder=4,
        label="交易用沙丁鱼的成交价")
ax.plot(after_days, after_price, color=C_RED, lw=2.4, ls=":", marker="o",
        ms=6, zorder=4, label="最后没人再接盘之后（示意）")

# 关键点标注
label(ax, 4.0, 118, "每一次转手都在加价：\n大家买它不是因为要吃，\n而是相信有人会出更高的价",
      color=C_DARK, fontsize=11.5, ha="left", va="center")
label(ax, 9.0, 214, "第 10 手：200 元", color=C_ORANGE, fontsize=12,
      weight="bold", ha="center", va="bottom")
label(ax, 10.9, 60, "最后一个买家\n打开罐子：臭了", color=C_RED,
      fontsize=11.5, ha="center", va="center", weight="bold")

ax.set_xlim(-0.6, 13.4)
ax.set_ylim(0, 250)
style_axes(ax, xlabel="转手次数（第几手买家）", ylabel="一罐沙丁鱼的价格（元）",
           title="交易用沙丁鱼：价格涨到 20 倍，罐子里的东西一点没变好",
           grid_axis="y")
ax.legend(loc="upper left", fontsize=11, frameon=True, bbox_to_anchor=(0.015, 0.80))
plain(ax, 13.3, -22, "数字为简化示意，用于教学", fontsize=10, color=C_GRAY,
      ha="right", va="center")

save(fig, "w3d0_sardine_price.png")
