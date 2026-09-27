"""Week 2 第 4 章配图：同一家公司，三种方法算出三个数字。

真实坐标柱状图；横线是今天的股价。数字为教学用的简化示意数字。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, style_axes, label, hline,
                             C_BLUE, C_GOLD, C_GREEN, C_ORANGE)

fig, ax = plt.subplots(figsize=(10.5, 6))

names = ["看资产\n（资产法）", "看盈利\n（盈利法）", "看现金流\n（现金流法）"]
values = [18, 28, 35]
colors = [C_GREEN, C_BLUE, C_GOLD]

ax.bar([0, 1, 2], values, width=0.5, color=colors, zorder=3)
for x, v in zip([0, 1, 2], values):
    label(ax, x, v + 1.4, f"{v} 元", fontsize=12, color="#222222")

hline(ax, 16, -0.6, 3.2, color=C_ORANGE, lw=1.8, ls=(0, (5, 3)), zorder=1)
label(ax, 2.62, 16.8, "今天的股价 16 元", fontsize=11, color=C_ORANGE,
      ha="left")

label(ax, 1.0, 41.5, "保守起见，先拿最低的 18 元当估值底线",
      fontsize=11.5, color=C_GREEN)

ax.set_xlim(-0.8, 3.4)
ax.set_ylim(0, 45)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(names, fontsize=11.5)
style_axes(ax, ylabel="每股价值（元，简化示意数字）",
           title="同一家示意公司：三种方法，三个数字")

save(fig, "w2d4_three_values.png")
