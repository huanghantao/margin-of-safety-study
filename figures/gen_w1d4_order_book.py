"""Week 1 第 4 章配图之二：五档报价与买卖撮合。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.6, xlim=(0, 10), ylim=(0, 10.4))

plain(ax, 5, 10.00, "报价是怎么来的：买卖双方挂单，交易所撮合",
      fontsize=15, weight="bold")
plain(ax, 3.00, 9.15, "五档报价（示意）", fontsize=12, weight="bold")

LX, LW = 1.05, 3.90          # 报价梯子
H, STEP = 0.62, 0.70
TOP = 7.60

sell = [("卖5", "10.50", "120 手"), ("卖4", "10.40", "260 手"),
        ("卖3", "10.30", "180 手"), ("卖2", "10.20", "90 手"),
        ("卖1", "10.10", "300 手")]
buy = [("买1", "10.00", "450 手"), ("买2", "9.90", "210 手"),
       ("买3", "9.80", "370 手"), ("买4", "9.70", "150 手"),
       ("买5", "9.60", "280 手")]

y = TOP
for tag, px, qty in sell:
    box(ax, LX, y, LW, H, f"{tag}　　{px} 元　　{qty}",
        fc=F_ORANGE, ec=C_ORANGE, fontsize=10.5)
    y -= STEP

box(ax, LX, y, LW, H, "最新成交价　　10.05 元", fc=F_GOLD, ec=C_GOLD,
    fontsize=10.5, weight="bold")
y -= STEP

for tag, px, qty in buy:
    box(ax, LX, y, LW, H, f"{tag}　　{px} 元　　{qty}",
        fc=F_BLUE, ec=C_BLUE, fontsize=10.5)
    y -= STEP

# ── 右侧说明面板 ────────────────────────────────────────────────────
panel = ("报价不是谁规定的，\n"
         "是买卖双方一张一张挂出来的。\n"
         "\n"
         "想卖的人把价格挂在上面，\n"
         "想买的人把价格挂在下面。\n"
         "\n"
         "卖1 = 最低的卖价 10.10 元\n"
         "买1 = 最高的买价 10.00 元\n"
         "两边差 0.10 元 → 此刻不成交\n"
         "\n"
         "上面的「最新成交价 10.05 元」\n"
         "是上一笔成交留下的记录。\n"
         "\n"
         "一旦有人愿意按 10.10 元买，\n"
         "马上就成交，最新价也变成 10.10 元。\n"
         "这就是「价格」的由来。")
box(ax, 5.55, 1.30, 4.20, 6.30, panel, fc="#fbfbfb", ec=C_GRAY, fontsize=10.5)

# ── 左侧：卖1 与买1 的价差 ──────────────────────────────────────────
label(ax, 0.62, 6.05, "卖1\n与\n买1\n相差\n0.10 元", fontsize=9.5, color=C_GRAY)
arrow(ax, (0.62, 5.25), (0.62, 3.70), color=C_GRAY, lw=1.4)

save(fig, "w1d4_order_book.png")
