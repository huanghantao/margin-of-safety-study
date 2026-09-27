"""W5 第 3 章配图：指数基金的三组真实数字（原书 p64–p65）。

左：1980→1990 指数基金规模；中：标普 500 赢了多少个季度；
右：被纳入指数的价格效应（Blockbuster，1991 年初）。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, style_axes,
                             C_BLUE, C_GRAY, C_GREEN, C_ORANGE, C_RED, C_DARK)

fig, axes = plt.subplots(1, 3, figsize=(15.0, 5.4))

# ── 左：规模 ─────────────────────────────────────────────────────────
ax = axes[0]
ax.bar([0, 1], [100, 1700], width=0.5, color=[C_BLUE, C_GREEN], zorder=3)
plain(ax, 0, 150, "100 亿", fontsize=11.5, color=C_BLUE, weight="bold",
      va="bottom")
plain(ax, 1, 1750, "1700 亿", fontsize=11.5, color=C_GREEN, weight="bold",
      va="bottom")
ax.set_xticks([0, 1])
ax.set_xticklabels(["1980 年", "1990 年"])
ax.set_xlim(-0.6, 1.7)
ax.set_ylim(0, 2300)
style_axes(ax, ylabel="指数基金管理的资金（亿美元）",
           title="十年 17 倍：钱都涌进了指数基金")

# ── 中：季度胜出次数 ─────────────────────────────────────────────────
ax = axes[1]
groups = [0, 1]
sp = [24, 23]
other = [7, 6]
ax.bar([g - 0.19 for g in groups], sp, width=0.34, color=C_ORANGE, zorder=3,
       label="标普 500 指数赢")
ax.bar([g + 0.19 for g in groups], other, width=0.34, color=C_GRAY, zorder=3,
       label="对手赢")
for g, a, b in zip(groups, sp, other):
    plain(ax, g - 0.19, a + 0.8, str(a), fontsize=11.5, color=C_ORANGE,
          weight="bold", va="bottom")
    plain(ax, g + 0.19, b + 0.8, str(b), fontsize=11.5, color=C_GRAY,
          weight="bold", va="bottom")
ax.set_xticks(groups)
ax.set_xticklabels(["对普通股票型\n共同基金\n（共 31 个季度）",
                    "对威尔士 5000\n指数\n（共 29 个季度）"], fontsize=10)
ax.set_xlim(-0.7, 1.7)
ax.set_ylim(0, 33)
style_axes(ax, ylabel="标普 500 胜出的季度数",
           title="那些年，指数一直在赢")
ax.legend(loc="upper right", fontsize=10)

# ── 右：纳入指数的价格效应 ────────────────────────────────────────────
ax = axes[2]
ax.bar([0, 1], [9.1, 4.0], width=0.5, color=[C_RED, C_ORANGE], zorder=3)
plain(ax, 0, 9.7, "+9.1%", fontsize=11.5, color=C_RED, weight="bold",
      va="bottom")
plain(ax, 1, 4.6, "+4%", fontsize=11.5, color=C_ORANGE, weight="bold",
      va="bottom")
ax.set_xticks([0, 1])
ax.set_xticklabels(["Blockbuster\n被纳入标普 500\n当天（1991 年初）",
                    "新股票被纳入指数后\n第一周平均跑赢\n市场约 4%"], fontsize=9.5)
ax.set_xlim(-0.7, 1.7)
ax.set_ylim(0, 12.5)
style_axes(ax, ylabel="涨幅（%）",
           title="被纳入指数：一次没有基本面理由的上涨")

fig.subplots_adjust(wspace=0.42)
plain(ax, 1.68, -3.6, "数字照抄原书 p64–p65", fontsize=10, color=C_DARK,
      ha="right", va="center")

save(fig, "w5d3_index_flow.png")
