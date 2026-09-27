"""Week 6 第 2 章配图：X 公司与 Y 公司 —— 同样的 EBITDA，完全不同的价值。

数字**全部照抄原书表 1**（p88–p89，单位：百万美元）：
    X 服务型公司：收入 100，现金费用 80，折旧和摊销 0，EBIT 20，EBITDA 20
    Y 制造型公司：收入 100，现金费用 80，折旧和摊销 20，EBIT 0，EBITDA 20
原书 p89：X 公司利润 2000 万美元，Y 公司利润为零。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED)

import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(11, 6.2))

    names = ["收入", "现金费用", "折旧和摊销", "EBIT\n（营业利润）", "EBITDA"]
    x_vals = [100, 80, 0, 20, 20]
    y_vals = [100, 80, 20, 0, 20]
    pos = list(range(len(names)))
    width, gap = 0.34, 0.06

    ax.bar([p - width - gap / 2 for p in pos], x_vals, width=width,
           color=C_BLUE, label="X 公司（服务型）", zorder=3)
    ax.bar([p + gap / 2 for p in pos], y_vals, width=width,
           color=C_ORANGE, label="Y 公司（制造型）", zorder=3)

    for p, v in zip(pos, x_vals):
        ax.annotate(f"{v}", xy=(p - width - gap / 2 + width / 2, v),
                    xytext=(0, 5), textcoords="offset points",
                    ha="center", va="bottom", fontsize=10, color=C_BLUE,
                    weight="bold", zorder=6)
    for p, v in zip(pos, y_vals):
        ax.annotate(f"{v}", xy=(p + gap / 2 + width / 2, v),
                    xytext=(0, 5), textcoords="offset points",
                    ha="center", va="bottom", fontsize=10, color=C_ORANGE,
                    weight="bold", zorder=6)

    ax.set_xticks(pos)
    ax.set_xticklabels(names, fontsize=11)
    ax.set_ylim(0, 132)
    ax.set_xlim(-0.6, 4.6)
    style_axes(ax, ylabel="百万美元（原书表 1，p88–p89）",
               title="X 公司和 Y 公司 1990 年损益表：EBITDA 一模一样，利润一个 20 一个 0")
    ax.legend(fontsize=10.5, loc="upper right", framealpha=0.95)

    label(ax, 2.5, 62,
          "两家 EBITDA 都是 20，\n买家用同一个倍数出价，\n"
          "但 Y 公司的机器迟早要换，\n钱留不下来",
          color=C_GRAY, fontsize=10.5, ha="center", va="center")

    fig.text(0.5, -0.005,
             "X 公司几乎没有需要更换的重资产，折旧为 0，EBITDA 就是它能自由支配的钱；"
             "Y 公司的 20 是机器的折旧，必须再投回去。",
             ha="center", fontsize=10.5, color=C_GRAY)

    save(fig, "w6d2_xy_company.png")


main()
