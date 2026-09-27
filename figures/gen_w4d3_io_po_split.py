"""W4 第 3 章图：IOs 与 POs——把一笔房贷剪成两半。

左：结构图。一笔房贷的还款被剪成「利息流」和「本金流」，分别打包卖给不同的人；
右：真实坐标柱状图。利率上升 1 个百分点时，完整证券、IO、PO 的反应完全不同。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, box, arrow, plain, label, style_axes,
                             C_BLUE, C_GREEN, C_GRAY, C_RED, C_ORANGE,
                             F_BLUE, F_GREEN, F_RED, F_GRAY)

fig, axes = plt.subplots(1, 2, figsize=(13.8, 7.2),
                         gridspec_kw={"width_ratios": [1.22, 1.0]})
fig.subplots_adjust(top=0.84, bottom=0.16, left=0.04, right=0.97, wspace=0.14)

# ══════════════════════════════════════════════════════════════════
#  左：结构图
# ══════════════════════════════════════════════════════════════════
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

plain(ax, 5.0, 9.70, "一笔房贷的还款，被剪成两股现金流",
      fontsize=13.5, weight="bold", color="#222222")

box(ax, 0.10, 3.95, 3.05, 2.55,
    "一笔 30 年期房贷\n\n借款人每月还款\n（一部分是利息，\n一部分是本金）",
    fc=F_BLUE, ec=C_BLUE, fontsize=10.5)

box(ax, 4.60, 5.70, 5.30, 1.85,
    "IO 证券（Interest Only，只收利息）\n\n卖给：担心利率上升、想对冲的机构",
    fc=F_GREEN, ec=C_GREEN, fontsize=11)
box(ax, 4.60, 2.10, 5.30, 1.85,
    "PO 证券（Principal Only，只收本金）\n\n卖给：赌利率下降、想要高波动的人",
    fc=F_RED, ec=C_RED, fontsize=11)

arrow(ax, (3.25, 5.90), (4.45, 6.55), color=C_GREEN, lw=2.0)
arrow(ax, (3.25, 4.55), (4.45, 4.00), color=C_RED, lw=2.0)
label(ax, 3.85, 7.35, "剪成两股", color="#222222", fontsize=11.5,
      weight="bold")

box(ax, 0.10, 0.35, 9.80, 1.25,
    "切开容易，合回去难：想把两半再拼回一张完整房贷，\n"
    "得两份持有人同时点头——而他们没有理由点头。",
    fc="#f7f7f7", ec=C_GRAY, fontsize=11.5, weight="bold")

# ══════════════════════════════════════════════════════════════════
#  右：利率上升 1 个百分点的反应
# ══════════════════════════════════════════════════════════════════
ax = axes[1]
names = ["完整的抵押\n贷款证券", "IO\n（只收利息）", "PO\n（只收本金）"]
vals = [-6, 8, -16]
colors = [C_BLUE, C_GREEN, C_RED]

ax.bar(range(3), vals, width=0.50, color=colors, zorder=3)
for i, v in enumerate(vals):
    if v >= 0:
        plain(ax, i, v + 0.9, f"+{v}%", fontsize=13, color=colors[i],
              weight="bold", va="bottom", ha="center")
    else:
        plain(ax, i, v - 0.9, f"{v}%", fontsize=13, color=colors[i],
              weight="bold", va="top", ha="center")

ax.axhline(0, color="#444444", lw=1.6, zorder=4)
ax.set_xticks(range(3))
ax.set_xticklabels(names, fontsize=11)
ax.set_ylim(-23, 15)
ax.set_xlim(-0.64, 2.64)
style_axes(ax, ylabel="价格变化（%）",
           title="利率上升 1 个百分点，三种证券各走各的", grid_axis="y")
plain(ax, -0.62, -27.6,
      "以下为简化示意数字，用于说明「方向相反」这件事，",
      fontsize=10, color=C_GRAY, ha="left", va="top")
plain(ax, -0.62, -29.4,
      "不是真实市场报价。IO 涨是因为提前还款变慢、利息流更长。",
      fontsize=10, color=C_GRAY, ha="left", va="top")

save(fig, "w4d3_io_po_split.png")
