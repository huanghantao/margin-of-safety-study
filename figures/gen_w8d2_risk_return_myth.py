"""Week 8 第 2 章配图：风险与回报被讲错的关系。

左：流行的说法——一条向上的直线。
右：真实的图景——机会散布成一整片，便宜货在左上，陷阱在右下。
两幅子图都用真实坐标（0~10），轴线用箭头画。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (fig_multi, save, arrow, plain, label,
                             C_RED, C_GREEN, C_GRAY)


fig, axes = fig_multi(1, 2, width=13.6, height=6.8)
axL, axR = axes


def draw_axes(ax):
    """画一个只有方向、没有刻度的坐标系。"""
    arrow(ax, (1.1, 0.75), (9.7, 0.75), color="#555555", lw=1.5,
          shrinkA=0, shrinkB=0)
    arrow(ax, (1.1, 0.75), (1.1, 9.4), color="#555555", lw=1.5,
          shrinkA=0, shrinkB=0)
    plain(ax, 9.7, 1.05, "风险（可能亏钱的程度）", fontsize=11,
          color="#555555", ha="right", va="center")
    plain(ax, 1.5, 9.15, "回报", fontsize=11, color="#555555", ha="left",
          va="center")


# ── 左图：错误的一条直线 ────────────────────────────────────────────
draw_axes(axL)
plain(axL, 5.3, 9.75, "流行的说法：高风险 = 高回报",
      fontsize=13, weight="bold", color=C_RED)
axL.plot([1.4, 9.0], [1.4, 8.8], color=C_RED, lw=2.6, zorder=3)
axL.plot([2.6, 5.2, 7.8], [2.55, 5.1, 7.6], "o", color=C_RED, ms=8, zorder=4)
label(axL, 3.3, 1.35, "低风险\n低回报", fontsize=10.5, color=C_RED)
label(axL, 5.9, 3.9, "中等风险\n中等回报", fontsize=10.5, color=C_RED)
label(axL, 7.2, 8.6, "高风险\n高回报", fontsize=10.5, color=C_RED)
label(axL, 5.3, 0.15,
      "这条线把「可能亏钱」当成了会自动发奖金的东西。",
      fontsize=11, color="#444444")

# ── 右图：真实的图景 ────────────────────────────────────────────────
draw_axes(axR)
plain(axR, 5.3, 9.75, "真实的图景：机会散成一整片",
      fontsize=13, weight="bold", color=C_GREEN)
axR.plot([1.4, 9.0], [1.4, 8.8], color=C_GRAY, lw=1.6, ls=(0, (5, 4)),
         zorder=2)

axR.plot([2.3, 3.1, 4.3], [7.5, 6.6, 7.0], "o", color=C_GREEN, ms=9,
         zorder=4)
axR.plot([6.6, 7.9, 7.2], [3.1, 2.1, 4.0], "o", color=C_RED, ms=9, zorder=4)
label(axR, 3.4, 8.4, "低风险、高回报：\n被市场遗弃的便宜货（少见，但存在）",
      fontsize=10.5, color=C_GREEN, ha="left")
label(axR, 6.2, 2.0, "高风险、低回报：\n定价过高的热门股（很常见）",
      fontsize=10.5, color=C_RED, ha="right")
label(axR, 5.3, 0.15,
      "虚线就是左图那条线。风险本身不发奖金，只有价格才发。",
      fontsize=11, color="#444444")

save(fig, "w8d2_risk_return_myth.png")
