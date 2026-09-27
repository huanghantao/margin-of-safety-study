"""W5 第 2 章配图：投资组合保险的恶性循环（机制示意图）。

依据原书 p59–p60：跌 3% 就卖股指期货 → 期货卖盘把期货砸到比股票低 10%
→ 套利者买期货、卖股票 → 股价再跌 → 触发更多卖出。1987 年 10 月 19 日。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain,
                             C_RED, C_DARK, F_RED, F_ORANGE, F_GRAY)

fig, ax = fig_ax(12.0, 7.0, xlim=(0, 12), ylim=(0, 9.4))

plain(ax, 6.0, 9.0, "投资组合保险：一个“保本公式”怎么把下跌放大", fontsize=16,
      color=C_DARK, weight="bold")

box(ax, 4.2, 7.0, 3.6, 1.45,
    "股价跌了 3%\n公式触发：卖出股指期货", fc=F_RED, ec=C_RED, fontsize=11)
box(ax, 8.4, 3.9, 3.4, 1.45,
    "卖的人太多\n期货比股票便宜 10%", fc=F_ORANGE, ec=C_RED, fontsize=11)
box(ax, 4.2, 0.8, 3.6, 1.45,
    "套利者买便宜的期货\n同时卖出股票", fc=F_GRAY, ec=C_RED, fontsize=11)
box(ax, 0.2, 3.9, 3.4, 1.45,
    "股价进一步下跌\n触发更多卖出", fc=F_RED, ec=C_RED, fontsize=11)

arrow(ax, (7.85, 7.5), (9.9, 5.45), color=C_RED, lw=2.0,
      connectionstyle="arc3,rad=-0.28")
arrow(ax, (10.1, 3.85), (7.85, 2.1), color=C_RED, lw=2.0,
      connectionstyle="arc3,rad=-0.28")
arrow(ax, (4.15, 1.4), (2.1, 3.85), color=C_RED, lw=2.0,
      connectionstyle="arc3,rad=-0.28")
arrow(ax, (1.9, 5.4), (4.15, 7.15), color=C_RED, lw=2.0,
      connectionstyle="arc3,rad=-0.28")

label(ax, 6.0, 4.62, "越跌越卖\n越卖越跌", color=C_RED, fontsize=13.5,
      weight="bold")
plain(ax, 6.0, 0.35, "据原书 p59–p60 的机制描述绘制；1987 年 10 月 19 日，"
                     "这条链条在几个小时里走完了一整圈",
      fontsize=10.5, color=C_DARK)

save(fig, "w5d2_insurance_loop.png")
