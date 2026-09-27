"""Week 8 第 5 章配图：同一段下跌，三种人的三种结局。

左：股价路径（10 元 → 跌到 6 元 → 三年后 15 元），真实坐标。
右：每投入 1 元最后变成多少钱（真实坐标柱状图）。
三个人面对的是同一只股票、同一段行情，区别只在于「要不要被迫卖出」和「有没有现金」。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (fig_multi, save, label, plain, style_axes,
                             hline, vline, C_BLUE, C_ORANGE, C_GREEN, C_RED,
                             C_GRAY)

fig, axes = fig_multi(1, 2, width=13.6, height=6.6)
axL, axR = axes

# ── 左图：价格路径 ──────────────────────────────────────────────────
axL.set_axis_on()
months = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
price = [10.0, 9.0, 8.0, 6.9, 6.0, 7.1, 8.3, 9.4, 10.6, 11.8, 12.9,
         14.0, 15.0]
axL.plot(months, price, color=C_ORANGE, lw=2.8, zorder=4)
axL.plot([0, 12, 36], [10.0, 6.0, 15.0], "o", color=C_ORANGE, ms=8,
         zorder=5)

vline(axL, 12, 0, 6.0, color=C_RED, lw=1.4, ls=(0, (4, 4)), zorder=2)
label(axL, 12.6, 1.6, "甲在这里被迫卖出", fontsize=10.5, color=C_RED,
      ha="left")
label(axL, 0.8, 10.6, "买入 10.00 元", fontsize=10.5, color=C_ORANGE,
      ha="left")
label(axL, 21.0, 4.3, "跌到 6.00 元", fontsize=10.5, color=C_ORANGE)
label(axL, 35.2, 15.5, "三年后 15.00 元", fontsize=10.5, color=C_ORANGE,
      ha="right")

axL.set_xlim(-1, 38)
axL.set_ylim(0, 17.4)
axL.set_xticks([0, 6, 12, 18, 24, 30, 36])
style_axes(axL, xlabel="时间（月）", ylabel="股价（元）",
           title="同一只股票：10 元买进，跌到 6 元，三年后 15 元")

# ── 右图：每 1 元投入的结局 ─────────────────────────────────────────
axR.set_axis_on()
names = ["甲\n急用钱，\n6 元被迫卖出", "乙\n满仓不动，\n拿到 15 元",
         "丙\n留了现金，\n6 元又投同样多"]
values = [0.60, 1.50, 2.00]
colors = [C_RED, C_BLUE, C_GREEN]
pcts = ["-40%", "+50%", "+100%"]

axR.bar(range(3), values, width=0.5, color=colors, zorder=3)
for i, (v, c, p) in enumerate(zip(values, colors, pcts)):
    plain(axR, i, v + 0.06, f"{v:.2f} 元（{p}）", fontsize=11.5, color=c,
          weight="bold", ha="center", va="bottom")

hline(axR, 1.0, 0.65, 2.55, color="#444444", lw=1.4, ls=(0, (5, 4)),
      zorder=4)
label(axR, 2.65, 1.12, "本金 1.00 元", fontsize=10.5, color="#444444",
      ha="left")

axR.set_xlim(-0.6, 3.6)
axR.set_ylim(0, 2.4)
axR.set_xticks([0, 1, 2])
axR.set_xticklabels(names, fontsize=10.5)
style_axes(axR, ylabel="每投入 1 元，最后变成多少元",
           title="同样的行情，三个人的结局完全不同")

save(fig, "w8d5_three_investors.png")
