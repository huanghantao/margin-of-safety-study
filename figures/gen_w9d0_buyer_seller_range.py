"""Week 9 第 0 章第二张图：买卖双方各有一个价值区间，成交价落在中间。

原书 p134 的意思：每一项被买卖的资产都有一个受限于买家价值和卖家价值的
价值范围，实际的交易价格处在买卖双方的价值预期中间。这里把三段落在一根
真实坐标轴上：卖方能接受的最低价区间 18~22 元，买方愿意出的最高价区间
28~33 元，中间那段 22~28 元才是成交价可能出现的地方。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, label, plain, brace, vline,
                             C_BLUE, C_GREEN, C_GOLD, C_GRAY,
                             F_BLUE, F_GREEN, F_GOLD, style_axes)

fig, ax = plt.subplots(figsize=(12.5, 5.6))

ax.set_xlim(0, 40)
ax.set_ylim(0, 10)

Y0, H = 5.6, 1.7

# ── 三段：卖方要价区 / 成交价可落区 / 买方出价区 ────────────────────
ax.add_patch(plt.Rectangle((18, Y0), 4, H, fc=F_BLUE, ec=C_BLUE, lw=1.8,
                           zorder=3))
ax.add_patch(plt.Rectangle((22, Y0), 6, H, fc=F_GREEN, ec=C_GREEN, lw=2.0,
                           ls="--", zorder=3))
ax.add_patch(plt.Rectangle((28, Y0), 5, H, fc=F_GOLD, ec=C_GOLD, lw=1.8,
                           zorder=3))

plain(ax, 20.0, Y0 + H / 2, "卖方要价", fontsize=12, color=C_BLUE,
      weight="bold")
plain(ax, 25.0, Y0 + H / 2, "可能成交", fontsize=12, color=C_GREEN,
      weight="bold")
plain(ax, 30.5, Y0 + H / 2, "买方出价", fontsize=12, color="#8a6d1f",
      weight="bold")

plain(ax, 20.0, Y0 + H + 0.5, "18 ~ 22 元\n低于这个价，卖方不卖",
      fontsize=11, color=C_BLUE)
plain(ax, 25.0, Y0 + H + 0.5, "22 ~ 28 元", fontsize=11, color=C_GREEN)
plain(ax, 30.5, Y0 + H + 0.5, "28 ~ 33 元\n高于这个价，买方不买",
      fontsize=11, color="#8a6d1f")

# ── 举例：成交在 25 元 ────────────────────────────────────────────
vline(ax, 25, Y0 - 0.15, Y0 - 1.15, color=C_GREEN, lw=2.0, zorder=4)
plain(ax, 25, Y0 - 1.6, "举例：成交在 25 元", fontsize=11, color=C_GREEN)

# ── 下面那道空隙 ─────────────────────────────────────────────────
brace(ax, 22, 28, 2.3, "成交价只能落在这 6 元的空隙里", color=C_GREEN,
      fontsize=11.5, depth=0.3, text_offset=0.35)

plain(ax, 0.6, 8.6, "同一家公司，两个人心里两个价", fontsize=13,
      weight="bold", ha="left")
plain(ax, 0.6, 7.7,
      "卖方觉得它只值 18~22 元，\n"
      "买方觉得它值 28~33 元。\n\n"
      "两个区间不重叠，生意才谈得成；\n"
      "价格最后落在中间那段空隙里。\n\n"
      "对做投资的人来说，重点是：\n"
      "你要知道自己算的是哪一段，\n"
      "而不是照抄别人的数字。",
      fontsize=10.5, color="#444444", ha="left", va="top")

ax.set_yticks([])
ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35])
style_axes(ax, xlabel="这家公司值多少元（教学示意数字）",
           title="买卖双方各有一段价值区间，成交价落在两段之间的空隙里",
           grid_axis="x")
ax.spines["left"].set_visible(False)

save(fig, "w9d0_buyer_seller_range.png")
