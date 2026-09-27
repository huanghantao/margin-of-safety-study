"""Week 11 第 1 章配图之二：发行人对财政困境的三种回应（原书 p206）。

纯概念分支图，坐标是 0~10 的相对位置，没有数值含义。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, plain, label,
                             C_BLUE, C_ORANGE, C_RED, C_GREEN, C_GRAY,
                             F_BLUE, F_ORANGE, F_RED, F_GRAY)

fig, ax = fig_ax(12.6, 8.2, xlim=(0, 10), ylim=(0, 11.0))

plain(ax, 5.0, 10.4, "付不出钱了，管理层只有三条路可走（原书 p206）",
      fontsize=14.5, weight="bold")

box(ax, 3.10, 8.65, 3.80, 1.00,
    "企业付不出利息、也还不上到期的债", fc=F_RED, ec=C_RED, fontsize=12.5)

COL_X = [0.20, 3.45, 6.70]
COL_W = 3.10
TOP = 6.90
BOT = 2.55

for x in COL_X:
    arrow(ax, (5.0, 8.65), (x + COL_W / 2, TOP), color=C_GRAY, lw=1.8)

box(ax, COL_X[0], BOT, COL_W, TOP - BOT, "", fc=F_BLUE, ec=C_BLUE)
plain(ax, COL_X[0] + COL_W / 2, TOP - 0.45, "① 继续还本付息",
      fontsize=12.5, weight="bold", color=C_BLUE)
plain(ax, COL_X[0] + COL_W / 2, TOP - 1.35,
      "削减成本、卖掉资产、\n找外面注入新钱\n\n"
      "好处：不进法院，\n名声和客户都保住\n\n"
      "代价：靠砍库存、拖货款、\n降薪省下来的钱\n"
      "会腐蚀长期价值",
      fontsize=10.5, va="top")

box(ax, COL_X[1], BOT, COL_W, TOP - BOT, "", fc=F_ORANGE, ec=C_ORANGE)
plain(ax, COL_X[1] + COL_W / 2, TOP - 0.45, "② 证券交换",
      fontsize=12.5, weight="bold", color=C_ORANGE)
plain(ax, COL_X[1] + COL_W / 2, TOP - 1.35,
      "用新证券换掉旧证券，\n不进法院的重组\n\n"
      "难点：债券持有人\n没法被强迫签字\n\n"
      "于是出现搭便车：\n"
      "别人让步、我死守，\n我最占便宜",
      fontsize=10.5, va="top")

box(ax, COL_X[2], BOT, COL_W, TOP - BOT, "", fc=F_RED, ec=C_RED)
plain(ax, COL_X[2] + COL_W / 2, TOP - 0.45, "③ 违约 + 申请破产",
      fontsize=12.5, weight="bold", color=C_RED)
plain(ax, COL_X[2] + COL_W / 2, TOP - 1.35,
      "请求法院保护，\n暂停所有追债和支付\n\n"
      "好处：能甩掉合同、\n租约和一部分债务\n\n"
      "代价：名声污点，\n所以往往是\n最后一种选择",
      fontsize=10.5, va="top")

box(ax, 0.60, 0.75, 8.80, 1.35, "", fc=F_GRAY, ec=C_GRAY)
plain(ax, 5.0, 1.42,
      "三条路经常同时走：一边谈判、一边卖资产、一边准备破产申请。",
      fontsize=11.5, weight="bold")
plain(ax, 5.0, 1.02,
      "所以买问题证券之前，三种可能性都要算进价格里。",
      fontsize=11, color="#444444")

save(fig, "w11d1_three_responses.png")
