"""Week 7 第 3 章配图：巴菲特的大桥承重比喻。

桥的设计承重 3 万磅，实际只放行 1 万磅的卡车 —— 余量 2 万磅就是安全边际。
换成 3.5 万磅的卡车（相当于出价高于价值），桥就塌了。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, arrow, vline,
                             C_BLUE, C_GREEN, C_RED, C_GOLD)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(11.6, 6.2))

names = ["如果来一辆 3.5 万磅的卡车", "实际放行的卡车：1 万磅",
         "桥的设计承重：3 万磅"]
vals = [35000, 10000, 30000]
colors = [C_RED, C_BLUE, C_GREEN]
bars = ax.barh(names, vals, height=0.46, color=colors, zorder=3)

for b, v in zip(bars, vals):
    txt = f"{v // 10000} 万磅" if v % 10000 == 0 else "3.5 万磅"
    label(ax, v + 900, b.get_y() + b.get_height() / 2, txt,
          fontsize=12.5, color="#222222", ha="left", weight="bold")

vline(ax, 30000, -0.55, 2.6, color=C_GREEN, lw=1.6, ls="--", zorder=2)
plain(ax, 30000, 2.72, "承重上限 3 万磅", fontsize=11.5, color=C_GREEN, ha="center")

arrow(ax, (10500, 1.0), (29500, 1.0), color=C_GREEN, lw=2.2, style="<|-|>",
      zorder=4)
label(ax, 19500, 1.42, "安全边际：还有 2 万磅余量（3 倍）", fontsize=12,
      color=C_GREEN, weight="bold")
label(ax, 41500, 0.0, "超载：桥塌", fontsize=12, color=C_RED, ha="left",
      weight="bold")

ax.set_xlim(0, 53000)
ax.set_ylim(-0.75, 3.05)
ax.set_xticks([0, 10000, 20000, 30000, 40000, 50000])
ax.set_xticklabels(["0", "1 万", "2 万", "3 万", "4 万", "5 万"])
style_axes(ax, xlabel="重量（磅）",
           title="巴菲特的大桥比喻：坚信能承重 3 万磅，只让 1 万磅的卡车上桥",
           grid_axis="x")

fig.tight_layout(pad=1.6)
save(fig, "w7d3_bridge_load.png")
