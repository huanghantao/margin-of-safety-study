"""W3 第 0 章图二：投资品 vs 投机品 —— 钱从哪里来。

左边：投资品会自己生出现金流（母鸡下蛋）。
右边：投机品不生现金流，唯一的出路是卖给下一个人。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_DARK,
                             F_BLUE, F_ORANGE, F_GREEN, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 6.8)

plain(ax, 5.0, 9.72, "投资品和投机品都能买卖、都会涨跌，区别只有一个：它自己会不会生钱",
      fontsize=13, weight="bold", color=C_DARK)

# ── 左：投资品 ──────────────────────────────────────────────
box(ax, 0.35, 6.55, 4.35, 2.65,
    "投资品\n\n• 一家公司的股票\n• 一张债券（借条）\n• 一台会干活的机器\n• 一幢收租的房子",
    fc=F_GREEN, ec=C_GREEN, fontsize=11.5)
box(ax, 0.35, 4.05, 4.35, 1.55,
    "它自己会生钱：\n股息、利息、租金、机器产出的货",
    fc=F_GREEN, ec=C_GREEN, fontsize=11.5)
arrow(ax, (2.52, 6.45), (2.52, 5.72), color=C_GREEN, lw=2.2)
box(ax, 0.35, 1.75, 4.35, 1.65,
    "你的回报 = 它生出来的钱\n+ 别人愿意出的价（可有可无）",
    fc="white", ec=C_GREEN, fontsize=11.5)

# ── 右：投机品 ──────────────────────────────────────────────
box(ax, 5.55, 6.55, 4.35, 2.65,
    "投机品\n\n• 名画、古董、纪念卡片\n• 收藏级白酒、邮票\n• 前文那种“交易用沙丁鱼”",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=11.5)
box(ax, 5.55, 4.05, 4.35, 1.55,
    "它自己什么也不生：\n现金流 = 0",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=11.5)
arrow(ax, (7.72, 6.45), (7.72, 5.72), color=C_ORANGE, lw=2.2)
box(ax, 5.55, 1.75, 4.35, 1.65,
    "你的回报 = 只有别人出的价\n（也就是必须找到下一个买家）",
    fc="white", ec=C_ORANGE, fontsize=11.5)

# ── 底部一句总结 ────────────────────────────────────────────
box(ax, 1.4, 0.28, 7.2, 0.95,
    "同一个东西可以是投资品，也可以是投机品：\n看它有没有现金流，不看它的价格涨得多凶",
    fc=F_GRAY, ec=C_GRAY, fontsize=11.5)

save(fig, "w3d0_invest_vs_spec.png")
