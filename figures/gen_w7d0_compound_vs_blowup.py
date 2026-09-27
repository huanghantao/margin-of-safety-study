"""Week 7 第 0 章配图：复利 vs 一次大亏 / 亏损与回本的不对称。

左图：甲每年 +16% 连续 10 年，乙 9 年 +20% 但第 10 年 -15% —— 结果几乎打平。
右图：亏 10% / 30% / 50% / 70% 之后，回本分别需要涨多少。
数字取自《安全边际》原书 p96 的复利表，其余为可直接手算的算术结果。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, plain, label,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GOLD, C_DARK)

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["axes.unicode_minus"] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 6.0))

# ── 左图：两条路，十年后几乎打平 ────────────────────────────────────
names = ["甲：每年 +16%\n连续 10 年", "乙：9 年每年 +20%\n第 10 年 -15%"]
vals = [4411, 4386]
colors = [C_BLUE, C_ORANGE]
bars = ax1.bar(names, vals, color=colors, width=0.5, zorder=3)
for b, v in zip(bars, vals):
    plain(ax1, b.get_x() + b.get_width() / 2, v + 130, f"{v} 元",
          fontsize=13, weight="bold", color=C_DARK, va="bottom")
ax1.set_ylim(0, 5800)
style_axes(ax1, ylabel="十年后的账户金额（元）",
           title="起点都是 1000 元：稳与猛，十年后几乎打平")
label(ax1, 0.5, 5250, "差距不到 1%，但甲每年都睡得着觉", fontsize=12,
      color=C_BLUE, weight="bold")

# ── 右图：亏损与回本的不对称 ────────────────────────────────────────
loss = ["亏 10%", "亏 30%", "亏 50%", "亏 70%"]
need = [11.1, 42.9, 100.0, 233.3]
bars2 = ax2.bar(loss, need, color=[C_GREEN, C_GOLD, C_ORANGE, C_RED],
                width=0.55, zorder=3)
for b, v in zip(bars2, need):
    plain(ax2, b.get_x() + b.get_width() / 2, v + 7, f"{v}%",
          fontsize=13, weight="bold", color=C_DARK, va="bottom")
ax2.set_ylim(0, 290)
style_axes(ax2, ylabel="把本金赚回来所需的涨幅（%）",
           title="跌下去容易，爬回来难：回本需要的涨幅")
label(ax2, 1.5, 255, "亏一半，要翻倍才回本", fontsize=12,
      color=C_RED, weight="bold")

fig.tight_layout(pad=2.2)
save(fig, "w7d0_compound_vs_blowup.png")
