"""W12 第 3 章配图二：怎么评估一个资金管理人（概念图）。

原书 p238–p241 的五个审查方向，整理成「该问什么 / 危险信号是什么」两列。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_RED, C_GRAY, C_GREEN,
                             F_BLUE, F_RED)

fig, ax = fig_ax(13.0, 7.8, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5.0, 9.66, "怎么评估一个资金管理人：原书给的五个审查方向",
      fontsize=15.5, weight="bold", color="#222222")
plain(ax, 5.0, 9.12, "顺序就是原书的顺序：先看人，再看业绩（p238–p241）",
      fontsize=11.0, color=C_GRAY)

plain(ax, 4.30, 8.60, "该问什么", fontsize=11.5, color="#555555", weight="bold")
plain(ax, 8.20, 8.60, "危险信号", fontsize=11.5, color="#555555", weight="bold")

rows = [
    ("① 他吃自己煮的食物吗？",
     "他自己的钱和客户的钱\n放在一起管吗？",
     "只卖不买、\n自己不投自己的产品"),
    ("② 他一视同仁吗？",
     "是否公平对待所有客户？\n是否同时执行所有人的交易？",
     "先给自己或大客户\n跑，再轮到小客户"),
    ("③ 他的规模是不是太大了？",
     "管理规模大幅增加后，\n业绩有没有变差？",
     "规模暴涨，\n策略却一点没变"),
    ("④ 他的投资哲学是什么？",
     "担心绝对回报，还是\n被相对表现竞赛牵着走？",
     "时时刻刻满仓、\n只跟指数比高低"),
    ("⑤ 他的历史业绩怎么看？",
     "跨过几轮周期了吗？是同一个人\n做的吗？靠体系还是靠一两次运气？",
     "只拿最近两年\n最好看的那一段"),
]

h = 1.22
gap = 0.34
y_top = 8.30

for i, (q, ask, flag) in enumerate(rows):
    y = y_top - i * (h + gap) - h
    box(ax, 0.22, y, 3.95, h, q, fc="#ffffff", ec=C_BLUE, fontsize=11.9,
        tc=C_BLUE, weight="bold")
    box(ax, 4.55, y, 3.30, h, ask, fc=F_BLUE, ec=C_BLUE, fontsize=10.9,
        tc="#222222")
    box(ax, 8.23, y, 1.55, h, flag, fc=F_RED, ec=C_RED, fontsize=10.2,
        tc="#a02020")

plain(ax, 5.0, 0.34,
      "最后一条是原书专门强调的：你和这名管理人合得来吗？合不来，关系就长不了。",
      fontsize=11.6, color="#444444")

save(fig, "w12d3_manager_five.png")
