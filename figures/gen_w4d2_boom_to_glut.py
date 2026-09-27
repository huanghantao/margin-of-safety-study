"""W4 第 2 章图：金融创新从繁荣到过剩（原书 p41 的自证预言）。

上图：华尔街创造的「供应」与投资者的「需求」两条曲线，供应最终超过需求；
下图：价格在供应还没超过需求时就已经见顶——因为价格反映的是预期。
横轴为时间（示意），纵轴为指数。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, plain, label, style_axes, vline,
                             C_GREEN, C_RED, C_ORANGE, C_GRAY, C_BLUE)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
demand = [1.0, 2.0, 3.4, 5.0, 6.6, 8.0, 9.2, 8.6, 6.8, 4.2, 1.8]
supply = [0.3, 0.8, 1.6, 2.8, 4.4, 6.6, 8.8, 9.8, 8.9, 6.0, 2.6]
price = [1.0, 2.1, 3.6, 5.2, 7.0, 8.6, 9.7, 8.4, 5.9, 3.4, 1.3]

fig, axes = plt.subplots(2, 1, figsize=(11.8, 8.6), sharex=True,
                         gridspec_kw={"height_ratios": [1.05, 1.0]})
fig.subplots_adjust(top=0.87, bottom=0.10, left=0.09, right=0.97, hspace=0.30)

# ── 三个阶段背景带（两幅图共用同一套色带）──────────────────────
BANDS = [(0, 3.0, "#f4f9f4"), (3.0, 7.5, "#fdf6ec"), (7.5, 10, "#fbecec")]
NAMES = ["① 萌芽：没人相信", "② 狂热：人人想要", "③ 出清：供应过剩"]

for ax in axes:
    for (x0, x1, c) in BANDS:
        ax.axvspan(x0, x1, color=c, zorder=0)

# ══════════════════════════════════════════════════════════════════
#  上：供应 vs 需求
# ══════════════════════════════════════════════════════════════════
ax = axes[0]
ax.plot(x, demand, color=C_GREEN, lw=2.6, marker="o", ms=5, zorder=4,
        label="投资者的需求")
ax.plot(x, supply, color=C_RED, lw=2.6, marker="s", ms=5, zorder=4,
        label="华尔街创造的供应")
vline(ax, 7.45, 0, 10.6, color=C_GRAY, lw=1.4, ls="--", zorder=2)

label(ax, 2.35, 10.55, "投资者的需求", color=C_GREEN, fontsize=12,
      weight="bold")
label(ax, 5.55, 4.35, "华尔街创造的供应", color=C_RED, fontsize=12,
      weight="bold")
label(ax, 7.45, 11.55, "供过于求的临界点", color="#222222", fontsize=11.5,
      weight="bold")

ax.set_ylim(0, 12.6)
ax.set_xlim(-0.15, 10.15)
style_axes(ax, ylabel="指数（示意）", title="", grid_axis="y")

# ══════════════════════════════════════════════════════════════════
#  下：价格
# ══════════════════════════════════════════════════════════════════
ax = axes[1]
ax.plot(x, price, color=C_ORANGE, lw=2.8, marker="o", ms=5, zorder=4)
vline(ax, 7.45, 0, 10.6, color=C_GRAY, lw=1.4, ls="--", zorder=2)
vline(ax, 6.0, 0, 10.6, color=C_BLUE, lw=1.4, ls=":", zorder=2)

label(ax, 6.0, 11.55, "价格见顶", color=C_BLUE, fontsize=11.5, weight="bold")
label(ax, 2.30, 8.30, "价格跟着热情走", color=C_ORANGE, fontsize=12,
      weight="bold")
label(ax, 8.55, 9.10, "价格先跌，供应才过剩——\n价格反映的是预期，不是现实",
      color="#222222", fontsize=10.5)

ax.set_ylim(0, 12.6)
style_axes(ax, xlabel="时间（示意）", ylabel="价格指数（示意）",
           title="", grid_axis="y")
ax.set_xticks(x)
ax.set_xticklabels([str(i) for i in x], fontsize=10)

# ── 阶段名放在最下方，避免压线 ────────────────────────────────
for (x0, x1, _), nm in zip(BANDS, NAMES):
    plain(ax, (x0 + x1) / 2, -3.05, nm, fontsize=11, color="#444444",
          weight="bold", va="top")

fig.suptitle("华尔街会把任何一种新东西的供应，一直做到过剩为止",
             fontsize=14.5, weight="bold", y=0.965)
plain(axes[0], -0.70, 13.15, "原书 p41：只要买家推高价格，热情就能维持；"
                             "价格一触顶，买家立刻变成卖家。",
      fontsize=10.5, color=C_GRAY, ha="left", va="center")

save(fig, "w4d2_boom_to_glut.png")
