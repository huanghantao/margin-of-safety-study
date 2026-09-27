"""Week 1 第 1 章配图之二：一股 = 公司所有权的一小片。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

import matplotlib.pyplot as plt

fig, ax = fig_ax(11.5, 6.8, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5, 9.60, "一股 = 公司所有权的一小片", fontsize=15, weight="bold")
plain(ax, 3.00, 8.85, "一家公司被切成许多等份，每一份叫「1 股」", fontsize=11)

# ── 左半：把公司画成被切好的格子 ────────────────────────────────────
COLS, ROWS, CELL = 10, 6, 0.5
GX, GY = 0.55, 4.80
HI = (3, 1)                      # 被高亮的那一格（列, 行）

for i in range(COLS):
    for j in range(ROWS):
        if (i, j) == HI:
            fc, ec, lw = C_ORANGE, "#a34a00", 1.6
        else:
            fc, ec, lw = "#e3edf7", "#9dbfdd", 0.9
        ax.add_patch(plt.Rectangle((GX + i * CELL, GY + j * CELL), CELL, CELL,
                                   fc=fc, ec=ec, lw=lw, zorder=3))

label(ax, 2.30, 3.40, "你买到的其中一份", fontsize=11, color="#a34a00")
arrow(ax, (2.30, 3.85), (2.30, GY + (HI[1]) * CELL - 0.15),
      color=C_ORANGE, lw=1.8)

plain(ax, 3.00, 2.70,
      "图上「你的那一份」被画大了：真实持股比例往往连一个小格子都不到",
      fontsize=10, color="#666666")

# ── 右半：把比例和钱算一遍 ──────────────────────────────────────────
panel = ("算一遍你就懂了\n"
         "\n"
         "公司一共发行 1 亿股（示意）\n"
         "你买入 100 股\n"
         "\n"
         "你的持股比例\n"
         "= 100 股 / 1 亿股\n"
         "= 百万分之一\n"
         "\n"
         "每股 10 元\n"
         "你的成本 = 10 元 × 100 股 = 1000 元\n"
         "公司总市值 = 10 元 × 1 亿股 = 10 亿元")
box(ax, 6.15, 2.60, 3.60, 5.40, panel, fc=F_BLUE, ec=C_BLUE, fontsize=10.5)

save(fig, "w1d1_share_split.png")
