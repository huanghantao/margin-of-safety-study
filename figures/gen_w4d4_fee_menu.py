"""W4 第 4 章图一：A 股／港股投资者一年要付的显性费用清单。

同样 10 万元放一年，自己买卖、宽基 ETF、主动权益基金、投顾组合的显性费用
（元）。费率取常见量级的约数，正文另有说明。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, style_axes,
                             C_GREEN, C_RED, C_ORANGE, C_GRAY, C_BLUE)

items = [
    ("自己买卖，全年只动 1 个回合", 109),
    ("宽基 ETF：管理 0.15% + 托管 0.05%", 200),
    ("自己买卖，全年动 4 个回合", 436),
    ("主动权益基金：管理 1.2% + 托管 0.2%", 1400),
    ("主动权益基金 + 申购 0.15% + 赎回 0.25%", 1800),
    ("投顾组合：投顾 0.5% + 底层 1.4%", 1900),
]
labels = [a for a, _ in items]
vals = [b for _, b in items]
colors = [C_GREEN, C_GREEN, C_ORANGE, C_RED, "#a81c1c", "#7f1010"]

fig, ax = plt.subplots(figsize=(12.6, 6.6))
fig.subplots_adjust(top=0.86, bottom=0.21, left=0.345, right=0.97)

ypos = list(range(len(vals)))
ax.barh(ypos, vals, height=0.56, color=colors, zorder=3)
for i, v in enumerate(vals):
    plain(ax, v + 45, i, f"{v:,} 元（{v / 1000:.2f}%）", fontsize=11.5,
          color=colors[i], weight="bold", va="center", ha="left")

ax.set_yticks(ypos)
ax.set_yticklabels(labels, fontsize=11)
ax.set_xlim(0, 2500)
ax.set_ylim(len(vals) - 0.55, -0.55)
style_axes(ax, xlabel="10 万元放一年要付的显性费用（元）",
           title="同样 10 万元放一年：最省和最贵，差出十几倍", grid_axis="x")

fig.text(0.345, 0.055,
         "费率为常见量级的约数，具体以你的券商 App 与基金合同为准；"
         "只算显性费用，未含买卖价差。",
         fontsize=10, color=C_GRAY, ha="left", va="center")

save(fig, "w4d4_fee_menu.png")
