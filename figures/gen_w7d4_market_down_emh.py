"""Week 7 第 4 章配图（双联图）。

左：下跌的市场里，价格跌到价值下方更深处 —— 折扣（安全边际）反而变厚。
右：有效市场假设的三种形态，以及卡拉曼对每一种的判断。
全部为简化示意数字与概念示意。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, box,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY,
                             F_GREEN, F_RED)

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.5, 6.4))

# ══ 左：下跌让折扣变厚 ══════════════════════════════════════════════
t = [0, 1, 2, 3, 4, 5, 6]
value = [20, 20, 20.5, 20.5, 21, 21, 21]
price = [20, 17, 13, 11, 14.5, 18, 19.5]

ax1.fill_between(t, price, value, where=[p < v for p, v in zip(price, value)],
                 color=C_GREEN, alpha=0.16, interpolate=True, zorder=1)
ax1.plot(t, value, color=C_GREEN, lw=2.6, marker="o", zorder=3)
ax1.plot(t, price, color=C_ORANGE, lw=2.6, marker="o", zorder=3)
ax1.scatter([3], [11], s=130, color=C_ORANGE, edgecolors="white",
            linewidths=1.6, zorder=5)

label(ax1, 0.06, 23.0, "保守估算的价值：约 20 元", fontsize=11.5,
      color=C_GREEN, ha="left", weight="bold")
label(ax1, 3.05, 7.2, "熊市底部：价格 11 元\n折价 45%，安全边际最厚", fontsize=11.5,
      color=C_ORANGE, ha="left")
label(ax1, 5.95, 24.6, "价格回到 19.5 元：\n情绪修复，折价收窄", fontsize=11.5,
      color=C_GRAY, ha="right")
label(ax1, 3.6, 17.0, "绿色区域 = 折价（安全边际）", fontsize=11.5,
      color=C_GREEN)

ax1.set_xlim(-0.3, 6.3)
ax1.set_ylim(5, 27)
ax1.set_xticks(t)
style_axes(ax1, xlabel="时间（年）", ylabel="每股价格 / 价值（元，示意数字）",
           title="下跌不是风险：它让折扣变大")

# ══ 右：有效市场假设的三种形态 ══════════════════════════════════════
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis("off")
plain(ax2, 5.0, 9.5, "有效市场假设的三种形态", fontsize=14, weight="bold")
plain(ax2, 5.0, 8.85, "它们一个比一个强，也一个比一个容易被现实打脸",
      fontsize=11, color=C_GRAY)

rows = [
    ("弱式有效：过去的价格走势\n无法预测未来", "成立：技术分析确实浪费时间",
     F_GREEN, C_GREEN),
    ("半强式有效：所有公开信息\n都已经反映在价格里", "不成立：勤奋研究的人能找到错误定价",
     F_RED, C_RED),
    ("强式有效：连未公开的信息\n也不能让你赚到超额回报", "更不成立：市场远没有有效到那个程度",
     F_RED, C_RED),
]
for i, (left, right, fc, ec) in enumerate(rows):
    y = 6.4 - i * 2.35
    box(ax2, 0.3, y, 4.6, 1.8, left, fc=fc, ec=ec, fontsize=11)
    box(ax2, 5.2, y, 4.6, 1.8, right, fc="#ffffff", ec=ec, fontsize=11)

plain(ax2, 5.0, 0.85, "如果市场真的完全有效，价值投资者只能无所事事",
      fontsize=11.5, color=C_GRAY)

fig.tight_layout(pad=2.0)
save(fig, "w7d4_market_down_emh.png")
