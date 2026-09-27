"""W4 第 4 章图二：费率对长期收益的侵蚀（真实坐标折线图）。

10 万元本金，毛收益 8%/年；一种持有人每年只付 0.2% 的费用，
另一种每年付 1.4%。30 年后的差距在脚本里算出来，直接标在图上。
"""

import sys, pathlib

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, label, style_axes, vline,
                             C_GREEN, C_RED, C_GRAY, C_ORANGE)

PRINCIPAL = 100_000
GROSS = 0.08
FEE_LOW = 0.002
FEE_HIGH = 0.014
YEARS = 30

years = list(range(YEARS + 1))
low = [PRINCIPAL * (1 + GROSS - FEE_LOW) ** n for n in years]
high = [PRINCIPAL * (1 + GROSS - FEE_HIGH) ** n for n in years]
gap = low[-1] - high[-1]

fig, ax = plt.subplots(figsize=(12.0, 6.8))
fig.subplots_adjust(top=0.87, bottom=0.17, left=0.10, right=0.98)

ax.fill_between(years, high, low, color="#fdf1e3", zorder=1)
ax.plot(years, low, color=C_GREEN, lw=2.8, zorder=4)
ax.plot(years, high, color=C_RED, lw=2.8, zorder=4)
vline(ax, YEARS, 0, low[-1], color=C_GRAY, lw=1.2, ls=":", zorder=2)

label(ax, 29.0, low[-1], f"每年只付 0.2% 费用\n30 年后 {low[-1] / 10000:.1f} 万元",
      color=C_GREEN, fontsize=11.5, weight="bold", ha="left", va="center")
label(ax, 29.0, high[-1], f"每年付 1.4% 费用\n30 年后 {high[-1] / 10000:.1f} 万元",
      color=C_RED, fontsize=11.5, weight="bold", ha="left", va="center")
label(ax, 29.0, (low[-1] + high[-1]) / 2, f"相差 {gap / 10000:.1f} 万元",
      color=C_ORANGE, fontsize=12, weight="bold", ha="left", va="center")

plain(ax, 8.6, 660000,
      "两边的毛收益都是 8%/年，\n只因每年 1.2 个百分点的费率差，\n30 年就少了一辆车。",
      fontsize=12, color="#222222", ha="left", va="center")

ax.set_xlim(0, 44)
ax.set_ylim(0, low[-1] * 1.14)
ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
ax.set_yticks([0, 200000, 400000, 600000, 800000, 1000000])
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v / 10000:.0f} 万"))
style_axes(ax, xlabel="持有年数", ylabel="10 万元变成多少钱",
           title="毛收益都是 8%，费用差 1.2 个百分点，30 年差出一辆车", grid_axis="y")

fig.text(0.10, 0.045,
         "10 万元本金，毛收益 8%/年，费用按年从收益里扣；未考虑税与买卖价差。",
         fontsize=10, color=C_GRAY, ha="left", va="center")

save(fig, "w4d4_fee_drag.png")
print(f"  低费率终值 {low[-1]:,.0f} 元；高费率终值 {high[-1]:,.0f} 元；差 {gap:,.0f} 元")
for n in (5, 10, 20, 30):
    print(f"   第 {n:2d} 年：{low[n]:>10,.0f}  vs  {high[n]:>10,.0f}")
