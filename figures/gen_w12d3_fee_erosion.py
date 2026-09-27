"""W12 第 3 章配图一：基金费率对长期收益的侵蚀（真实坐标）。

10 万元本金，毛收益都是 8%/年：
  低费率：每年扣 0.5%（指数基金的管理费 + 托管费，示意）
  高费率：每年扣 2.0%（主动基金的管理费 + 托管费 + 申购赎回费摊销 + 销售服务费，示意）
差额正好是每年 1.5 个百分点。数值在脚本里算出来，正文的「算一算」逐年列出。
"""

import sys, pathlib

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, label, style_axes, vline,
                             C_GREEN, C_RED, C_ORANGE, C_GRAY)

PRINCIPAL = 100_000
GROSS = 0.08
FEE_LOW = 0.005
FEE_HIGH = 0.020
YEARS = 30

years = list(range(YEARS + 1))
low = [PRINCIPAL * (1 + GROSS - FEE_LOW) ** n for n in years]
high = [PRINCIPAL * (1 + GROSS - FEE_HIGH) ** n for n in years]

fig, ax = plt.subplots(figsize=(12.2, 6.8))
fig.subplots_adjust(top=0.87, bottom=0.17, left=0.10, right=0.99)

ax.fill_between(years, high, low, color="#fdf1e3", zorder=1)
ax.plot(years, low, color=C_GREEN, lw=2.8, zorder=4)
ax.plot(years, high, color=C_RED, lw=2.8, zorder=4)

vline(ax, YEARS, 0, low[-1], color=C_GRAY, lw=1.2, ls=":", zorder=2)

label(ax, 30.6, low[-1], f"每年付 0.5% 费用\n30 年后 {low[-1] / 10000:.1f} 万元",
      color=C_GREEN, fontsize=11.5, weight="bold", ha="left", va="center")
label(ax, 30.6, high[-1], f"每年付 2.0% 费用\n30 年后 {high[-1] / 10000:.1f} 万元",
      color=C_RED, fontsize=11.5, weight="bold", ha="left", va="center")
label(ax, 24.3, (low[-1] + high[-1]) / 2 + 20000,
      f"差 {int(round(low[-1] - high[-1])) / 10000:.0f} 万元",
      color=C_ORANGE, fontsize=13, weight="bold", ha="left", va="center")

for n in (10, 20):
    label(ax, n, (low[n] + high[n]) / 2 + 3000,
          f"第 {n} 年差 {int(round(low[n] - high[n])) / 10000:.1f} 万元",
          color=C_ORANGE, fontsize=10.5, ha="center", va="center")

plain(ax, 1.0, 700000,
      "两边的毛收益都是 8%/年，\n只因每年 1.5 个百分点的费率差，\n30 年后少了约 30 万元。",
      fontsize=12.0, color="#222222", ha="left", va="center")

ax.set_xlim(0, 45)
ax.set_ylim(0, 980000)
ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
ax.set_yticks([0, 200000, 400000, 600000, 800000])
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v / 10000:.0f} 万"))
style_axes(ax, xlabel="持有年数", ylabel="10 万元变成多少钱",
           title="毛收益都是 8%，每年少付 1.5 个百分点的费用，30 年差出约 30 万元",
           grid_axis="y")

fig.text(0.10, 0.045,
         "10 万元本金，毛收益 8%/年，费用按年从收益里扣；未考虑税、买卖价差与申赎时点。"
         "费率为简化示意数字，真实费率以基金合同为准。",
         fontsize=9.5, color=C_GRAY, ha="left", va="center")

save(fig, "w12d3_fee_erosion.png")

print("  年份   低费率(0.5%)   高费率(2.0%)      差额")
for n in years:
    print(f"  {n:3d}  {low[n]:14,.0f}  {high[n]:14,.0f}  {low[n] - high[n]:12,.0f}")
