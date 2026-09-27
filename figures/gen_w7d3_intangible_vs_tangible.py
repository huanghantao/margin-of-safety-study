"""Week 7 第 3 章配图：无形资产 vs 有形资产的安全边际厚度。

一切顺利时，两类公司都被估成 100 元；一旦出问题（口味变了、对手进攻、
生意不赚钱了），有形资产还能清算、转租、卖掉，无形资产几乎归零。
柱子的落差就是安全边际的厚度。全部为简化示意数字。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, arrow,
                             C_BLUE, C_GREEN, C_RED, C_GRAY)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(11.6, 6.4))

groups = ["无形资产重的公司\n（品牌、配方、口碑）", "有形资产重的公司\n（设备、库存、房产）"]
x = [-0.2, 0.2, 0.8, 1.2]
vals = [100, 15, 100, 65]
colors = [C_BLUE, C_RED, C_BLUE, C_GREEN]
bars = ax.bar(x, vals, width=0.34, color=colors, zorder=3)

notes = ["一切顺利：100", "出事后：只剩 15", "一切顺利：100", "出事后：还剩 65"]
for b, v, n in zip(bars, vals, notes):
    plain(ax, b.get_x() + b.get_width() / 2, v + 2.5, n, fontsize=11.5,
          color="#222222", ha="center", va="bottom", weight="bold")

arrow(ax, (-0.62, 16), (-0.62, 99), color=C_RED, lw=2.0, style="<|-|>", zorder=4)
label(ax, -0.62, 57, "跌掉 85%", fontsize=11.5, color=C_RED,
      rotation=90, weight="bold")
arrow(ax, (1.62, 66), (1.62, 99), color=C_GREEN, lw=2.0, style="<|-|>", zorder=4)
label(ax, 1.62, 82, "只跌 35%", fontsize=11.5, color=C_GREEN,
      rotation=90, weight="bold")

label(ax, 0.5, 130, "有形资产在别处还有用（能卖、能租、能清算），\n"
                    "无形资产一旦没人认，安全边际就非常薄",
      fontsize=11.5, color=C_GRAY, ha="center")

ax.set_xlim(-0.85, 1.75)
ax.set_ylim(0, 148)
ax.set_xticks([0, 1])
ax.set_xticklabels(groups, fontsize=11.5)
style_axes(ax, ylabel="这家公司值多少钱（元，简化示意数字）",
           title="出问题的时候还剩多少：这就是安全边际的厚度")

fig.tight_layout(pad=1.6)
save(fig, "w7d3_intangible_vs_tangible.png")
