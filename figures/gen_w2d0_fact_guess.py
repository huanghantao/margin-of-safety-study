"""Week 2 第 0 章配图：事实 vs 猜测。

左边一栏是"已经发生、可以翻年报查证"的事实，
右边一栏是"还没发生、只能估计"的猜测。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, label, plain, vline,
                             C_BLUE, C_GREEN, C_ORANGE, C_GRAY,
                             F_BLUE, F_GREEN, F_ORANGE)

fig, ax = fig_ax(11, 6.5)

plain(ax, 5, 9.65, "同一家公司：哪些是事实，哪些是猜测", fontsize=15,
      weight="bold", color="#222222")

box(ax, 0.3, 8.5, 4.4, 0.8, "事实 · 已经发生，能翻年报查证", fc=F_GREEN,
    ec=C_GREEN, fontsize=12, weight="bold", tc=C_GREEN)
box(ax, 5.3, 8.5, 4.4, 0.8, "猜测 · 还没发生，只能估计", fc=F_ORANGE,
    ec=C_ORANGE, fontsize=12, weight="bold", tc=C_ORANGE)

left = [
    "账上有多少现金\n（年报「货币资金」一栏）",
    "去年一年赚了多少\n（年报「净利润」）",
    "欠了银行多少钱\n（年报「有息负债」）",
    "去年分给股东多少\n（年报「分红方案」）",
]
right = [
    "明年能赚多少\n（看竞争、看需求）",
    "五年后还在不在\n（看行业会不会被替代）",
    "管理层把钱花在哪\n（看人的决定）",
    "别人愿意出什么价\n（看市场情绪）",
]

ys = [7.5, 5.9, 4.3, 2.7]
for y, t in zip(ys, left):
    box(ax, 0.3, y, 4.4, 1.0, t, fc=F_BLUE, ec=C_BLUE, fontsize=11)
for y, t in zip(ys, right):
    box(ax, 5.3, y, 4.4, 1.0, t, fc="#fafafa", ec=C_GRAY, fontsize=11)

vline(ax, 5.0, 2.4, 9.4, color="#cccccc", lw=1.2, ls=(0, (4, 4)))

label(ax, 5, 1.4,
      "事实告诉你「它现在是什么」；猜测才决定「它值多少钱」"
      "——这就是估值天生不精确的原因",
      fontsize=12, color="#222222")

save(fig, "w2d0_fact_guess.png")
