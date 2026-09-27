"""Week 9 第 2 章配图：同一套现金流，换个贴现率，价值差多少。

设定：一家公司未来 20 年每年给你 100 元，20 年后什么都没有。
四个贴现率分别折回今天：
  8%  → 981.82 元
  10% → 851.36 元
  12% → 746.94 元
  15% → 625.93 元
柱子高度是真实坐标。最高的 981.82 和最低的 625.93 之间差 355.89 元，
也就是同一套预测、同一个模型，光换个贴现率就能差出 36%。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label, brace,
                             C_BLUE, C_GREEN, C_RED, style_axes)

rates = ["8%", "10%", "12%", "15%"]
vals = [981.82, 851.36, 746.94, 625.93]
colors = [C_BLUE, C_BLUE, C_GREEN, C_GREEN]

fig, ax = plt.subplots(figsize=(11.5, 6.8))

xs = [0, 1, 2, 3]
ax.bar(xs, vals, width=0.5, color=colors, zorder=3)
for x, v in zip(xs, vals):
    plain(ax, x, v + 18, f"{v:.2f}", fontsize=12.5, weight="bold",
          color="#222222", va="bottom")

ax.set_xlim(-0.75, 3.78)
ax.set_ylim(0, 1260)
ax.set_xticks(xs)
ax.set_xticklabels([f"贴现率 {r}" for r in rates], fontsize=12.5)

brace(ax, 0, 3, 1090, "同一套现金流预测，光换个贴现率就差 355.89 元（36%）",
      color=C_RED, fontsize=11.5, depth=0.28, text_offset=30)

label(ax, 3.62, 1010,
      "卡拉曼给低等级债券\n用的是 12%~15%；\n"
      "确定性越高的现金流，\n才配用越低的贴现率。",
      fontsize=10.5, color="#444444", ha="right", va="top")

style_axes(ax, xlabel="你要求的年回报率（贴现率）",
           ylabel="这家公司今天值多少钱（元）",
           title="20 年、每年 100 元：贴现率从 8% 抬到 15%，价值掉三分之一还多")

save(fig, "w9d2_rate_sensitivity.png")
