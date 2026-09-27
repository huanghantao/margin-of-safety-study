"""Week 1 第 2 章配图之一：一家公司为什么值钱——四个来源。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.0, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5, 9.55, "一家公司为什么值钱：四个来源", fontsize=15, weight="bold")

# 中心
box(ax, 3.60, 4.25, 2.80, 1.50, "这家奶茶店\n到底值多少钱？",
    fc=F_GOLD, ec=C_GOLD, fontsize=12.5, weight="bold")

# 四个来源
box(ax, 0.25, 6.95, 3.90, 2.10,
    "① 它有什么（资产）\n　设备、装修、押金、\n　账上的现金、租约",
    fc=F_BLUE, ec=C_BLUE, fontsize=11, multialignment="left")
box(ax, 5.85, 6.95, 3.90, 2.10,
    "② 它每年赚多少（盈利）\n　一年卖 6 万杯，\n　扣完成本净赚约 20 万元",
    fc=F_GREEN, ec=C_GREEN, fontsize=11, multialignment="left")
box(ax, 0.25, 1.05, 3.90, 2.10,
    "③ 真金白银进来多少（现金流）\n　客人当场扫码付钱，\n　不是赊账、不是白条",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=11, multialignment="left")
box(ax, 5.85, 1.05, 3.90, 2.10,
    "④ 以后会不会更多（成长）\n　隔壁新盖了写字楼，\n　明年可能多卖三成",
    fc=F_GOLD, ec=C_GOLD, fontsize=11, multialignment="left")

# 四支箭头
arrow(ax, (3.90, 5.75), (2.60, 6.85), color=C_GRAY, lw=1.6)
arrow(ax, (6.10, 5.75), (7.40, 6.85), color=C_GRAY, lw=1.6)
arrow(ax, (3.90, 4.25), (2.60, 3.25), color=C_GRAY, lw=1.6)
arrow(ax, (6.10, 4.25), (7.40, 3.25), color=C_GRAY, lw=1.6)

plain(ax, 5, 0.50,
      "四个来源不是四道独立的题：成长要靠盈利和现金流来证明，盈利最终要变成现金才算数。",
      fontsize=10.5, color="#444444")

save(fig, "w1d2_value_four.png")
