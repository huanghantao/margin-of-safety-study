"""W3 第 1 章图：同一张股票，两条完全不同的赚钱链条。

上链（投资者）：你买的是一门生意的一部分，钱由生意生出来。
下链（投机者）：你买的是一张纸，钱只能由下一个买家掏出来。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain,
                             C_BLUE, C_ORANGE, C_GREEN, C_GRAY, C_DARK,
                             F_BLUE, F_ORANGE, F_GREEN, F_GRAY)

fig, ax = fig_ax(11.5, 7.4)

plain(ax, 5.0, 9.78, "同一张股票，两条完全不同的赚钱链条",
      fontsize=14, weight="bold", color=C_DARK)
plain(ax, 5.0, 9.30, "证券本身不贴标签 —— 分红的是它，能被反复倒手的也是它；"
                     "区别只在买它的人打算赚哪一段钱",
      fontsize=11, color=C_GRAY)

# ── 上面这条链：投资者 ───────────────────────────────────────
box(ax, 0.20, 7.55, 2.10, 1.30, "你\n（投资者）", fc=F_BLUE, ec=C_BLUE,
    fontsize=11.5, weight="bold")
box(ax, 2.75, 7.55, 2.30, 1.30, "公司的一部分\n所有权", fc=F_GREEN, ec=C_GREEN,
    fontsize=11.5)
box(ax, 5.50, 7.55, 2.30, 1.30, "公司做生意\n赚出现金流", fc=F_GREEN, ec=C_GREEN,
    fontsize=11.5)
box(ax, 8.25, 7.55, 1.55, 1.30, "钱回到\n你手里", fc=F_GREEN, ec=C_GREEN,
    fontsize=11.5, weight="bold")
for x0, x1 in ((2.34, 2.71), (5.09, 5.46), (7.84, 8.21)):
    arrow(ax, (x0, 8.20), (x1, 8.20), color=C_GREEN, lw=2.2)

label(ax, 5.0, 6.78, "赚的是：分红 + 公司长大后价值的提升 + 价格向价值回归的差价\n"
                     "（三条路都不需要别人犯傻，只需要公司真的赚钱）",
      color=C_GREEN, fontsize=11.5)

# ── 下面这条链：投机者 ───────────────────────────────────────
box(ax, 0.20, 4.55, 2.10, 1.30, "你\n（投机者）", fc=F_ORANGE, ec=C_ORANGE,
    fontsize=11.5, weight="bold")
box(ax, 2.75, 4.55, 2.30, 1.30, "一张可以\n反复换手的纸", fc=F_ORANGE,
    ec=C_ORANGE, fontsize=11.5)
box(ax, 5.50, 4.55, 2.30, 1.30, "猜别人下一步\n会怎么买卖", fc=F_ORANGE,
    ec=C_ORANGE, fontsize=11.5)
box(ax, 8.25, 4.55, 1.55, 1.30, "钱回到\n你手里", fc=F_ORANGE, ec=C_ORANGE,
    fontsize=11.5, weight="bold")
for x0, x1 in ((2.34, 2.71), (5.09, 5.46), (7.84, 8.21)):
    arrow(ax, (x0, 5.20), (x1, 5.20), color=C_ORANGE, lw=2.2)

label(ax, 5.0, 3.78, "赚的是：下一个买家愿意出的更高价\n"
                     "（公司赚不赚钱无所谓，只要还有人接盘就行）",
      color=C_ORANGE, fontsize=11.5)

# ── 结论 ─────────────────────────────────────────────────────
box(ax, 0.20, 1.05, 9.60, 1.90,
    "关键区别不在“买了什么”，而在“凭什么赚钱”\n\n"
    "• 钱来自公司经营  →  投资（即使他买的是别人眼里的垃圾股）\n"
    "• 钱来自下一个人  →  投机（即使他买的是茅台、是蓝筹、是“核心资产”）",
    fc=F_GRAY, ec=C_GRAY, fontsize=12)

save(fig, "w3d1_two_players.png")
