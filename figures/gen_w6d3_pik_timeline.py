"""Week 6 第 3 章配图：零息债 / PIK 债是怎么把痛苦推到未来的。

算术（面值 100 元、年息 10%，利息不付现金而是继续滚进欠条）：
    第 1 年末 100 x 1.1 = 110
    第 2 年末 110 x 1.1 = 121
    第 3 年末 121 x 1.1 = 133.1
    第 4 年末 133.1 x 1.1 = 146.4
    第 5 年末 146.4 x 1.1 = 161.1（到期一次性还 161.1 元）

上图：每年真正要掏出去的现金。普通付息债每年 10 元、第 5 年再还本金 100 元；
      零息债前四年一分钱不掏，第 5 年一次性掏 161.1 元。
下图：欠条上写着的金额。普通付息债一直是 100 元；零息债 100 -> 161.1。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED)

import matplotlib.pyplot as plt


def main():
    years = [1, 2, 3, 4, 5]
    cash_coupon = [10, 10, 10, 10, 110]      # 第 5 年：10 元利息 + 100 元本金
    cash_zero = [0, 0, 0, 0, 161.1]          # 第 5 年：本金和滚出来的利息一起还

    fig, axes = plt.subplots(2, 1, figsize=(10.5, 9.0), sharex=True)

    # ── 上图：现金流出 ──────────────────────────────────────────────
    ax1 = axes[0]
    w, gap = 0.34, 0.06
    ax1.bar([y - w - gap / 2 for y in years], cash_coupon, width=w,
            color=C_BLUE, label="每年付息的普通债（年息 10 元）", zorder=3)
    ax1.bar([y + gap / 2 for y in years], cash_zero, width=w,
            color=C_RED, label="零息债 / PIK 债（利息不付现金）", zorder=3)

    for y, v in zip(years, cash_coupon):
        if y == 5:
            # 第 5 年红柱紧挨着蓝柱，数值写在蓝柱左侧外面，避免被红柱压住
            ax1.annotate(f"{v}", xy=(y - w - gap / 2 - 0.04, v),
                         xytext=(0, 5), textcoords="offset points",
                         ha="right", va="bottom", fontsize=9.5, color=C_BLUE,
                         weight="bold", zorder=6)
        else:
            ax1.annotate(f"{v}", xy=(y - w - gap / 2 + w / 2, v),
                         xytext=(0, 5), textcoords="offset points",
                         ha="center", va="bottom", fontsize=9.5, color=C_BLUE,
                         weight="bold", zorder=6)
    for y, v in zip(years, cash_zero):
        ax1.annotate(f"{v:g}", xy=(y + gap / 2 + w / 2, v),
                     xytext=(0, 5), textcoords="offset points", ha="center",
                     va="bottom", fontsize=9.5, color=C_RED, weight="bold",
                     zorder=6)

    ax1.set_ylim(0, 205)
    ax1.set_xlim(0.45, 5.55)
    style_axes(ax1, ylabel="当年要掏出去的现金（元）",
               title="上图：零息债前四年一分钱现金都不用付，痛苦全部堆到最后一年")
    ax1.legend(fontsize=10.5, loc="upper left", framealpha=0.95)
    label(ax1, 2.5, 90, "前四年：现金支出是 0，\n账面看起来毫无压力",
          color=C_RED, fontsize=10.5, ha="center", va="center")
    label(ax1, 4.35, 150, "第 5 年一次性掏 161.1 元",
          color=C_RED, fontsize=10.5, ha="right", va="center")

    # ── 下图：欠条上的金额 ─────────────────────────────────────────
    ax2 = axes[1]
    ax2.plot(years, [100, 100, 100, 100, 100], marker="o", ms=6, lw=2.4,
             color=C_BLUE, label="普通付息债：欠条一直是 100 元", zorder=3)
    ax2.plot(years, [110, 121, 133.1, 146.4, 161.1], marker="s", ms=6, lw=2.4,
             color=C_RED, label="零息债：欠条自己会长大", zorder=3)

    for y, v in zip(years, [110, 121, 133.1, 146.4, 161.1]):
        ax2.annotate(f"{v:g}", xy=(y, v), xytext=(0, 9),
                     textcoords="offset points", ha="center", va="bottom",
                     fontsize=10, color=C_RED, weight="bold", zorder=6)

    ax2.set_ylim(85, 200)
    style_axes(ax2, xlabel="第几年", ylabel="欠条上写着的金额（元）",
               title="下图：本金没有变多，欠条上的数字却一直在长大")
    ax2.legend(fontsize=10.5, loc="upper left", framealpha=0.95)
    label(ax2, 3.75, 183, "每年 10% 的利息没有付出去，\n而是变成了新的欠条",
          color=C_GRAY, fontsize=10.5, ha="center", va="center")

    fig.subplots_adjust(hspace=0.38)
    save(fig, "w6d3_pik_timeline.png")


main()
