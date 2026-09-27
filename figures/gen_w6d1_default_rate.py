"""Week 6 第 1 章配图：违约率为什么被算小了 —— 分子与分母（原书 p71）。

上图：分母（市场上尚未到期的垃圾债总量）涨得飞快，分子（当年真正违约的
      债券）涨得很慢。下图：两者相除得到的"违约率"看起来一直在下降，
      直到 1990 年新发行停止、分母不再变大，违约才集中暴露出来。

⚠️ 本图是**示意图**：两条线的取值只用来表示原书描述的变化方向和节奏，
   不是历史统计数据。纵轴因此只标"相对规模（示意）"，不给具体数值。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED)

import matplotlib.pyplot as plt


def main():
    years = [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991]
    denom = [100, 150, 220, 300, 400, 520, 650, 780, 800, 800]
    numer = [3, 4, 6, 8, 10, 13, 17, 22, 55, 70]
    ratio = [round(n / d * 100, 1) for n, d in zip(numer, denom)]

    fig, axes = plt.subplots(2, 1, figsize=(10.5, 8.6), sharex=True)

    ax1 = axes[0]
    ax1.plot(years, denom, marker="o", ms=6, lw=2.4, color=C_BLUE,
             label="分母：市场上还没到期的垃圾债总量", zorder=3)
    ax1.plot(years, numer, marker="s", ms=6, lw=2.4, color=C_RED,
             label="分子：这一年真正违约的债券", zorder=3)
    ax1.set_ylim(0, 1150)
    ax1.set_xlim(1981.4, 1992.8)
    style_axes(ax1, ylabel="相对规模（示意）",
               title="分子长得慢，分母长得快")
    ax1.legend(fontsize=10.5, loc="upper left", framealpha=0.95)

    label(ax1, 1988.5, 950,
          "每年都有大量新债发出来，\n分母越堆越高", color=C_BLUE,
          fontsize=10.5, ha="center")
    label(ax1, 1989.5, 230,
          "1990 年：新发行停了，\n分母不再变大，\n违约集中暴露",
          color=C_RED, fontsize=10.5, ha="center")
    arrow(ax1, (1989.6, 150), (1990.2, 62), color=C_RED, lw=1.6)

    ax2 = axes[1]
    ax2.plot(years, ratio, marker="o", ms=6, lw=2.4, color=C_ORANGE, zorder=3)
    ax2.set_ylim(0, 11)
    style_axes(ax2, xlabel="年份", ylabel="违约率（%，示意）",
               title="相除之后的违约率：先越来越低，然后跳起来")
    ax2.annotate("约 3%", xy=(1982, 3.0), xytext=(0, 10),
                 textcoords="offset points", ha="center", va="bottom",
                 fontsize=10.5, color=C_ORANGE, weight="bold", zorder=6)
    ax2.annotate("约 2.5%", xy=(1986.7, 2.5), xytext=(0, 10),
                 textcoords="offset points", ha="center", va="bottom",
                 fontsize=10.5, color=C_ORANGE, weight="bold", zorder=6)
    ax2.annotate("约 8.8%", xy=(1991, 8.8), xytext=(0, 10),
                 textcoords="offset points", ha="center", va="bottom",
                 fontsize=10.5, color=C_RED, weight="bold", zorder=6)
    label(ax2, 1984.4, 6.6,
          "同一批债券，\n换一个时点再看，\n违约率完全不同",
          color=C_GRAY, fontsize=10.5, ha="center")

    fig.text(0.5, 0.015,
             "示意图：只表示原书 p71 描述的两条线的相对走向，不是历史统计数据。",
             ha="center", fontsize=10, color=C_GRAY)
    fig.subplots_adjust(hspace=0.42)

    save(fig, "w6d1_default_rate.png")


main()
