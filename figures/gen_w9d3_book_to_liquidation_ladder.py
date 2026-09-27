"""Week 9 第 3 章核心配图（★）：从账面价值一级一级打折到清算价值。

真实坐标的瀑布图（阶梯图）：横轴是每一级扣减，纵轴是每股还剩多少元。
每一根柱子都落在真实高度上，读者能直接看出「账面 100 元」
是怎么一路掉到「清算 42 元」的。

数字是**教学示意数字**，用来演示原书 p145–p146 描述的扣减顺序，
不是任何一家真实公司的财报。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label, arrow, hline,
                             C_BLUE, C_GREEN, C_RED, C_GRAY, style_axes)

labels = ["账面价值\n（账本净资产）",
          "减：商誉与\n无形资产",
          "减：厂房与\n设备打折",
          "减：库存\n打折",
          "减：应收\n账款打折",
          "减：清算费用\n遣散环保",
          "清算价值\n（关门能剩）"]

# (起点, 高度, 颜色, 柱顶标注)
steps = [
    (0.0, 100.0, C_BLUE, "100 元"),
    (80.0, 20.0, C_RED, "-20"),
    (62.0, 18.0, C_RED, "-18"),
    (54.0, 8.0, C_RED, "-8"),
    (50.0, 4.0, C_RED, "-4"),
    (42.0, 8.0, C_RED, "-8"),
    (0.0, 42.0, C_GREEN, "42 元"),
]

fig, ax = plt.subplots(figsize=(13, 6.8))

for i, (base, h, c, txt) in enumerate(steps):
    ax.add_patch(plt.Rectangle((i - 0.32, base), 0.64, h, fc=c, ec=c,
                               lw=1.4, zorder=3, alpha=0.9))
    plain(ax, i, base + h + 3.0, txt, fontsize=11.5, weight="bold",
          color="#222222", va="bottom")

# 阶梯之间的虚线连接：从上一级的高度，平着拉到下一根柱子
for i in range(len(steps) - 1):
    level = steps[0][1] if i == 0 else steps[i][0]
    hline(ax, level, i + 0.32, i + 1 - 0.32, color=C_GRAY, lw=1.1,
          ls=(0, (4, 3)), zorder=2)

# 最右侧：整体打了多少折
arrow(ax, (7.0, 42), (7.0, 100), color=C_RED, lw=2.0, style="<|-|>",
      zorder=4)
label(ax, 7.35, 71, "账面 100 元\n清算只剩 42 元\n一共少了 58%", fontsize=11.5,
      color=C_RED, ha="left")

ax.set_xlim(-0.78, 10.0)
ax.set_ylim(0, 122)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=10.5)
ax.set_yticks([0, 20, 40, 60, 80, 100])

style_axes(ax, ylabel="每股还剩多少元（教学示意数字）",
           title="从账面价值一级一级打折到清算价值：每一步都在扣掉「卖不掉的价钱」")

save(fig, "w9d3_book_to_liquidation_ladder.png")
