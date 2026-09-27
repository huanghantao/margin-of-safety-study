"""Week 7 第 1 章配图：买入之后，你的钱从三条路进来。

三条路的可靠度天差地别：企业赚钱（最可靠）、市场抬倍数（最不可靠）、
价格向价值回归（需要时间与催化剂）。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, plain, label,
                             C_BLUE, C_ORANGE, C_GREEN, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD)

fig, ax = fig_ax(11.6, 6.8)

plain(ax, 5.0, 9.62, "买入之后，你的钱从三条路进来", fontsize=15,
      weight="bold", color="#222222")
plain(ax, 5.0, 9.05, "三条路的可靠度天差地别，而多数人只盯着第二条",
      fontsize=11.5, color=C_GRAY)

# ── 三条路的方框 ────────────────────────────────────────────────────
top = 6.6
h = 2.05
w = 3.0
xs = [0.25, 3.5, 6.75]
texts = [
    "路① 企业赚的钱变多\n（现金流增长）\n\n最可靠：靠生意本身",
    "路② 市场给的倍数变高\n（估值提升）\n\n最不可靠：靠别人出价",
    "路③ 价格向价值回归\n（折价收敛）\n\n需要耐心：等时间与催化剂",
]
fcs = [F_GREEN, F_ORANGE, F_BLUE]
ecs = [C_GREEN, C_ORANGE, C_BLUE]
for x, t, fc, ec in zip(xs, texts, fcs, ecs):
    box(ax, x, top, w, h, t, fc=fc, ec=ec, fontsize=11, lw=1.8)

# ── 三支箭头汇到下面的总回报条 ──────────────────────────────────────
for x, tx in zip(xs, [2.0, 5.0, 8.0]):
    arrow(ax, (x + w / 2, top), (tx, 3.05), color=C_GRAY, lw=1.8,
          connectionstyle="arc3,rad=0.08")

box(ax, 0.6, 1.25, 8.8, 1.75,
    "你的总回报 = 现金流增长 + 分红 + 倍数变化 + 折价收敛",
    fc=F_GOLD, ec=C_GOLD, fontsize=13.5, lw=1.8, weight="bold")

label(ax, 5.0, 0.5, "第 1 条与第 3 条可以慢慢等；第 2 条来的时候，也会走",
      fontsize=11.5, color=C_ORANGE)

save(fig, "w7d1_three_sources.png")
