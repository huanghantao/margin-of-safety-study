"""Week 2 第 2 章配图：市盈率 = 股价 除以 每股盈利（可视化）。

20 个「1 元」的方块 = 今天的股价 20 元；金色那一块 = 公司一年帮你赚的 1 元。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, fig_ax, label, plain, brace,
                             C_GOLD, C_BLUE, C_GRAY, F_GOLD)

fig, ax = fig_ax(11, 6.2, xlim=(0, 10.9), ylim=(0, 10))

plain(ax, 5.45, 9.5, "市盈率 = 今天的股价 除以 公司一年帮你赚的钱",
      fontsize=15, weight="bold", color="#222222")

size, gap, x0, y1, y2 = 0.85, 0.15, 0.5, 6.3, 5.2
for i in range(20):
    row, col = divmod(i, 10)
    x = x0 + col * (size + gap)
    y = y1 if row == 0 else y2
    first = (i == 0)
    ax.add_patch(plt.Rectangle((x, y), size, size,
                               fc=F_GOLD if first else "#dce9f5",
                               ec=C_GOLD if first else C_BLUE, lw=1.8 if first else 1.3,
                               zorder=3))
    plain(ax, x + size / 2, y + size / 2, "1元", fontsize=9.5,
          color="#8a6d1f" if first else "#215b8a", weight="bold", zorder=5)

brace(ax, x0, x0 + 10 * (size + gap) - gap, 7.5,
      "今天的股价：20 元（20 个「1 元」）", color=C_BLUE, fontsize=11.5)

# 图例：金色方块代表什么
ax.add_patch(plt.Rectangle((x0, 3.9), 0.42, 0.42, fc=F_GOLD, ec=C_GOLD,
                           lw=1.6, zorder=3))
plain(ax, x0 + 0.6, 4.11, "= 公司一年帮你每股赚到 1 元（每股盈利）",
      fontsize=11.5, ha="left", color="#8a6d1f")

plain(ax, 5.45, 2.9, "市盈率 = 20 除以 1 = 20 倍", fontsize=14,
      weight="bold", color="#222222")
plain(ax, 5.45, 1.75,
      "粗略直觉：如果每年都赚 1 元、并且全部归你，要 20 年才把本金赚回来",
      fontsize=11.5, color=C_GRAY)
plain(ax, 5.45, 1.05, "（这是直觉，不是承诺：公司明年赚多少并不确定）",
      fontsize=11, color=C_GRAY)

save(fig, "w2d2_pe_visual.png")
