"""Week 9 第 1 章配图一：把未来每一年的 100 元，一年一年折回今天。

横轴是「第几年收到这笔钱」，纵轴是它相当于今天的多少钱（贴现率 10%）。
柱子高度就是真实坐标：第 1 年 90.91 元，第 10 年只剩 38.55 元。
左上角的方框写的就是「上一年那个数再除以 1.10」。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label, hline,
                             C_BLUE, C_ORANGE, C_GOLD, style_axes)

fig, ax = plt.subplots(figsize=(12.5, 6.6))

# 1.10 连乘表（逐年往后乘），再用 100 除以它
mult = [1.1]
for _ in range(9):
    mult.append(round(mult[-1] * 1.1, 4))
pv = [round(100 / m, 2) for m in mult]

xs = list(range(1, 11))
ax.bar(xs, pv, width=0.58, color=[C_BLUE] * 5 + [C_GOLD] * 5, zorder=3)

for x, v in zip(xs, pv):
    plain(ax, x, v + 2.2, f"{v:.2f}", fontsize=9.5, color="#333333",
          va="bottom")

ax.set_xlim(0.3, 11.0)
ax.set_ylim(0, 156)
ax.set_xticks(xs)
ax.set_xticklabels([f"第 {i} 年" for i in xs], fontsize=10.5)

hline(ax, 100, 0.3, 11.0, color=C_ORANGE, lw=1.6, ls=(0, (5, 3)), zorder=1)
label(ax, 10.85, 103, "每年名义上都是 100 元", fontsize=11, color=C_ORANGE,
      ha="right")

label(ax, 0.55, 149, "同样的 100 元，越晚到手越不值钱", fontsize=12.5,
      color=C_GOLD, ha="left", weight="bold")
label(ax, 0.55, 126,
      "每往右一年，就再除以一次 1.10：\n"
      "100 除以 1.10 = 90.91\n"
      "90.91 除以 1.10 = 82.64\n"
      "一路除到第 10 年，只剩 38.55",
      fontsize=11, color="#333333", ha="left")

style_axes(ax, xlabel="这笔钱在第几年到手", ylabel="相当于今天的多少钱（元）",
           title="每年收到 100 元，按 10% 一年一年折回今天")

save(fig, "w9d1_discount_timeline.png")
