"""W5 第 4 章配图：留一点现金的力量（真实坐标，两条资产曲线）。

20 万元本金，股价从 10 元跌到 6 元再涨回 10 元。
A：20 万元全部买入；B：只买 16 万元、留 4 万元现金，并在 6 元时把现金投进去。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, label, plain, style_axes,
                             C_BLUE, C_GREEN, C_GRAY, C_ORANGE, C_DARK)

fig, ax = plt.subplots(figsize=(11.5, 6.9))

price = [10, 9, 8, 7, 6, 7, 8, 9, 10]
steps = list(range(9))

# A：20 万元全部买入（2 万份）
a_assets = [20 * p / 10 for p in price]
# B：16 万元买入（1.6 万份）+ 4 万元现金；第 4 阶段在 6 元把 4 万元投进去
b_assets = [16 * p / 10 + 4 for p in price[:5]]
shares_b = 16000 + 40000 / 6          # 份数
b_assets += [shares_b * p / 10000 for p in price[5:]]   # 份数 x 股价 = 万元

ax.plot(steps, a_assets, color=C_ORANGE, lw=2.8, marker="o", ms=5.5, zorder=4,
        label="A：20 万元全部买入（满仓）")
ax.plot(steps, b_assets, color=C_GREEN, lw=2.8, marker="o", ms=5.5, zorder=5,
        label="B：只买 16 万元，留 4 万元现金")

ax.plot([4], [13.6], marker="o", ms=14, mfc="none", mec=C_GREEN, mew=2.8,
        zorder=6)
ax.plot([8], [22.67], marker="o", ms=14, mfc="none", mec=C_GREEN, mew=2.8,
        zorder=6)
ax.plot([4], [12.0], marker="o", ms=14, mfc="none", mec=C_ORANGE, mew=2.8,
        zorder=6)

label(ax, 5.15, 10.1,
      "股价 6 元：满仓的 A 剩 12.0 万，B 有 13.6 万\n"
      "B 把 4 万元现金在 6 元买进去，成本被摊低",
      color=C_GREEN, fontsize=11.5, ha="left", va="center")
label(ax, 8.0, 25.6,
      "股价涨回 10 元：\nA 回到 20.0 万，B 变成 22.7 万",
      color=C_DARK, fontsize=11.5, ha="right", va="center", weight="bold")

ax.set_xlim(-0.35, 8.7)
ax.set_ylim(8, 27)
ax.set_xticks(steps)
ax.set_xticklabels([f"{p} 元" for p in price])
style_axes(ax, xlabel="股价路径：先跌 40%，再涨回原点（横轴按时间顺序）",
           ylabel="你的总资产（万元）",
           title="留 20% 现金的人：跌得少一点，回来得快一点",
           grid_axis="y")
ax.legend(loc="lower left", fontsize=11, frameon=True)
plain(ax, 8.65, 6.2, "数字为简化示意，用于教学", fontsize=10.5, color=C_GRAY,
      ha="right", va="center")

save(fig, "w5d4_waiting_power.png")
