"""Week 2 第 3 章配图：把未来的 100 元折回今天。

三个贴现率（5% / 10% / 15%）下，第 1、2、3 年收回的 100 元分别值今天的多少钱。
真实坐标柱状图。数字由"一年一年地除"算得。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, style_axes, label, hline,
                             C_BLUE, C_GREEN, C_GOLD)

fig, ax = plt.subplots(figsize=(11, 6.2))

groups = ["第 1 年的 100 元", "第 2 年的 100 元", "第 3 年的 100 元"]
series = [
    ("贴现率 5%", [95.24, 90.70, 86.38], C_GREEN),
    ("贴现率 10%", [90.91, 82.64, 75.13], C_BLUE),
    ("贴现率 15%", [86.96, 75.61, 65.75], C_GOLD),
]

width, offsets = 0.22, [-0.26, 0.0, 0.26]
for (name, vals, color), off in zip(series, offsets):
    xs = [i + off for i in range(3)]
    ax.bar(xs, vals, width=width, color=color, label=name, zorder=3)
    for x, v in zip(xs, vals):
        label(ax, x, v + 2.0, f"{v:.2f}", fontsize=9, color=color)

hline(ax, 100, -0.55, 2.55, color="#999999", lw=1.2, ls=(0, (4, 4)), zorder=1)
label(ax, 2.3, 104.5, "三年后拿到的都是 100 元", fontsize=10.5, color="#555555")

ax.set_xlim(-0.7, 2.7)
ax.set_ylim(0, 132)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(groups, fontsize=11.5)
ax.legend(loc="upper right", fontsize=10.5, frameon=False)
style_axes(ax, ylabel="折回今天，值多少元",
           title="同样收回 100 元：利率越高，折算到今天就越是「缩水」")

save(fig, "w2d3_discount.png")
