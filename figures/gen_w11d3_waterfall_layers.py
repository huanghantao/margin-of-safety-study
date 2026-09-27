"""Week 11 第 3 章配图之二：资本结构的分层瀑布与"支点证券"。

把企业的总索取权按等级从低到高堆成一根柱子（合计 100 元面值），
再从下往上"切"企业价值：切到哪一级没钱了，那一级以下就归零。

  有担保债务 30 + 高级无担保 25 + 次级债券 20 + 优先股 10 + 普通股 15 = 100
  企业价值 68 元时：30 + 25 + 13 + 0 + 0 = 68，次级债券拿回 13 比 20 = 65%
  企业价值 88 元时：30 + 25 + 20 + 10 + 3 = 88，普通股拿回 3 比 15 = 20%

**全部是简化示意数字，用于教学。**
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, hline,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             C_TEAL)

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BAR_X, BAR_W = 1.10, 2.40

LAYERS = [
    ("有担保债务", 30, C_BLUE),
    ("高级无担保债务", 25, C_TEAL),
    ("次级债券", 20, C_GOLD),
    ("优先股", 10, C_ORANGE),
    ("普通股", 15, C_RED),
]

NOTES = [
    "面值 30 元\n两种情形都全额拿回",
    "面值 25 元\n两种情形都全额拿回",
    "面值 20 元　← 支点证券\n68 元时拿回 13 元（65%）\n88 元时拿满 20 元（100%）",
    "面值 10 元\n68 元时归零；88 元时拿满",
    "面值 15 元\n68 元时归零；88 元时拿回 3 元（20%）",
]

VALUE_LOW, VALUE_HIGH = 68, 88

fig, ax = plt.subplots(figsize=(13.6, 8.2))

base = 0.0
for (name, face, color), note in zip(LAYERS, NOTES):
    ax.add_patch(Rectangle((BAR_X, base), BAR_W, face, fc=color, alpha=0.88,
                           ec="white", lw=1.8, zorder=3))
    ymid = base + face / 2
    if name == "次级债券":
        ymid -= 2.5
    if name == "普通股":
        ymid = base + face / 2 + 1.5
    plain(ax, BAR_X + BAR_W / 2, ymid, f"{name}\n{face} 元",
          fontsize=11.5, color="white", weight="bold", zorder=7,
          ha="center", va="center")
    if name == "次级债券":
        ymid -= 2.0
    label(ax, BAR_X + BAR_W + 0.55, ymid, note, fontsize=10.5, ha="left",
          va="center", zorder=7)
    base += face

# ── 两条企业价值线 ──────────────────────────────────────────────────
for y, color, txt in ((VALUE_LOW, C_RED, "企业价值偏低：68 元"),
                      (VALUE_HIGH, C_GREEN, "企业价值偏高：88 元")):
    hline(ax, y, -0.60, 15.60, color=color, lw=2.0, ls="--", zorder=4)

label(ax, 15.40, VALUE_LOW - 3.2, "企业价值偏低：68 元", fontsize=11.5,
      color=C_RED, ha="right", weight="bold", zorder=7)
label(ax, 15.40, VALUE_HIGH + 3.2, "企业价值偏高：88 元", fontsize=11.5,
      color=C_GREEN, ha="right", weight="bold", zorder=7)

plain(ax, -0.45, 104.5,
      "从最上面一级往下切，切到哪一级没钱了，那一级以下就归零",
      fontsize=11.5, ha="left", color="#333333", va="center")

style_axes(ax, ylabel="元（企业的总索取权面值合计 100 元，简化示意）",
           title="同一家公司，价值高一点低一点，各层拿到的东西完全不同",
           grid_axis="y")
ax.set_xlim(-0.8, 16.0)
ax.set_ylim(0, 112)
ax.set_xticks([])
ax.set_yticks([0, 20, 40, 60, 80, 100])

fig.text(0.5, -0.015,
         "馅饼只有 68 元（或 88 元），等着分的人却要 100 元。"
         "夹在「能不能全额拿回」之间的那一级，就叫支点证券（原书 p217–p218）："
         "价值往上走它受益最大，往下走它受伤最重。",
         ha="center", fontsize=10.5, color=C_GRAY)

save(fig, "w11d3_waterfall_layers.png")
