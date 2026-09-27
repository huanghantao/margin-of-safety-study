"""W5 第 0 章配图：季度排名竞赛 —— 先落后、后领先的路径，撑不到终点。

真实坐标：横轴是 8 个季度，纵轴是累计收益（%）。
基金 B 在第 2 季度落后指数，被客户赎回；实线到第 2 季度为止，
后面那段虚线是"他本来能赚到、但客户拿不到"的收益。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, label, plain, style_axes,
                             C_BLUE, C_ORANGE, C_GRAY, C_RED, C_DARK)

fig, ax = plt.subplots(figsize=(11.5, 6.9))

q = [1, 2, 3, 4, 5, 6, 7, 8]
fund_a = [0, 2, 3, 5, 6, 8, 9, 12]          # 每季都不难看，长期平庸
fund_b = [0, -4, -2, 3, 9, 16, 24, 32]      # 先落后，后领先
index = [0, 1.5, 2, 4, 5, 6.5, 8, 9]        # 及格线（指数）

ax.axhline(0, color=C_GRAY, lw=1.0, ls=":", zorder=1)
ax.plot(q, index, color=C_GRAY, lw=2.0, ls="--", marker="s", ms=4.0, zorder=3,
        label="指数（及格线）")
ax.plot(q, fund_a, color=C_ORANGE, lw=2.6, marker="o", ms=5.0, zorder=4,
        label="基金 A：每个季度都不难看")
ax.plot(q[:2], fund_b[:2], color=C_BLUE, lw=3.2, marker="o", ms=5.5, zorder=5,
        label="基金 B：先落后、后领先")
ax.plot(q[1:], fund_b[1:], color=C_BLUE, lw=2.0, ls=(0, (5, 3)), alpha=0.45,
        marker="o", ms=4.0, zorder=4)

ax.axvline(2, color=C_RED, lw=1.6, ls="--", zorder=2)

ax.plot([2], [-4], marker="o", ms=13, mfc="none", mec=C_RED, mew=2.6, zorder=6)
ax.plot([8], [32], marker="o", ms=13, mfc="none", mec=C_BLUE, mew=2.6, zorder=6)

label(ax, 2.35, -12.5, "第 2 季度：B 落后指数 5.5 个百分点\n客户赎回 → B 出局",
      color=C_RED, fontsize=11.5, ha="left", va="center", weight="bold")
label(ax, 4.35, 33.5, "第 8 季度：B 累计 +32%，A 只有 +12%\n"
                      "但 B 后面这 6 个季度的业绩，客户永远拿不到",
      color=C_BLUE, fontsize=11.5, ha="left", va="center", weight="bold")
label(ax, 8.5, -8.0, "B 的实线只到第 2 季度：\n他被换掉的那一刻，考核就结束了",
      color=C_DARK, fontsize=11, ha="right", va="center")

ax.set_xlim(0.4, 8.6)
ax.set_ylim(-16, 47)
ax.set_xticks(q)
style_axes(ax, xlabel="季度（每 3 个月考核一次）", ylabel="累计收益（%）",
           title="机构比的是季度排名：先落后的人，等不到他领先的那一天",
           grid_axis="y")
ax.legend(loc="upper left", fontsize=11, frameon=True)
plain(ax, 8.55, -19.5, "数字为简化示意，用于教学", fontsize=10.5, color=C_GRAY,
      ha="right", va="center")

save(fig, "w5d0_quarter_race.png")
