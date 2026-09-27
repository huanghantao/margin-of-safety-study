"""Week 6 第 4 章配图：今天的高收益陷阱，一张可以对照使用的识别清单。

四组线索：看债本身 / 看现金流 / 看会计手法 / 看你自己的位置。
纯概念清单图，每格文字不超过 10 个字，格与格之间留足间距。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             C_PURPLE, F_BLUE, F_GREEN, F_ORANGE, F_GOLD,
                             F_RED, F_GRAY, F_PURPLE)

import matplotlib.pyplot as plt


ROWS = [
    ("看债本身", C_BLUE, F_BLUE,
     ["利率高得离谱", "靠再融资还旧债", "条款藏着安慰剂"]),
    ("看现金流", C_GOLD, F_GOLD,
     ["EBITDA 漂亮\n但现金是负的", "资本开支长期\n低于折旧", "应收账款涨得\n比收入还快"]),
    ("看会计手法", C_PURPLE, F_PURPLE,
     ["商誉占净资产\n比重很高", "一次性计提\n巨额减值", "频繁更换\n审计师"]),
    ("看你自己的位置", C_RED, F_RED,
     ["你排在谁后面", "最坏能拿回多少", "不碰也是操作"]),
]


def main():
    fig, ax = fig_ax(12, 7.6, xlim=(0, 10), ylim=(0, 10))

    plain(ax, 5.0, 9.72, "今天的高收益陷阱：四组线索，十二个问题",
          fontsize=15, weight="bold", color="#222222")

    row_y = [8.0, 6.0, 4.0, 2.0]
    box_h = 1.3
    item_x = [2.55, 5.12, 7.69]
    # 连接线只画在框与框之间的空隙里，绝不横穿方框（否则会压住框里的文字）
    links = [(2.15, 2.55), (4.72, 5.12), (7.29, 7.69)]

    for (name, ec, fc, items), y in zip(ROWS, row_y):
        box(ax, 0.15, y, 2.0, box_h, name, fc=fc, ec=ec, fontsize=12.5,
            tc=ec, weight="bold")
        for x, txt in zip(item_x, items):
            box(ax, x, y, 2.17, box_h, txt, fc="#ffffff", ec=ec,
                fontsize=10.5, tc="#222222", lw=1.3)
        for x0, x1 in links:
            ax.plot([x0, x1], [y + box_h / 2, y + box_h / 2],
                    color=ec, lw=1.1, ls=":", zorder=1)

    label(ax, 5.0, 1.05,
          "一条总原则：凡是「必须一切顺利才能还上钱」的品种，"
          "看不懂就不碰，不碰也是操作。",
          color=C_RED, fontsize=12.5, ha="center", va="center")

    save(fig, "w6d4_trap_checklist.png")


main()
