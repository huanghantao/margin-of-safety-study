"""Week 10 第 3 章配图：同样的折扣，等 1 年、3 年、5 年、10 年拿到的年化收益。

买入 60 元、价值 100 元，总收益 66.7%（这是同一笔钱，只是兑现的年份不同）。
纵轴只有一个口径：年化收益率（%）。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, plain, style_axes,
                             C_GREEN, C_RED, C_GRAY, C_GOLD)

fig, ax = plt.subplots(figsize=(11.6, 6.4))

labels = ["1 年就实现", "3 年实现", "5 年实现", "10 年才实现"]
years = [1, 3, 5, 10]
rates = [66.7, 18.6, 10.8, 5.2]
colors = [C_GREEN, C_GREEN, C_GOLD, C_RED]

bars = ax.bar(labels, rates, color=colors, width=0.52, zorder=3)

for x, r in zip(range(4), rates):
    ax.text(x, r + 1.6, f"{r}%", ha="center", va="bottom",
            fontsize=13, weight="bold", color="#333333", zorder=5)

# 唯一的参照线：不冒风险的理财水平（说明文字放在坐标区右侧外面，绝不压柱）
ax.axhline(5.0, ls="--", lw=1.8, color=C_GRAY, zorder=2)
plain(ax, 3.58, 5.0, "5%：不冒风险的理财水平", fontsize=10.5,
      color="#555555", ha="left", va="center", clip_on=False)

ax.set_ylim(0, 78)
style_axes(ax, xlabel="这笔 66.7% 的收益，用几年拿到", ylabel="年化收益率（%）",
           title="买入 60 元、价值 100 元：同一笔收益，等得越久年化越低")

label(ax, 1.5, 46, "同一笔钱、同一个终点，\n只是等的时间不同。",
      fontsize=11, color="#333333")

save(fig, "w10d3_wait_cost.png")
