"""W12 第 2 章配图二：卖出决策树（概念图）。

原书 p232–p234 给的卖出依据，整理成「按顺序问的四个问题」，
右边是对应的动作，下面一整条是「这些都不是卖出理由」。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_GREEN, C_ORANGE, C_RED, C_GRAY,
                             F_BLUE, F_GREEN, F_ORANGE, F_RED)

fig, ax = fig_ax(12.6, 8.0, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5.0, 9.68, "卖出决策树：按顺序问自己四个问题",
      fontsize=16, weight="bold", color="#222222")
plain(ax, 5.0, 9.15, "原书 p233：只存在一个有效的卖出规则——所有的投资都应当在合适的价位卖出",
      fontsize=11.0, color=C_GRAY)
plain(ax, 3.35, 8.62, "问自己", fontsize=11.5, color="#555555", weight="bold")
plain(ax, 8.30, 8.62, "如果是，就动手", fontsize=11.5, color="#555555",
      weight="bold")

rows = [
    ("① 价格已经到达你估算的价值了吗？",
     "卖（或分批卖）",
     C_ORANGE, F_ORANGE),
    ("② 你找到明显更好的便宜货了吗？",
     "换股",
     C_BLUE, F_BLUE),
    ("③ 当初买入的理由被推翻了吗？",
     "必须卖",
     C_RED, F_RED),
    ("④ 你现在真的需要这笔钱吗？",
     "只能卖",
     C_GREEN, F_GREEN),
]

h = 1.24
gap = 0.36
y_top = 8.42

for i, (q, act, ec, fc) in enumerate(rows):
    y = y_top - i * (h + gap) - h
    box(ax, 0.30, y, 6.25, h, q, fc=fc, ec=ec, fontsize=12.4,
        tc="#222222", weight="bold")
    box(ax, 6.95, y, 2.75, h, act, fc="#ffffff", ec=ec, fontsize=12.4,
        tc=ec, weight="bold")

y_last = y_top - 3 * (h + gap) - h
box(ax, 0.30, y_last - 1.46, 9.40, 1.20,
    "这些都不是卖出理由：股价跌了  /  触发了止损线  /  别人都在卖\n"
    "已经赚了 20%  /  你受不了浮亏带来的难受",
    fc=F_RED, ec=C_RED, fontsize=12.2, tc="#a02020", weight="bold")

plain(ax, 5.0, 0.42,
      "四个问题问完都是「否」，就什么都不做——不卖也是一种决定。",
      fontsize=11.8, color="#444444")

save(fig, "w12d2_sell_reasons.png")
