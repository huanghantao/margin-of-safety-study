"""Week 6 第 0 章配图：堕落天使 vs 新发行垃圾债 —— 买入价站在那里，
决定了你还有多少下跌空间、多少上涨空间（原书 p70）。

每一组两根柱，纵轴是"每 100 元面值债券对应的钱（元）"，用真实比例：
  堕落天使：买入价 60 元，违约后拿回约 30 元 —— 跌掉 30 元
  新发行债：买入价 100 元（贴着面值），违约后同样拿回约 30 元 —— 跌掉 70 元
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED)

import matplotlib.pyplot as plt


def main():
    fig, ax = fig_ax(10.8, 7.4, xlim=(0, 10), ylim=(-3.4, 10.8))
    S = 1 / 12.0                       # 12 元 = 1 个坐标单位，比例保持真实

    # 面值参考线（100 元）
    hline(ax, 100 * S, 0.35, 9.75, color=C_GRAY, lw=1.3, ls="--", zorder=5)
    label(ax, 0.40, 100 * S + 0.28, "面值（印在债券上的价格）100 元",
          color=C_GRAY, fontsize=10.5, ha="left", va="bottom")

    # 左组：堕落天使
    plain(ax, 2.45, 10.25, "堕落天使债券", fontsize=13.5, weight="bold",
          color=C_BLUE)
    plain(ax, 2.45, 9.70, "价格大幅低于面值", fontsize=11, color=C_GRAY)
    bar_pair(ax, 2.45, 0, 60, 30, width=0.85, gap=0.18,
             color_a=C_GOLD, color_b=C_RED,
             label_a="买入价", label_b="违约后大约拿回",
             scale=S, text_fmt="{:.0f} 元", fontsize=11)
    plain(ax, 2.45, -1.35, "买入价只有面值的六成", fontsize=11, color=C_GOLD)
    plain(ax, 2.45, -2.15, "跌掉 30 元；涨回面值还有 40 元空间",
          fontsize=11, color=C_GREEN)

    # 右组：新发行垃圾债
    plain(ax, 7.25, 10.25, "新发行垃圾债", fontsize=13.5, weight="bold",
          color=C_BLUE)
    plain(ax, 7.25, 9.70, "贴着面值发行", fontsize=11, color=C_GRAY)
    bar_pair(ax, 7.25, 0, 100, 30, width=0.85, gap=0.18,
             color_a=C_GOLD, color_b=C_RED,
             label_a="买入价", label_b="违约后大约拿回",
             scale=S, text_fmt="{:.0f} 元", fontsize=11)
    plain(ax, 7.25, -1.35, "买入价就是面值，一分钱折扣都没有",
          fontsize=11, color=C_GOLD)
    plain(ax, 7.25, -2.15, "同样跌到 30 元，却跌掉 70 元；涨不上去",
          fontsize=11, color=C_RED)

    # 两组之间的关系说明
    arrow(ax, (3.55, 3.6), (6.15, 3.6), color=C_GRAY, lw=1.6)
    label(ax, 4.85, 3.6, "同样的违约结果", color=C_GRAY, fontsize=11)

    save(fig, "w6d0_two_bonds.png")


main()
