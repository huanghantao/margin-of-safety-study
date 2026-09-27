"""Week 6 第 0 章配图：垃圾债市场从兴起到崩塌（按原书数字画真实坐标）。

原书 p70：米尔肯出现之前，市场上仅有"几十亿美元"的垃圾债；
原书 p67：垃圾债被发展成一个"2000 亿美元的市场"；
原书 p67、p71：1990 年违约率创下记录、价格大幅下跌，新发行停止。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED)

import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(10.5, 6.4))

    labels = ["米尔肯登场之前\n（示意时点）", "垃圾债的顶峰\n（1980 年代末）"]
    vals = [50, 2000]
    colors = [C_BLUE, C_ORANGE]
    ax.bar([0, 1], vals, width=0.42, color=colors, zorder=3)

    # 柱顶数值
    ax.annotate("约 50 亿美元\n（原书：几十亿美元，p70）", xy=(0, 50),
                xytext=(0, 10), textcoords="offset points",
                ha="center", va="bottom", fontsize=11, color=C_BLUE,
                weight="bold", zorder=6)
    ax.annotate("约 2000 亿美元\n（原书 p67）", xy=(1, 2000),
                xytext=(0, 10), textcoords="offset points",
                ha="center", va="bottom", fontsize=11, color=C_ORANGE,
                weight="bold", zorder=6)

    # 中间的"约 40 倍"标注
    brace(ax, 0, 1, 2320, "约 40 倍", color=C_GRAY, fontsize=11,
          depth=70, text_offset=85)

    # 右侧：1990 年崩塌的说明
    label(ax, 1.62, 1180,
          "1990 年：\n"
          "违约率创下纪录，\n"
          "许多垃圾债价格\n"
          "大幅下跌，\n"
          "新发行停止。\n"
          "（p67、p71）",
          color=C_RED, fontsize=11, ha="left", va="top")
    arrow(ax, (1.60, 1300), (1.28, 1750), color=C_RED, lw=1.8)

    ax.set_xticks([0, 1])
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 2700)
    ax.set_xlim(-0.55, 2.75)
    style_axes(ax, ylabel="垃圾债市场规模（亿美元，约数）",
               title="垃圾债：从几十亿美元膨胀到 2000 亿美元，然后崩塌")

    fig.text(0.5, -0.02,
             "柱高按原书两处数字绘制（几十亿美元 → 2000 亿美元），只画了两个有原书依据的时点，中间过程未逐年绘制。",
             ha="center", fontsize=10, color=C_GRAY)

    save(fig, "w6d0_junk_boom.png")


main()
