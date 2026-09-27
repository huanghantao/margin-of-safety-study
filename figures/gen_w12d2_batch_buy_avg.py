"""W12 第 2 章配图一：分批买入的均价（真实坐标）。

情境（简化示意数字，与正文「算一算」完全一致）：
  A 先生：第 0 个月在 20 元一次性投入 5.92 万元，买入 2960 股。
  B 先生：同样 5.92 万元分三批：
        第 0 个月 20 元买 2 万元 → 1000 股
        第 4 个月 16 元买 2 万元 → 1250 股
        第 8 个月 12 元买 1.92 万元 → 1600 股（A 股按 100 股整数倍下单）
        合计 3850 股，平均成本 15.38 元。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, label, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY)

months = list(range(25))
prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11.5, 12.5, 13, 14, 15,
          16, 17, 18, 19, 20, 20.5, 21, 21.5, 22, 22, 22]

COST_A = 20.00          # 一次性买入的成本
COST_B = 59200 / 3850   # 分批买入的平均成本 = 15.38 元
BUYS = [(0, 20, "第 1 批 2 万元 @20 元 = 1000 股"),
        (4, 16, "第 2 批 2 万元 @16 元 = 1250 股"),
        (8, 12, "第 3 批 1.92 万元 @12 元 = 1600 股")]

fig, ax = plt.subplots(figsize=(12.2, 6.6))
fig.subplots_adjust(top=0.88, bottom=0.15, left=0.085, right=0.99)

ax.plot(months, prices, color=C_BLUE, lw=2.6, zorder=4)
ax.fill_between(months, prices, 0, color="#eaf2fa", zorder=1)

for m, p, txt in BUYS:
    ax.plot([m], [p], marker="o", ms=10, mfc=C_ORANGE, mec="white",
            mew=1.6, zorder=7)
    label(ax, m + 0.45, p + 3.05, txt, fontsize=11.0, color="#222222",
          ha="left", va="center")

ax.axhline(COST_A, color=C_RED, lw=1.9, ls="--", zorder=3)
ax.axhline(COST_B, color=C_GREEN, lw=1.9, ls="--", zorder=3)
label(ax, 24.6, COST_A, "一次性买入的成本 20.00 元", fontsize=11.3,
      color=C_RED, ha="left", weight="bold")
label(ax, 24.6, COST_B, "分三批的平均成本 15.38 元", fontsize=11.3,
      color=C_GREEN, ha="left", weight="bold")

label(ax, 13.5, 25.4,
      "同一段时间、同样 5.92 万元：分批买入把每股成本压低了 4.62 元",
      fontsize=12.0, color=C_GREEN, weight="bold", ha="center")

ax.set_xlim(-0.6, 36)
ax.set_ylim(0, 28)
ax.set_xticks([0, 4, 8, 12, 16, 20, 24])
ax.set_xticklabels(["第 0 月", "第 4 月", "第 8 月", "第 12 月",
                    "第 16 月", "第 20 月", "第 24 月"])
style_axes(ax, xlabel="时间（示意）", ylabel="股价（元）",
           title="分批买入：不是买得更准，而是买得更便宜", grid_axis="y")

fig.text(0.085, 0.03,
         "价格为简化示意数字，用于演示「以低于平均价格买进」的算术效果，不是任何真实股票的走势。",
         fontsize=9.5, color=C_GRAY, ha="left", va="center")

save(fig, "w12d2_batch_buy_avg.png")
print(f"  分批平均成本 {COST_B:.4f} 元；与一次性买入相差 {COST_A - COST_B:.4f} 元")
print(f"  股价回到 20 元时：A 先生 {2960 * (20 - COST_A):,.0f} 元；"
      f"B 先生 {3850 * (20 - COST_B):,.0f} 元")
