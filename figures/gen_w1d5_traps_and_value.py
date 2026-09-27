"""Week 1 第 5 章配图：导言里的两张清单——避开什么、做什么。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.2, xlim=(0, 10), ylim=(0, 10.2))

plain(ax, 5, 9.75, "导言里的两张清单：他让你避开什么、又让你做什么",
      fontsize=15, weight="bold")

box(ax, 0.25, 8.20, 4.50, 1.10, "投资者容易掉进去的陷阱",
    fc=F_RED, ec=C_RED, fontsize=13, weight="bold")
box(ax, 5.25, 8.20, 4.50, 1.10, "卡拉曼推荐的做法",
    fc=F_GREEN, ec=C_GREEN, fontsize=13, weight="bold")

left = ("① 想赚快钱\n"
        "　 成了别人短期疯狂的牺牲品\n"
        "\n"
        "② 用相对业绩评价自己\n"
        "　 只好去追市场流行的那一批\n"
        "\n"
        "③ 贪婪时只看见回报\n"
        "　 恐惧时只看见下跌\n"
        "\n"
        "④ 迷信公式和电脑程序\n"
        "　 以为数学等式能带来成功投资\n"
        "\n"
        "⑤ 只关心能赚多少\n"
        "　 很少关心会亏多少")
box(ax, 0.25, 1.35, 4.50, 6.55, left, fc=F_RED, ec=C_RED, fontsize=10.5,
    multialignment="left")

right = ("① 先确定内在价值\n"
         "　 再以这个价值的适当折扣买进\n"
         "\n"
         "② 第一目标是保证资金安全\n"
         "　 而不是赚得最多\n"
         "\n"
         "③ 寻找安全边际\n"
         "　 为估错、坏运气、逻辑错误留缓冲\n"
         "\n"
         "④ 自下而上，从公司本身出发\n"
         "　 不去预测大盘的方向\n"
         "\n"
         "⑤ 把下跌看成机会\n"
         "　 下跌的市场才是价值投资者的黄金时间")
box(ax, 5.25, 1.35, 4.50, 6.55, right, fc=F_GREEN, ec=C_GREEN, fontsize=10.5,
    multialignment="left")

plain(ax, 5, 0.60,
      "卡拉曼：价值投资就是先确定内在价值，然后以这个价值的适当折扣买进。（导言 p8）",
      fontsize=10.5, color="#444444")

save(fig, "w1d5_traps_and_value.png")
