"""W12 第 1 章配图：持股数量与风险构成（真实坐标堆叠柱状图）。

模型（简化示意，用于教学）：
  组合的价格波动幅度 = 根号( (个股特有风险 22%/根号n)的平方 + (市场风险 18%)的平方 )
  根号在脚本里算，教程正文里只给结果，不出现开方符号。
柱子拆成两段：
  下半段（灰色）= 市场风险，18%，与持股数量无关；
  上半段（蓝色）= 个股特有风险带来的那部分，随持股数量下降。
"""

import math
import sys, pathlib

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, label, style_axes, hline,
                             C_BLUE, C_GRAY, C_ORANGE, C_GREEN, C_RED)

MARKET = 18.0      # 市场风险：整个股市一起跌的那部分（示意）
IDIO = 22.0        # 单只股票的个股特有风险（示意）

counts = [1, 2, 3, 5, 10, 20, 30]
idio = [IDIO / math.sqrt(n) for n in counts]
total = [math.sqrt(v * v + MARKET * MARKET) for v in idio]

fig, ax = plt.subplots(figsize=(12.0, 6.8))
fig.subplots_adjust(top=0.88, bottom=0.26, left=0.09, right=0.98)

xs = list(range(len(counts)))
ax.bar(xs, [MARKET] * len(counts), width=0.52, color="#d9d9d9",
       edgecolor=C_GRAY, lw=1.2, zorder=3, label="市场风险（整个股市一起跌）")
ax.bar(xs, idio, bottom=[MARKET] * len(counts), width=0.52, color=C_BLUE,
       edgecolor=C_BLUE, lw=1.2, zorder=3, label="个股特有的风险（这家公司自己出事）")

for x, t in zip(xs, total):
    plain(ax, x, t + 0.55, f"{t:.1f}%", fontsize=11.5, weight="bold",
          color="#222222", va="bottom")

hline(ax, MARKET, -0.62, len(counts) - 0.38, color=C_RED, lw=1.8, ls="--",
      zorder=4)
label(ax, 5.55, 21.5, "这条红线（18%）是多样化消不掉的那一层",
      fontsize=11.8, color=C_RED, weight="bold", ha="center")

label(ax, 1.55, 32.0, "只买 1 只：\n总波动 28.4%，\n其中一大半是\n这家公司自己的事",
      fontsize=11.0, color=C_BLUE, ha="center", va="center")
label(ax, 4.75, 32.0, "买到 5–10 只以后\n曲线就走平了：再多买\n只是「为了多样化而多样化」",
      fontsize=11.0, color=C_GREEN, ha="center", va="center")
label(ax, 6.0, 9.0, "这一层只能靠对冲\n或者现金压下去", fontsize=11.0,
      color=C_RED, ha="center", va="center")

ax.set_xlim(-0.75, len(counts) - 0.25)
ax.set_ylim(0, 36)
ax.set_xticks(xs)
ax.set_xticklabels([f"{n} 只" for n in counts])
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))
style_axes(ax, xlabel="你持有的股票数量",
           ylabel="组合的价格波动幅度（示意）",
           title="多样化能消掉什么、消不掉什么", grid_axis="y")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.135), ncol=2,
          fontsize=10.5, frameon=False)

fig.text(0.09, 0.025,
         "简化示意数字：单只股票的个股特有风险按 22%、市场风险按 18% 估算，"
         "仅用于展示「快速下降后走平」这个形状，不代表任何真实组合。"
         "注意 Week 8 讲过：波动幅度不等于风险，这里只是用来看多样化的效果。",
         fontsize=9.5, color=C_GRAY, ha="left", va="center")

save(fig, "w12d1_diversify_curve.png")
for n, i, t in zip(counts, idio, total):
    print(f"  {n:2d} 只：个股部分 {i:5.1f}%  合计 {t:5.1f}%")
