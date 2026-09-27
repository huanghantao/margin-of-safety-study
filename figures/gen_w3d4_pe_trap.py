"""W3 第 4 章图二："买低市盈率" 公式为什么会在你手上失效（真实坐标三连图）。

盈利跌一半，股价只跌两成 —— 市盈率反而从 10 倍涨到 16 倍。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, style_axes,
                             C_ORANGE, C_GREEN, C_RED, C_GRAY, C_DARK)

fig, axes = plt.subplots(1, 3, figsize=(12.6, 6.2))
fig.subplots_adjust(top=0.78, wspace=0.42)

xs = [0, 1]
labels = ["买入时", "一年后"]


def panel(ax, values, colors, fmt, ylim, title, ylabel):
    ax.bar(xs, values, width=0.46, color=colors, zorder=3)
    for i, v in enumerate(values):
        plain(ax, i, v + ylim * 0.025, fmt.format(v), fontsize=13,
              color=colors[i], weight="bold", ha="center", va="bottom")
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_xlim(-0.75, 1.75)
    ax.set_ylim(0, ylim)
    style_axes(ax, ylabel=ylabel, title=title, grid_axis="y")


panel(axes[0], [10.0, 8.0], [C_ORANGE, C_ORANGE], "{:.2f} 元", 13.0,
      "① 股价：跌了两成", "股价（元）")
panel(axes[1], [1.00, 0.50], [C_GREEN, C_RED], "{:.2f} 元", 1.35,
      "② 每股盈利：跌了一半", "每股盈利（元）")
panel(axes[2], [10.0, 16.0], [C_GREEN, C_RED], "{:.0f} 倍", 22.0,
      "③ 市盈率：反而从 10 倍涨到 16 倍", "市盈率（倍）")

plain(axes[2], 0.5, 20.4, "盈利减半，股价只跌两成，\n市盈率就被“动”高了",
      fontsize=11.5, color=C_DARK, ha="center", va="center")

fig.suptitle("“买低市盈率股”这个公式：你以为买便宜了，其实是盈利先跑了",
             fontsize=14, weight="bold", y=0.95)
plain(axes[0], -0.72, -2.35, "简化示意数字（元）：股价 10.00 → 8.00；"
                             "每股盈利 1.00 → 0.50；市盈率 = 股价 除以 每股盈利",
      fontsize=10.5, color=C_GRAY, ha="left", va="center")

save(fig, "w3d4_pe_trap.png")
