"""Week 10 第 1 章配图：逆向投资者「先错、错很久、最后才对」的价格路径。

纵轴只有一根基准：你估算的内在价值 100 元（绿色虚线，全图不变）。
蓝色实线是同一只股票的市场报价，也画在同一根纵轴上，单位相同（元）。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, plain, arrow, style_axes,
                             C_BLUE, C_GREEN, C_GRAY,
                             F_ORANGE, F_GRAY, F_GREEN)

fig, ax = plt.subplots(figsize=(12.6, 6.8))

months = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
price = [60, 52, 45, 48, 46, 50, 47, 52, 55, 68, 82, 93, 100]

# 三个阶段的底色（用色块，不画竖线，避免线条互相压）
ax.axvspan(0, 8, color=F_ORANGE, alpha=0.85, zorder=0)
ax.axvspan(8, 24, color=F_GRAY, alpha=0.95, zorder=0)
ax.axvspan(24, 36, color=F_GREEN, alpha=0.85, zorder=0)

# 全图唯一的基准线：内在价值
ax.plot([0, 36], [100, 100], ls="--", lw=2.2, color=C_GREEN, zorder=2)
# 市场报价
ax.plot(months, price, color=C_BLUE, lw=2.8, marker="o", ms=5,
        markerfacecolor="white", markeredgewidth=1.8, zorder=3)

ax.set_xlim(0, 36)
ax.set_ylim(0, 138)
style_axes(ax, xlabel="你买入之后的第几个月", ylabel="每股价格（元）",
           title="同一只股票：你算它值 100 元，市场先给你 45 元，三年后才给 100 元")

label(ax, 4.0, 124, "① 第 0–8 个月\n你就是错的", fontsize=11, color="#a05a00")
label(ax, 16.0, 124, "② 第 8–24 个月\n你错了很久", fontsize=11, color="#555555")
label(ax, 30.0, 124, "③ 第 24–36 个月\n你终于对了", fontsize=11, color="#1a7a2a")

label(ax, 24.0, 108, "绿色虚线 = 你估算的内在价值 100 元（全图唯一的基准）",
      fontsize=11, color=C_GREEN)

label(ax, 16.0, 72, "同一时间，别人追捧的热门股在涨——\n你的相对排名很难看，这才是最难熬的地方",
      fontsize=10.5, color="#555555")

plain(ax, 12.5, 22, "蓝色实线 = 市场先生的报价", fontsize=11, color=C_BLUE)
arrow(ax, (13.0, 27), (9.6, 43), color=C_BLUE, lw=1.8)

save(fig, "w10d1_contrarian_timeline.png")
