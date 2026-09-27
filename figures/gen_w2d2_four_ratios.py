"""Week 2 第 2 章配图：四个倍数各自回答什么问题。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_multi, box, plain,
                             C_BLUE, C_GREEN, C_ORANGE, C_GOLD, C_RED,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD)

fig, axes = fig_multi(2, 2, width=12, height=7.4)

cards = [
    (C_BLUE, F_BLUE, "市盈率 P/E", "= 股价 除以 每股盈利",
     "问：按现在的盈利水平，\n几年能赚回本金？",
     "坑：盈利里可能夹着\n一次性的卖楼收益"),
    (C_GREEN, F_GREEN, "市净率 P/B", "= 股价 除以 每股净资产",
     "问：比账本上记的家底\n贵了多少倍？",
     "坑：账本上的机器设备\n可能早就不值那个钱"),
    (C_ORANGE, F_ORANGE, "净资产收益率 ROE", "= 净利润 除以 净资产",
     "问：股东投进去的钱，\n一年赚出几成回报？",
     "坑：靠大量借钱堆出来的\n高 ROE 很脆弱"),
    (C_GOLD, F_GOLD, "股息率", "= 每股分红 除以 股价",
     "问：光靠分红，\n一年能拿回几成？",
     "坑：股价跌出来的高股息率\n往往是陷阱"),
]

for ax, (color, face, name, formula, ask, trap) in zip(axes, cards):
    box(ax, 0.2, 0.4, 9.6, 9.2, "", fc=face, ec=color, lw=1.8)
    plain(ax, 5.0, 8.35, name, fontsize=14, weight="bold", color=color)
    plain(ax, 5.0, 7.0, formula, fontsize=12.5, color="#222222")
    plain(ax, 5.0, 5.15, ask, fontsize=11.5, color="#222222")
    plain(ax, 5.0, 2.5, trap, fontsize=11, color=C_RED)

save(fig, "w2d2_four_ratios.png")
