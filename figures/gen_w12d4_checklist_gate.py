"""W12 第 4 章配图二：买入前的五道闸门（概念图）。

一只候选股票从上面进来，依次过五道闸门（对应结业清单的五组）；
任何一道过不去，就从右边出去——不买，或者回去把这一项搞清楚。
五道全过，才允许下单（并且分批买）。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain, arrow,
                             C_BLUE, C_GREEN, C_ORANGE, C_RED, C_GRAY,
                             F_BLUE, F_GREEN, F_RED)

fig, ax = fig_ax(12.0, 8.4, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5.0, 9.76, "买入前的五道闸门：任何一道过不去，就不买",
      fontsize=15.5, weight="bold", color="#222222")

box(ax, 3.00, 8.62, 4.00, 0.78, "一只候选股票（你已经研究过了）",
    fc="#ffffff", ec=C_GRAY, fontsize=11.8, tc="#222222", weight="bold")
arrow(ax, (5.0, 8.62), (5.0, 8.35), color=C_GRAY, lw=1.8)

gates = [
    ("① 我懂这家公司吗？（4 条）", C_BLUE, F_BLUE),
    ("② 它值多少钱？（5 条）", C_GREEN, F_GREEN),
    ("③ 我付的价格够便宜吗？（5 条）", C_ORANGE, "#fdf1e3"),
    ("④ 我为什么是现在买？（4 条）", C_RED, F_RED),
    ("⑤ 什么情况下我会卖？（5 条）", C_GRAY, "#f2f2f2"),
]

h = 1.08
gap = 0.33
step = h + gap
y_top = 8.35

for i, (txt, ec, fc) in enumerate(gates):
    y = y_top - i * step - h
    box(ax, 3.00, y, 4.00, h, txt, fc=fc, ec=ec, fontsize=11.9,
        tc="#222222", weight="bold")
    arrow(ax, (7.05, y + h / 2), (7.35, y + h / 2), color=C_RED, lw=1.6)

y_last = y_top - 4 * step - h
box(ax, 7.40, y_last, 2.40, 4 * step + h, "任何一道\n过不去\n\n不买，或者\n回去把这一项\n搞清楚",
    fc=F_RED, ec=C_RED, fontsize=12.0, tc="#a02020", weight="bold")

arrow(ax, (5.0, y_last), (5.0, y_last - 0.34), color=C_GREEN, lw=2.0)
box(ax, 3.00, y_last - 1.28, 4.00, 0.94,
    "五道全过 → 才允许下单\n（并且按第 2 章的分批买入执行）",
    fc="#eaf6ec", ec=C_GREEN, fontsize=11.6, tc="#1a6b1f", weight="bold")

save(fig, "w12d4_checklist_gate.png")
