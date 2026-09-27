"""Week 8 第 0 章配图：自上而下 vs 自下而上。

左：自上而下的四个关卡（一条必须步步答对的链条）。
右：自下而上只需要回答的那一个问题。
概念图，坐标 0~10，左右各一个子图。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (fig_multi, save, box, arrow, plain, label,
                             C_RED, C_GREEN, C_GRAY, F_RED, F_GREEN)


fig, axes = fig_multi(1, 2, width=13.6, height=7.0)
axL, axR = axes

# ── 左图：自上而下的链条 ────────────────────────────────────────────
plain(axL, 5, 9.75, "自上而下：一条必须步步答对的链条",
      fontsize=13.5, weight="bold", color=C_RED)

steps = [
    "第 1 关  预测宏观经济\n（明年是繁荣还是衰退？）",
    "第 2 关  判断它对各个行业的影响",
    "第 3 关  挑出会受益的那一家公司",
    "第 4 关  还要比成千上万的人更早买入",
]
ys = [8.1, 6.1, 4.1, 2.1]
for text, y in zip(steps, ys):
    box(axL, 0.6, y, 8.8, 1.2, text, fc=F_RED, ec=C_RED, fontsize=11.5)
for y_hi, y_lo in zip(ys[:-1], ys[1:]):
    arrow(axL, (5, y_hi - 0.02), (5, y_lo + 1.22), color=C_RED, lw=1.8)

label(axL, 5, 0.95,
      "只要有一关答错，整条链就断了；\n而且你往往到最后都不知道是哪一关错了。",
      fontsize=11.5, color=C_RED)

# ── 右图：自下而上只需要回答的问题 ──────────────────────────────────
plain(axR, 5, 9.75, "自下而上：一次只研究一家公司",
      fontsize=13.5, weight="bold", color=C_GREEN)

box(axR, 0.6, 7.5, 8.8, 1.5,
    "这家公司到底值多少钱？", fc=F_GREEN, ec=C_GREEN, fontsize=13)
box(axR, 0.6, 5.1, 8.8, 1.6,
    "我准备付的价格，比它低多少？\n（低得越多，安全边际越厚）",
    fc=F_GREEN, ec=C_GREEN, fontsize=11.5)
box(axR, 0.6, 2.7, 8.8, 1.6,
    "找不到便宜货，就拿着现金等\n（不预测大盘，只等价格）",
    fc=F_GREEN, ec=C_GREEN, fontsize=11.5)

arrow(axR, (5, 7.48), (5, 6.72), color=C_GREEN, lw=1.8)
arrow(axR, (5, 5.08), (5, 4.32), color=C_GREEN, lw=1.8)

label(axR, 5, 1.5,
      "你不必预测任何东西：不预测 GDP，\n不预测利率，也不预测大盘指数。",
      fontsize=11.5, color=C_GREEN)

save(fig, "w8d0_topdown_vs_bottomup.png")
