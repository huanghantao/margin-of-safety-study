"""W3 第 4 章图一："收益猪" 的现金流被拆开看（真实坐标堆叠柱）。

每年固定分到 10 元，其中真利息越来越少、本金返还越来越多。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, style_axes,
                             C_GREEN, C_RED, C_GRAY, C_DARK, F_GREEN, F_RED)

fig, ax = plt.subplots(figsize=(11.5, 6.8))

years = ["第 1 年", "第 2 年", "第 3 年"]
interest = [6.00, 5.76, 5.51]          # 真利息：本金 100 / 96.00 / 91.76 元的 6%
principal = [4.00, 4.24, 4.49]         # 本金返还：分配额 10 元减去真利息
begin_principal = ["本金 100.00 元", "本金 96.00 元", "本金 91.76 元"]
xs = [0, 1, 2]

ax.bar(xs, interest, width=0.46, color=C_GREEN, zorder=3,
       label="真利息（钱生出来的）")
ax.bar(xs, principal, width=0.46, bottom=interest, color=C_RED, zorder=3,
       label="本金返还（本来就是你的钱）")

for i, x in enumerate(xs):
    plain(ax, x, 10.35, begin_principal[i], fontsize=11, color=C_DARK,
          ha="center", va="bottom")
    plain(ax, x, interest[i] / 2, f"{interest[i]:.2f}", fontsize=11,
          color="white", weight="bold", ha="center", va="center")
    plain(ax, x, interest[i] + principal[i] / 2, f"{principal[i]:.2f}",
          fontsize=11, color="white", weight="bold", ha="center", va="center")

plain(ax, 2.42, 2.90, "真利息", fontsize=11.5, color=C_GREEN, ha="left",
      va="center", weight="bold")
plain(ax, 2.42, 7.75, "本金返还", fontsize=11.5, color=C_RED, ha="left",
      va="center", weight="bold")
plain(ax, 1.34, 13.35,
      "同样是每年分到 10.00 元：真利息从 6.00 元降到 5.51 元，"
      "本金返还从 4.00 元升到 4.49 元",
      fontsize=11.5, color=C_DARK, ha="center", va="center")

ax.set_xticks(xs)
ax.set_xticklabels(years, fontsize=12)
ax.set_xlim(-0.75, 3.95)
ax.set_ylim(0, 15.2)
style_axes(ax, ylabel="每 100 元本金每年拿到的现金分配（元）",
           title="“高收益”是怎么做出来的：把你的本金，分期还给你自己",
           grid_axis="y")
ax.legend(loc="upper left", fontsize=11, frameon=True, bbox_to_anchor=(0.005, 0.86))
plain(ax, -0.72, -1.55, "简化示意数字：本金 100 元，每年固定分配 10 元，"
                        "资产端真实利息率 6%",
      fontsize=10.5, color=C_GRAY, ha="left", va="center")

save(fig, "w3d4_yield_pig.png")
