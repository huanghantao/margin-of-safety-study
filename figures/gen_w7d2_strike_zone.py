"""Week 7 第 2 章配图：价值投资者的好球区。

横轴是"买入价 ÷ 保守估算的价值"（越小越便宜），纵轴是"你对这家公司的把握"。
好球区 = 又便宜又看得懂；最理想击球区 = 便宜得更多。图中的公司只是示意位置。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, vline,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GOLD,
                             C_GRAY, C_DARK)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 7))

# ── 两个区域 ────────────────────────────────────────────────────────
ax.axvspan(0.30, 0.70, color=C_GREEN, alpha=0.10, zorder=0)
ax.axvspan(0.30, 0.55, color=C_GOLD, alpha=0.16, zorder=1)
vline(ax, 0.70, 0.0, 6.4, color=C_GREEN, lw=1.6, ls="--", zorder=2)
vline(ax, 1.00, 0.0, 6.4, color=C_GRAY, lw=1.6, ls="--", zorder=2)

plain(ax, 0.50, 2.30, "好球区：不高于七折", fontsize=12, color=C_GREEN,
      weight="bold")
plain(ax, 0.42, 1.72, "最理想区：不高于五五折", fontsize=12, color=C_GOLD,
      weight="bold")
label(ax, 0.72, 6.20, "好球区边界（七折）", fontsize=10.5, color=C_GREEN, ha="left")
label(ax, 1.02, 6.20, "价值本身（1.00）", fontsize=10.5, color=C_GRAY, ha="left")

# ── 八个投过来的球（示意位置） ──────────────────────────────────────
pitches = [
    (1.30, 4.0, "热门新股", "right"),
    (1.00, 2.6, "周期股", "left"),
    (0.85, 3.4, "银行股", "left"),
    (0.78, 5.0, "消费股", "left"),
    (0.66, 4.3, "水电股", "left"),
    (0.50, 1.0, "科技股", "left"),
    (0.45, 3.0, "困境股", "left"),
    (0.52, 5.3, "分拆股", "left"),
]
for x, y, name, side in pitches:
    ax.scatter([x], [y], s=90, color=C_BLUE, zorder=5,
               edgecolors="white", linewidths=1.4)
    if side == "left":
        label(ax, x + 0.02, y, name, fontsize=11, ha="left")
    else:
        label(ax, x - 0.02, y, name, fontsize=11, ha="right")

label(ax, 1.30, 3.45, "看得懂，但太贵：\n价格已经在价值之上", fontsize=11,
      color=C_RED)
label(ax, 0.62, 0.42, "很便宜，但看不懂：\n这不是你的好球", fontsize=11,
      color=C_RED, ha="left")

ax.set_xlim(0.25, 1.75)
ax.set_ylim(0, 6.6)
ax.set_xticks([0.4, 0.55, 0.7, 0.85, 1.0, 1.3])
ax.set_xticklabels(["0.40", "0.55", "0.70", "0.85", "1.00", "1.30"])
ax.set_yticks([1.0, 2.5, 4.0, 5.5])
ax.set_yticklabels(["很低", "一般", "较高", "很高"])
style_axes(ax, xlabel="买入价 ÷ 保守估算的价值（越小越便宜）",
           ylabel="你对这家公司的把握",
           title="没有裁判喊好球：这八个球，你只需要打其中一两个（示意位置）",
           grid_axis="x")

fig.tight_layout(pad=1.5)
save(fig, "w7d2_strike_zone.png")
