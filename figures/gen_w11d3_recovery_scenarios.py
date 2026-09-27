"""Week 11 第 3 章核心配图（★）：不同结局的加权回收值。

一根堆叠条 = 一种假设下，每 100 元面值债券的"期望回收值"。
每一段的**高度**就是"回收金额 乘 该结局的概率"（加权贡献），
所以整根柱子的**顶端**正好落在加权期望回收值上——几何位置自己说话。

**以下全部是简化示意数字，用于教学，不是任何一只真实债券的报价。**

  基准假设：15% 乘 8 + 25% 乘 35 + 30% 乘 62 + 20% 乘 100 + 10% 乘 0
            = 1.20 + 8.75 + 18.60 + 20.00 + 0 = 48.55 元
  悲观假设：20% 乘 8 + 25% 乘 35 + 20% 乘 62 + 10% 乘 100 + 25% 乘 0
            = 1.60 + 8.75 + 12.40 + 10.00 + 0 = 32.75 元
  市价：32 元
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, hline,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY)

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

MARKET = 32.0

# (名称, 每 100 元面值的回收金额, 基准概率, 悲观概率, 颜色)
SCEN = [
    ("① 清算", 8, 0.15, 0.20, C_RED),
    ("② 重整（低）", 35, 0.25, 0.25, C_ORANGE),
    ("③ 重整（高）", 62, 0.30, 0.20, C_BLUE),
    ("④ 被收购", 100, 0.20, 0.10, C_GREEN),
    ("⑤ 彻底归零", 0, 0.10, 0.25, C_GRAY),
]

BAR_X = 1.10
BAR_W = 2.00
BAR2_X = 7.60
LABEL_X = 3.60
LABEL2_X = 10.10

fig, ax = plt.subplots(figsize=(14.0, 7.8))

totals = []
for k, bx in enumerate((BAR_X, BAR2_X)):
    lx = LABEL_X if k == 0 else LABEL2_X
    base = 0.0
    for name, rec, p_base, p_bad, color in SCEN:
        p = p_base if k == 0 else p_bad
        h = rec * p
        if h > 0:
            ax.add_patch(Rectangle((bx, base), BAR_W, h, fc=color, alpha=0.88,
                                   ec="white", lw=1.6, zorder=3))
        if h >= 5.0:
            plain(ax, bx + BAR_W / 2, base + h / 2, f"{h:.2f}", fontsize=11,
                  color="white", weight="bold", zorder=7,
                  ha="center", va="center")
        ylab = base + h / 2 if h >= 1.0 else base + 2.2
        label(ax, lx, ylab,
              f"{name}　概率 {int(p * 100)}%\n"
              f"{rec} 乘 {int(p * 100)}% = {h:.2f} 元",
              fontsize=10, ha="left", va="center", zorder=7)
        base += h
    totals.append(base)
    ax.plot([bx - 0.24, bx + BAR_W + 0.24], [base, base],
            color="#111111", lw=1.6, zorder=5)

# ── 市价线 ──────────────────────────────────────────────────────────
hline(ax, MARKET, -3.60, 17.20, color=C_RED, lw=2.0, ls="--", zorder=4)
label(ax, -3.45, MARKET + 1.8, "市价 32 元", fontsize=12, color=C_RED,
      ha="left", weight="bold", zorder=7)

# ── 柱顶的期望回收值 ────────────────────────────────────────────────
label(ax, BAR_X + BAR_W / 2, totals[0] + 4.6,
      f"加权期望回收值\n{totals[0]:.2f} 元", fontsize=12, color=C_GREEN,
      weight="bold", zorder=7)
label(ax, BAR2_X + BAR_W / 2, totals[1] + 8.0,
      f"加权期望回收值\n{totals[1]:.2f} 元", fontsize=12, color=C_RED,
      weight="bold", zorder=7)

# ── 右上角：安全边际的账 ────────────────────────────────────────────
label(ax, 13.00, 50.0,
      f"基准假设：{totals[0]:.2f} - 32 = {totals[0] - MARKET:.2f} 元\n"
      f"安全边际 = {totals[0] - MARKET:.2f} 除以 32\n"
      f"　　　　　= {(totals[0] - MARKET) / MARKET * 100:.1f}%\n\n"
      f"悲观假设：{totals[1]:.2f} - 32 = {totals[1] - MARKET:.2f} 元\n"
      f"安全边际 = {(totals[1] - MARKET) / MARKET * 100:.1f}%\n"
      f"几乎等于没有",
      fontsize=10.5, color="#222222", ha="left", va="center", zorder=7)

plain(ax, BAR_X + BAR_W / 2, -4.4, "基准假设", fontsize=12.5,
      weight="bold", ha="center", va="center")
plain(ax, BAR2_X + BAR_W / 2, -4.4, "悲观假设", fontsize=12.5,
      weight="bold", ha="center", va="center")

style_axes(ax, ylabel="每 100 元面值债券的金额（元）",
           title="把每种结局的回收值按概率加权，柱顶就是期望回收值",
           grid_axis="y")
ax.set_xlim(-3.8, 17.5)
ax.set_ylim(-6.6, 62.0)
ax.set_xticks([])

fig.text(0.5, -0.015,
         "柱子每一段的高度 = 回收金额 乘 该结局的概率；段与段相加，"
         "顶端就是期望回收值。⑤ 彻底归零的加权贡献是 0 元，所以它没有高度。",
         ha="center", fontsize=11, color=C_GRAY)

save(fig, "w11d3_recovery_scenarios.png")
