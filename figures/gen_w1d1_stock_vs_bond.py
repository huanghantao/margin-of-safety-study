"""Week 1 第 1 章配图之一：债券与股票的差别 + 清算时的受偿顺序。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.6, xlim=(0, 10), ylim=(0, 10.6))

plain(ax, 5, 10.15, "债券和股票：同样是给公司钱，身份完全不同",
      fontsize=15, weight="bold")

# ── 表头 ────────────────────────────────────────────────────────────
box(ax, 0.25, 8.35, 4.5, 1.25, "债券 = 一张借条\n（你是债主）",
    fc=F_BLUE, ec=C_BLUE, fontsize=13, weight="bold")
box(ax, 5.25, 8.35, 4.5, 1.25, "股票 = 公司所有权的一小片\n（你是股东）",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=13, weight="bold")

# ── 两种身份的具体待遇 ──────────────────────────────────────────────
bond = ("你把 10 万元借给这家奶茶店，\n"
        "约定每年利息 5%，3 年后还本。\n"
        "\n"
        "· 每年拿 5000 元利息 —— 固定\n"
        "· 3 年后拿回 10 万元本金\n"
        "· 店里赚 100 万，你仍然只拿 5000 元\n"
        "· 店里亏钱，只要没倒闭，利息照付\n"
        "· 真倒闭了，你排在股东前面拿钱")
box(ax, 0.25, 4.30, 4.5, 3.65, bond, fc=F_BLUE, ec=C_BLUE, fontsize=10.5,
    multialignment="left")

stock = ("你花 10 万元买下这家奶茶店 10% 的股份。\n"
         "\n"
         "· 店里赚 20 万，你分 2 万\n"
         "· 店里亏 20 万，你的股份跟着缩水\n"
         "· 没有「到期还本」这回事\n"
         "· 店里不分红，你就一分钱拿不到\n"
         "· 倒闭清算时，你排在最后\n"
         "· 但生意做大，你那一份也跟着变大")
box(ax, 5.25, 4.30, 4.5, 3.65, stock, fc=F_ORANGE, ec=C_ORANGE, fontsize=10.5,
    multialignment="left")

# ── 清算受偿顺序 ────────────────────────────────────────────────────
plain(ax, 5, 3.62, "公司关门清算时，谁先拿到钱？（从左到右）",
      fontsize=12, weight="bold")

order = ["有担保的债主\n（抵押物变现后\n先还给他们）", "员工工资、社保\n与欠缴税款",
         "普通债主\n（供应商、银行、\n没担保的债券）", "股东\n（排在最后）"]
colors = [(F_GRAY, C_GRAY), (F_GRAY, C_GRAY), (F_BLUE, C_BLUE), (F_RED, C_RED)]
BW, BGAP = 2.15, 0.40
xs = [0.10 + i * (BW + BGAP) for i in range(4)]

for x, t, (fc, ec) in zip(xs, order, colors):
    box(ax, x, 1.50, BW, 1.55, t, fc=fc, ec=ec, fontsize=10.5)
for i in range(3):
    x_right = xs[i] + BW
    arrow(ax, (x_right + 0.02, 2.275), (xs[i + 1] - 0.02, 2.275),
          color=C_GRAY, lw=1.5)

plain(ax, 5, 0.75,
      "前面的人拿完了还有剩，才轮到股东 —— 所以股票的风险天然比债券大",
      fontsize=11, color="#444444")

save(fig, "w1d1_stock_vs_bond.png")
