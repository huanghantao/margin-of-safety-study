"""Week 1 第 2 章配图之二：奶茶店开店投入 30 万元，几年回本（真实坐标柱状图）。

⚠️ 图中数字是**简化示意数字**，用于教学，不是任何真实店铺的财务数据。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10.5, 6.2))

years = [1, 2, 3, 4]
cum = [8, 17, 28, 40]          # 累计净现金流入（万元，示意）

ax.bar(years, cum, width=0.55, color="#e8c66a", edgecolor="#8a6d1f",
       lw=1.4, zorder=3)
ax.axhline(30, color=C_RED, lw=2.0, ls="--", zorder=2)

# 数值写在柱子内部，避免与 30 万元这条横线相撞
for x, v in zip(years, cum):
    plain(ax, x, v / 2, f"{v} 万", color="#4a3810", fontsize=12,
          weight="bold")

# 回本点：第 3 年结束时累计 28 万，第 4 年按一年 12 万均匀流入，再 2 万约需 2 个月
ax.plot([3.17], [30], marker="o", ms=9, color=C_RED, zorder=6)

label(ax, 4.30, 30, "开店投入 30 万元", color=C_RED, fontsize=11, ha="left")
label(ax, 1.42, 34.5, "大约第 3 年零两个月，累计现金\n才追上开店的投入", fontsize=10.5,
      color="#a02020")
arrow(ax, (2.55, 33.4), (3.05, 30.5), color=C_RED, lw=1.5)

style_axes(ax, xlabel="经营年数", ylabel="累计净现金流入（万元）",
           title="奶茶店：开店投入 30 万元，几年能回本？",
           grid_axis="y", fontsize=11, title_size=13)
ax.set_ylim(0, 48)
ax.set_xlim(0.35, 5.55)
ax.set_xticks(years)
ax.set_xticklabels([f"第 {y} 年" for y in years])

save(fig, "w1d2_milktea_payback.png")
