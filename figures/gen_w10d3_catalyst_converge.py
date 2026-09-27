"""Week 10 第 3 章配图（核心）：有没有催化剂，决定「便宜」能不能变成「赚到」。

纵轴只有一根基准：内在价值 100 元（绿色虚线，全程不变）。
两条价格路径都画在同一根纵轴上，单位相同（元）。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, plain, arrow, style_axes,
                             C_BLUE, C_GREEN, C_GRAY, C_ORANGE,
                             F_BLUE, F_GRAY)

fig, ax = plt.subplots(figsize=(12.8, 7.0))

m = [0, 4, 8, 12, 16, 18, 19, 22, 26, 30, 36]
with_cat = [60, 58, 62, 59, 63, 63, 96, 99, 100, 100, 100]
no_cat = [60, 55, 62, 57, 64, 60, 58, 63, 59, 62, 61]

# 催化剂事件的位置用色块标出（不画竖线，避免线条互相压）
ax.axvspan(17.6, 18.4, color=F_GRAY, alpha=0.9, zorder=0)

# 全图唯一的基准线：内在价值
ax.plot([0, 36], [100, 100], ls="--", lw=2.2, color=C_GREEN, zorder=2)
ax.plot(m, no_cat, color=C_GRAY, lw=2.6, ls=(0, (6, 3)), zorder=3)
ax.plot(m, with_cat, color=C_BLUE, lw=2.9, zorder=4)

ax.set_xlim(0, 36)
ax.set_ylim(35, 133)
style_axes(ax, xlabel="你买入之后的第几个月", ylabel="每股价格（元）",
           title="同一笔「六折」的买入，有没有催化剂，是两种人生")

label(ax, 9.0, 112, "绿色虚线 = 内在价值 100 元（全图唯一的基准）",
      fontsize=11, color=C_GREEN)
label(ax, 18.0, 125,
      "催化剂发生（要约收购 / 清算分配 / 分拆完成）",
      fontsize=10.5, color=C_ORANGE)
label(ax, 27.0, 88, "有催化剂：事件把价格拉回价值", fontsize=11, color=C_BLUE)
label(ax, 26.0, 48, "没有催化剂：便宜可能一直便宜下去", fontsize=11, color="#555555")

arrow(ax, (34.2, 62.5), (34.2, 98.5), color=C_ORANGE, lw=1.8, style="<|-|>")
label(ax, 33.2, 80, "差 64%", fontsize=11, color=C_ORANGE, ha="right")

save(fig, "w10d3_catalyst_converge.png")
