"""Week 9 第 4 章配图：价格与价值之间的反射关系。

原书 p150–p151 讲的两件事：股价不只是被动反映企业价值，
它还能反过来改变企业价值。左右两个四步闭环就是这两种方向。
坐标全部手工摆好，箭头两端各留空隙。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_ax, box, arrow, plain, label,
                             C_GREEN, C_RED,
                             F_GREEN, F_RED)

fig, ax = fig_ax(14, 7.0, xlim=(0, 19.6), ylim=(0, 10))

# ── 左：恶性循环 ─────────────────────────────────────────────────
plain(ax, 4.1, 9.3, "恶性循环：股价跌，公司真的会垮", fontsize=12.5,
      color=C_RED, weight="bold")
box(ax, 0.9, 6.6, 3.6, 1.5, "股价跌到只有\n几美元", fc=F_RED, ec=C_RED,
    fontsize=11.5)
box(ax, 5.9, 6.6, 3.7, 1.5, "想增发股票融资\n没人肯买", fc=F_RED, ec=C_RED,
    fontsize=11.5)
box(ax, 5.9, 3.1, 3.7, 1.5, "资本补不上\n撑不住了", fc=F_RED, ec=C_RED,
    fontsize=11.5)
box(ax, 0.9, 3.1, 3.6, 1.5, "经营真的垮掉\n（原本只是担心）", fc=F_RED,
    ec=C_RED, fontsize=11.5)

arrow(ax, (4.5, 7.35), (5.9, 7.35), color=C_RED)
arrow(ax, (7.75, 6.6), (7.75, 4.6), color=C_RED)
arrow(ax, (5.9, 3.85), (4.5, 3.85), color=C_RED)
arrow(ax, (2.7, 4.6), (2.7, 6.6), color=C_RED)

# ── 右：良性循环 ─────────────────────────────────────────────────
plain(ax, 13.8, 9.3, "良性循环：股价高，公司真的会变强", fontsize=12.5,
      color=C_GREEN, weight="bold")
box(ax, 10.6, 6.6, 3.6, 1.5, "股价涨到\n几十美元", fc=F_GREEN, ec=C_GREEN,
    fontsize=11.5)
box(ax, 15.4, 6.6, 3.7, 1.5, "增发股票融资\n抢着买", fc=F_GREEN, ec=C_GREEN,
    fontsize=11.5)
box(ax, 15.4, 3.1, 3.7, 1.5, "资本变充足\n敢做业务", fc=F_GREEN, ec=C_GREEN,
    fontsize=11.5)
box(ax, 10.6, 3.1, 3.6, 1.5, "经营真的变好\n（原本只是期待）", fc=F_GREEN,
    ec=C_GREEN, fontsize=11.5)

arrow(ax, (14.2, 7.35), (15.4, 7.35), color=C_GREEN)
arrow(ax, (17.25, 6.6), (17.25, 4.6), color=C_GREEN)
arrow(ax, (15.4, 3.85), (14.2, 3.85), color=C_GREEN)
arrow(ax, (12.4, 4.6), (12.4, 6.6), color=C_GREEN)

# ── 原书例子 ────────────────────────────────────────────────────
label(ax, 4.1, 1.9, "1990 年的抵押和房地产信托公司：\n"
                    "市场不信它，它就真的还不上钱。",
      fontsize=11, color=C_RED)
label(ax, 13.8, 1.9, "1991 年初的花旗银行：\n"
                     "股价几十美元，它就能顺利增发、充实资本。",
      fontsize=11, color=C_GREEN)

plain(ax, 9.8, 0.55,
      "反射关系：价格不只是价值的一面镜子，它还会走进去，把价值改掉。",
      fontsize=11.5, color="#333333")

save(fig, "w9d4_reflexive_loop.png")
