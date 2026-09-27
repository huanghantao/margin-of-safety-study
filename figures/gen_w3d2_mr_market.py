"""W3 第 2 章图一：市场先生每天的报价 vs 你估算的内在价值（真实坐标）。

报价在"沮丧价"和"狂热价"之间来回摆动，内在价值只是慢慢变化的一条窄带。
"""

import sys, pathlib

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, label, plain, style_axes,
                             C_GREEN, C_ORANGE, C_RED, C_GRAY, C_DARK, C_BLUE)

fig, ax = plt.subplots(figsize=(11.5, 6.8))

days = list(range(1, 31))
quotes = [105, 98, 88, 76, 65, 58, 62, 74, 85, 96,
          110, 125, 140, 152, 168, 175, 160, 138, 120, 104,
          92, 80, 70, 64, 72, 88, 102, 115, 130, 142]

# 内在价值窄带（你估算的价值：大约 100 元，允许上下浮动一点）
ax.axhspan(95, 105, color=C_GREEN, alpha=0.16, zorder=1)
ax.axhline(100, color=C_GREEN, lw=1.8, ls="--", zorder=2)

ax.plot(days, quotes, color=C_ORANGE, lw=2.6, marker="o", ms=4.5, zorder=4)

# 关键点：沮丧价 / 狂热价
ax.plot([6], [58], marker="o", ms=13, mfc="none", mec=C_GREEN, mew=2.6, zorder=5)
ax.plot([16], [175], marker="o", ms=13, mfc="none", mec=C_RED, mew=2.6, zorder=5)
ax.plot([24], [64], marker="o", ms=13, mfc="none", mec=C_GREEN, mew=2.6, zorder=5)

label(ax, 0.4, 18, "第 6 天他吓坏了：58 元就肯卖\n（你的估值是 100 元 → 可以买）",
      color=C_GREEN, fontsize=11.5, ha="left", va="center", weight="bold")
label(ax, 18.6, 207, "第 16 天他发疯了：175 元才肯买\n（你的估值是 100 元 → 可以卖，也可以不理）",
      color=C_RED, fontsize=11.5, ha="center", va="center", weight="bold")
label(ax, 24.6, 22, "第 24 天他又沮丧了：64 元\n（同一家公司，什么都没变）",
      color=C_GREEN, fontsize=11.5, ha="left", va="center", weight="bold")
label(ax, 14.2, 42, "第 9～11 天报价和你的估值差不多：\n既不想买也不想卖，合上报纸去干别的",
      color=C_GRAY, fontsize=11, ha="center", va="center")
plain(ax, 0.35, 113, "你估的内在价值：大约 100 元", color=C_GREEN, fontsize=11.5,
      ha="left", va="bottom", weight="bold")

ax.set_xlim(0, 31.2)
ax.set_ylim(0, 235)
style_axes(ax, xlabel="交易日（第几天）", ylabel="市场先生报出的每股价格（元）",
           title="市场先生的报价：在沮丧价与狂热价之间来回摆",
           grid_axis="y")
ax.legend(handles=[plt.Line2D([], [], color=C_ORANGE, lw=2.6, marker="o", ms=5,
                              label="市场先生每天的报价"),
                   Patch(facecolor=C_GREEN, alpha=0.16, edgecolor=C_GREEN,
                         label="你估的内在价值区间（95～105 元）")],
          loc="upper left", fontsize=11, frameon=True)
plain(ax, 31.0, -26, "数字为简化示意，用于教学", fontsize=10, color=C_GRAY,
      ha="right", va="center")

save(fig, "w3d2_mr_market.png")
