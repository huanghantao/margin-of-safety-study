"""Week 2 第 1 章配图：从营业收入到自由现金流（奶茶店瀑布图）。

真实坐标柱状图，柱子高度按万元数值画。数字为简化示意数字。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, style_axes, label, hline,
                             C_BLUE, C_GREEN, C_RED, C_GOLD, C_GRAY)

fig, ax = plt.subplots(figsize=(11, 6.2))

names = ["营业收入", "各项成本", "净利润", "加回折旧",
         "经营现金流", "资本开支", "自由现金流"]
# (顶部值, 底部值, 颜色, 柱顶标注)
bars = [
    (60.0, 0.0, C_BLUE, "+60"),
    (60.0, 17.0, C_RED, "-43"),
    (17.0, 0.0, C_GREEN, "= 17"),
    (20.0, 17.0, C_GOLD, "+3"),
    (20.0, 0.0, C_BLUE, "= 20"),
    (20.0, 12.0, C_RED, "-8"),
    (12.0, 0.0, C_GREEN, "= 12"),
]

width = 0.7
centers = [i * 1.15 + 0.6 for i in range(len(bars))]

for cx, (top, bot, color, tag) in zip(centers, bars):
    ax.add_patch(plt.Rectangle((cx - width / 2, bot), width, top - bot,
                               fc=color, ec=color, lw=1.4, zorder=3))
    label(ax, cx, top + 3.0, tag, fontsize=11, color=color)

# 相邻柱之间的虚线连接，帮读者看清"从哪一段接到哪一段"
# level_after[i] = 第 i 根柱结束后，下一根柱接着的那个高度
level_after = [60.0, 17.0, 17.0, 20.0, 20.0, 12.0]
for i in range(len(bars) - 1):
    hline(ax, level_after[i], centers[i] + width / 2, centers[i + 1] - width / 2,
          color=C_GRAY, lw=1.0, ls=(0, (4, 4)), zorder=1)

ax.set_xlim(0, 8.3)
ax.set_ylim(0, 74)
ax.set_xticks(centers)
ax.set_xticklabels(names, fontsize=10.5)
style_axes(ax, ylabel="万元（简化示意数字）",
           title="奶茶店一年：从收入到自由现金流")

save(fig, "w2d1_cash_flow.png")
