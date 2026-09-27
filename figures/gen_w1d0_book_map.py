"""Week 1 第 0 章配图：《安全边际》全书结构 与 12 周课程地图。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.8, xlim=(0, 10), ylim=(0, 11.4))

plain(ax, 5, 11.0, "《安全边际》全书结构 与 12 周课程地图",
      fontsize=15.5, weight="bold")

LX, LW = 0.25, 4.4          # 左栏：原书结构
RX, RW = 5.65, 4.1          # 右栏：本课程周次
H = 1.5

rows = [
    (9.10,
     "导言\n（原书 p3–11）", F_GOLD, C_GOLD,
     "Week 1　零基础起步 + 导言\n第 0–5 章：股票、公司、市场与价格", F_GOLD, C_GOLD),
    (7.15,
     "原书没有这一块\n（它默认你已经会看财报）", F_GRAY, C_GRAY,
     "Week 2　估值入门（原创补课）\n资产、利润、现金、市盈率与安全边际", F_GRAY, C_GRAY),
    (5.20,
     "第一部分　多数投资者会在哪里跌倒\n第 1–4 章（原书 p13–92）", F_ORANGE, C_ORANGE,
     "Week 3 – Week 6\n投机者 · 华尔街 · 机构 · 垃圾债", F_ORANGE, C_ORANGE),
    (3.25,
     "第二部分　价值投资哲学\n第 5–8 章（原书 p94–161）", F_GREEN, C_GREEN,
     "Week 7 – Week 9\n投资目标 · 安全边际 · 哲学起源 · 估值", F_GREEN, C_GREEN),
    (1.30,
     "第三部分　价值投资过程\n第 9–14 章（原书 p163–241）", F_BLUE, C_BLUE,
     "Week 10 – Week 12\n研究 · 机会 · 困境证券 · 组合与结业", F_BLUE, C_BLUE),
]

for y0, lt, lf, le, rt, rf, re in rows:
    box(ax, LX, y0, LW, H, lt, fc=lf, ec=le, fontsize=11)
    box(ax, RX, y0, RW, H, rt, fc=rf, ec=re, fontsize=10.5)
    arrow(ax, (LX + LW, y0 + H / 2), (RX, y0 + H / 2), color=C_GRAY, lw=1.4)

plain(ax, 5, 0.55,
      "附录二、附录三、卡拉曼访谈、编后记 —— 放在 Week 12 第 4 章一起读",
      fontsize=11, color="#444444")

save(fig, "w1d0_book_map.png")
