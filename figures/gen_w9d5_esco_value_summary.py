"""Week 9 第 5 章配图二（Esco 案例）★：估值汇总图。

同一家公司、同一份公开资料，四种方法给出四段区间，
左下角那条橙色虚线是 1990 年 10 月的真实股价：3 美元。

所有数字都来自原书 p154–p157：
  净现值法（业绩无改善）      4.70 ~ 5.87 美元/股
  净现值法（现金流逐步改善） 10.83 ~ 14.76 美元/股
  私有市场价值法（照 Hazeltine 收购价）  约 15 美元/股
  逐步清算价值法（不低于纯营运资金净额） 至少 15 美元/股
  股市价值法（同行市净率 60%~100%）      15 ~ 25 美元/股
  参照点：有形资产账面价值               25 美元/股
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label, arrow, vline,
                             C_BLUE, C_GREEN, C_GOLD, C_ORANGE, C_GRAY,
                             style_axes)

rows = [
    ("现值分析法\n业绩无改善 12%~15%", 4.70, 5.87, C_BLUE, "4.70 ~ 5.87"),
    ("现值分析法\n现金流逐步改善", 10.83, 14.76, C_BLUE, "10.83 ~ 14.76"),
    ("私有市场价值法\n照 Hazeltine 的收购价", 14.6, 15.4, C_GOLD, "约 15"),
    ("逐步清算价值法\n不低于纯营运资金净额", 15.0, 19.0, C_GREEN,
     "至少 15（上不封顶）"),
    ("股市价值法\n同行市净率 60%~100%", 15.0, 25.0, C_GOLD, "15 ~ 25"),
    ("参照点\n有形资产账面价值", 24.6, 25.4, C_GRAY, "25"),
]

fig, ax = plt.subplots(figsize=(13, 6.6))

for i, (name, lo, hi, c, txt) in enumerate(rows):
    y = len(rows) - 1 - i
    ax.add_patch(plt.Rectangle((lo, y - 0.26), hi - lo, 0.52, fc=c, ec=c,
                               lw=1.4, zorder=3, alpha=0.88))
    lx = 22.9 if name.startswith("逐步清算") else hi + 0.6
    plain(ax, lx, y, txt + " 美元", fontsize=11, weight="bold",
          color="#222222", va="center", ha="left")

# 「至少 15」那一行，右端加一个箭头，表示上不封顶
arrow(ax, (19.4, 2), (22.3, 2), color=C_GREEN, lw=2.2, style="-|>", zorder=4)

# 真实股价：1990 年 10 月的 3 美元
vline(ax, 3, -0.7, 5.75, color=C_ORANGE, lw=2.6, ls="--", zorder=2)
label(ax, 3.5, 5.62, "1990 年 10 月的真实股价：3 美元", fontsize=12,
      color=C_ORANGE, ha="left", weight="bold")

label(ax, 14.2, 5.62,
      "四种方法算出来没有一个是 3 美元；\n"
      "最保守的那一端（4.70）也比股价高 57%。",
      fontsize=11.5, color=C_GREEN, ha="left")

ax.set_xlim(-0.6, 34)
ax.set_ylim(-0.85, 6.05)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in reversed(rows)], fontsize=10.5)
plt.setp(ax.get_yticklabels(), va="center")
ax.set_xticks([0, 5, 10, 15, 20, 25, 30])

style_axes(ax, xlabel="每股值多少美元（数字全部来自原书 p154–p157）",
           title="Esco 电子公司估值汇总：四种方法算出的价值区间，都远高于 3 美元的股价",
           grid_axis="x")

save(fig, "w9d5_esco_value_summary.png")
