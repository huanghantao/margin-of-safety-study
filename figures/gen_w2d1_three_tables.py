"""Week 2 第 1 章配图：三张表，三种问法（奶茶店版）。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, label, plain,
                             C_BLUE, C_GREEN, C_GOLD, C_GRAY,
                             F_BLUE, F_GREEN, F_GOLD)

fig, ax = fig_ax(11, 7)

plain(ax, 5, 9.6, "三张表，三种问法：奶茶店的一年", fontsize=15,
      weight="bold", color="#222222")

rows = [
    (7.0, F_BLUE, C_BLUE,
     "资产负债表 —— 某一天拍的照片\n"
     "问：它有什么、欠什么，剩下真正属于股东的还有多少？\n"
     "奶茶店开业那天：设备 15 万、原料 2 万、现金 3 万（共 20 万），其中银行借了 6 万"),
    (4.5, F_GREEN, C_GREEN,
     "利润表 —— 一段时间的录像\n"
     "问：这一年做了多少生意，扣掉各种成本之后剩下多少？\n"
     "奶茶店全年收入 60 万，扣掉原料、房租、人工和税，净赚 17 万"),
    (2.0, F_GOLD, C_GOLD,
     "现金流量表 —— 银行流水的对账\n"
     "问：账上说的利润，钱真的收到了吗？又花到哪里去了？\n"
     "奶茶店全年经营净进账 20 万，买设备又花掉 8 万，自由现金流 12 万"),
]

for y, fc, ec, text in rows:
    box(ax, 0.3, y, 9.4, 1.9, text, fc=fc, ec=ec, fontsize=11.5)

label(ax, 5, 0.9, "利润是「看法」，现金是「事实」——两个都要看",
      fontsize=12, color="#222222")

save(fig, "w2d1_three_tables.png")
