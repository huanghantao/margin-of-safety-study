"""Week 9 第 1 章配图二：远期现金流对今天的价值贡献有多小。

同样每年 100 元、贴现率 10%：
  第 1~5 年   折回今天 379.08 元
  第 6~10 年  折回今天 235.38 元
  第 11~15 年 折回今天 146.15 元
  第 16~20 年 折回今天 90.75 元
四个数字加起来 851.36 元。柱子画的是每一段占总现值的百分比。
这就是「终值占比过大」这个难题的几何形状。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label, hline,
                             C_BLUE, C_GOLD, C_ORANGE, C_GREEN, style_axes)

segs = [("第 1~5 年", 379.08), ("第 6~10 年", 235.38),
        ("第 11~15 年", 146.15), ("第 16~20 年", 90.75)]
total = sum(v for _, v in segs)
pct = [v / total * 100 for _, v in segs]

fig, ax = plt.subplots(figsize=(11.5, 6.6))

colors = [C_GREEN, C_BLUE, C_GOLD, C_ORANGE]
xs = [0, 1, 2, 3]
ax.bar(xs, pct, width=0.5, color=colors, zorder=3)

for x, p in zip(xs, pct):
    plain(ax, x, p + 1.4, f"{p:.1f}%", fontsize=13, weight="bold",
          color="#222222", va="bottom")

ax.set_xlim(-0.65, 3.75)
ax.set_ylim(0, 56)
ax.set_xticks(xs)
ax.set_xticklabels(
    [f"{name}\n折回今天 {v:.2f} 元" for name, v in segs], fontsize=11.5)

label(ax, 2.35, 45, "名义上，每 5 年都是 500 元；\n"
                    "折回今天，最后 5 年只占 10.7%。",
      fontsize=11.5, color=C_ORANGE, ha="left")

label(ax, 1.42, 36, "前 10 年贡献了 72%\n（614.46 除以 851.36）",
      fontsize=11, color=C_GREEN, ha="left")

hline(ax, 0, -0.65, 3.75, color="#333333", lw=1.2, zorder=2)

style_axes(ax, xlabel="这笔钱在第几年到手（每段 5 年）",
           ylabel="占全部现值的百分比（%）",
           title="每年 100 元、贴现率 10%、共 20 年：越远的钱，占的分量越小")

save(fig, "w9d1_far_future_weight.png")
