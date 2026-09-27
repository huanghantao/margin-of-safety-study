"""Week 9 第 0 章核心配图（★）：价值是一个区间，不是一个点。

真实坐标：横轴就是「每股值多少元」（0~40 元）。
同一家公司，三种方法各给一个数（18 / 22 / 27 元），
连起来就是一段价值区间；今天的市场价 12 元落在区间外面。
安全边际永远只拿区间最低的那一端（18 元）去减 —— 全教程统一参照点。

数字是教学示意数字，不是任何一家真实公司的财报。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, plain, brace, vline,
                             C_BLUE, C_ORANGE, C_GREEN, C_GOLD, C_GRAY,
                             F_GREEN, style_axes)

fig, ax = plt.subplots(figsize=(12.5, 6.6))

ax.set_xlim(0, 48)
ax.set_ylim(0, 12)

# ── 价值区间带：18 ~ 27 元 ─────────────────────────────────────────
ax.add_patch(plt.Rectangle((18, 6.0), 9, 1.5, fc=F_GREEN, ec=C_GREEN,
                           lw=1.8, zorder=3))
plain(ax, 22.5, 6.75, "价值区间", fontsize=13, color=C_GREEN, weight="bold")

# 区间两端刻度与说明
for x, txt in ((18, "保守下沿 18 元"), (27, "乐观上沿 27 元")):
    vline(ax, x, 7.5, 8.5, color=C_GREEN, lw=1.6, zorder=4)
    plain(ax, x, 9.3, txt, fontsize=11.5, color=C_GREEN)

# ── 三种方法：落在区间里的三个位置 ────────────────────────────────
methods = [(18, "清算价值法\n18 元", C_GRAY),
           (22, "现值分析法\n22 元", C_BLUE),
           (27, "股市价值法\n27 元", C_GOLD)]
for x, name, c in methods:
    vline(ax, x, 5.2, 6.0, color=c, lw=1.6, ls=":", zorder=2)
    plain(ax, x, 4.6, name, fontsize=11, color=c)

plain(ax, 22.5, 3.6,
      "同一家公司，换一种算法就换一个数字，三个数字连起来才是它的价值",
      fontsize=11.5, color="#444444")

# ── 今天的市场价 12 元 ───────────────────────────────────────────
vline(ax, 12, 4.3, 9.6, color=C_ORANGE, lw=2.4, ls="--", zorder=2)
vline(ax, 12, 0.35, 1.0, color=C_ORANGE, lw=2.4, ls="--", zorder=2)
label(ax, 12.6, 10.7, "今天的市场价 12 元", fontsize=12.5, color=C_ORANGE,
      ha="left", weight="bold")

# ── 安全边际：永远拿保守下沿 18 元去减 ────────────────────────────
brace(ax, 12, 18, 2.1, "安全边际 = 18 - 12 = 6 元", color=C_GREEN,
      fontsize=12, depth=0.3, text_offset=0.35, text_va="bottom")
plain(ax, 31.0, 1.6,
      "基准只有一条：区间最低的那一端。\n正例反例都拿它去减，才不会被自己的乐观骗到。",
      fontsize=11, color=C_GREEN, ha="left")

ax.set_yticks([])
ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35, 40])
style_axes(ax, xlabel="每股值多少元（教学示意数字）",
           title="价值是一个区间：三种方法给出三个数字，价格落在区间之外",
           grid_axis="x")
ax.spines["left"].set_visible(False)

save(fig, "w9d0_value_range_band.png")
