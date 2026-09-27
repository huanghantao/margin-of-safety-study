"""Week 9 第 3 章第二张图：格雷厄姆式的那把尺子 —— 纯营运资金净额。

横轴是钱（元），五行从左往右读：
  流动资产 100
  减 流动负债 35  → 营运资金净额 65
  减 长期债务 20  → 纯营运资金净额 45
最后一行绿色柱子就是这个「最硬的底」：如果一家公司的总市值买不到
这 45 元，格雷厄姆式的投资者就开始感兴趣。

数字是教学示意数字，公式出自原书 p146 对 net net working capital 的解释。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label,
                             C_BLUE, C_GREEN, C_RED, C_GOLD, style_axes)

rows = [
    ("流动资产 100 元\n（现金 40 + 应收 35 + 库存 25）", 0, 100, C_BLUE, "100"),
    ("减：流动负债 35 元\n（应付账款、一年内到期的钱）", 65, 35, C_RED, "-35"),
    ("= 营运资金净额 65 元", 0, 65, C_GOLD, "65"),
    ("减：长期债务 20 元\n（一年以后才要还的）", 45, 20, C_RED, "-20"),
    ("= 纯营运资金净额 45 元", 0, 45, C_GREEN, "45"),
]

fig, ax = plt.subplots(figsize=(12.5, 6.2))

for i, (name, left, width, c, txt) in enumerate(rows):
    y = len(rows) - 1 - i
    ax.add_patch(plt.Rectangle((left, y - 0.3), width, 0.6, fc=c, ec=c,
                               lw=1.4, zorder=3, alpha=0.88))
    plain(ax, left + width + 2.5, y, txt + " 元", fontsize=11.5,
          weight="bold", color="#222222", va="center", ha="left")

label(ax, 118, 4, "账上能较快变成现金的东西", fontsize=11, color=C_BLUE,
      ha="left")
label(ax, 118, 3, "一年内要还掉的钱", fontsize=11, color=C_RED, ha="left")
label(ax, 118, 2, "流动资产减流动负债", fontsize=11, color="#8a6d1f", ha="left")
label(ax, 118, 1, "一年以后才要还的钱", fontsize=11, color=C_RED, ha="left")
label(ax, 118, 0,
      "格雷厄姆的尺子：\n"
      "如果整家公司卖掉\n"
      "还不到 45 元，\n"
      "那就值得细看。",
      fontsize=11, color=C_GREEN, ha="left", va="center")

ax.set_xlim(-3, 178)
ax.set_ylim(-0.9, 4.9)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in reversed(rows)], fontsize=10.5)
plt.setp(ax.get_yticklabels(), va="center")
ax.set_xticks([0, 20, 40, 60, 80, 100])

style_axes(ax, xlabel="每股多少元（教学示意数字）",
           title="纯营运资金净额怎么算：流动资产一路扣到只剩最硬的那部分",
           grid_axis="x")

save(fig, "w9d3_pure_working_capital.png")
