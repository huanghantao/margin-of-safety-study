"""Week 7 第 1 章配图：三种获利方式的可靠度差异。

同一个买入价、同一份利润增长，卖出时市场给的倍数不同，
你的收益会差出三倍。全部为明确标注的简化示意数字，可以手算复核：
  买入：每股利润 1 元 x 10 倍市盈率 = 10 元
  5 年后：每股利润 1.61 元（每年 +10%）
  情景 A 市场给 12 倍：1.61 x 12 = 19.32 元，赚 9.3 元（+93%）
  情景 B 市场给 8 倍：1.61 x 8 = 12.88 元，赚 2.9 元（+29%）
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, plain, label,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_DARK)

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(11.6, 6.6))

groups = ["情景 A：卖出时市场给 12 倍", "情景 B：卖出时市场给 8 倍"]
profit = [6.1, 6.1]          # 每股利润 1 → 1.61，按当时倍数折算的贡献
multiple = [3.2, -3.2]       # 倍数变化带来的贡献
x = [0.0, 1.0]
w = 0.30

b1 = ax.bar([i - w / 2 - 0.02 for i in x], profit, width=w,
            color=C_GREEN, zorder=3, label="企业利润增长的贡献")
b2 = ax.bar([i + w / 2 + 0.02 for i in x], multiple, width=w,
            color=C_ORANGE, zorder=3, label="市场倍数变化的贡献")

for b, v in zip(b1, profit):
    plain(ax, b.get_x() + b.get_width() / 2, v + 0.35, f"+{v} 元",
          fontsize=12, weight="bold", color=C_GREEN, va="bottom")
for b, v in zip(b2, multiple):
    if v >= 0:
        plain(ax, b.get_x() + b.get_width() / 2, v + 0.35, f"+{v} 元",
              fontsize=12, weight="bold", color=C_ORANGE, va="bottom")
    else:
        plain(ax, b.get_x() + b.get_width() / 2, v - 0.35, f"{v} 元",
              fontsize=12, weight="bold", color=C_RED, va="top")

ax.axhline(0, color=C_DARK, lw=1.2, zorder=2)
ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=12)
ax.set_ylim(-6.5, 10.5)
style_axes(ax, ylabel="相对 10 元买入价，各部分贡献了多少钱（元）",
           title="同样的利润增长，卖出时的倍数决定你赚多少（简化示意数字）")
ax.legend(fontsize=11, loc="upper left", framealpha=0.95)

label(ax, 0.5, -5.3, "情景 A 总共赚 9.3 元（+93%）；情景 B 只赚 2.9 元（+29%）",
      fontsize=12, color=C_DARK, weight="bold")

fig.tight_layout(pad=1.8)
save(fig, "w7d1_source_reliability.png")
