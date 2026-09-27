"""Week 11 第 0 章配图：普通 IPO 与储蓄机构转制，新股东到底拿到了什么。

统一参照点只有一条：**买入之后，每股对应的账面净资产**。
两组柱子都用这一个参照点，不做任何口径切换。

  普通 IPO（原书 p196 的 XYZ 公司算例）：
      公众付 11 美元/股，发行后每股账面净资产 6 美元  -> 被稀释 5 美元
  储蓄机构转制（原书 p196 的算例）：
      新股东付 10 美元/股，发行后每股账面净资产 20 美元 -> 白得 10 美元

图中数字全部来自原书 p196 的两个算例，不是编造的。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, hline, vline, plain, money_bar,
                             label, C_GREEN, C_GOLD, C_GRAY, C_RED)

fig, ax = fig_ax(11.8, 7.4, xlim=(0, 10), ylim=(-6.2, 30))

# ── 纵轴：美元/股 ───────────────────────────────────────────────────
vline(ax, 0.62, 0, 24.6, color="#333333", lw=1.4)
for y in (0, 5, 10, 15, 20):
    hline(ax, y, 0.44, 0.62, color="#333333", lw=1.2)
    plain(ax, 0.36, y, f"{y}", fontsize=10.5, ha="right", va="center")
plain(ax, 0.36, 25.6, "美元/股", fontsize=10.5, ha="right", va="center")

# ── 两组标题 ────────────────────────────────────────────────────────
plain(ax, 2.60, 28.6, "普通 IPO：XYZ 公司", fontsize=13, weight="bold")
plain(ax, 7.00, 28.6, "储蓄机构转制", fontsize=13, weight="bold")

# ── A 组：普通 IPO ──────────────────────────────────────────────────
money_bar(ax, 1.45, 0, 1.15, 11, "你付出\n11 美元", fc=C_GOLD, fontsize=11.5)
money_bar(ax, 3.00, 0, 1.15, 6, "你得到\n6 美元", fc="#9ecfa5", ec=C_GREEN,
          fontsize=11.5)
plain(ax, 2.60, -1.0,
      "你付的是 11 美元，\n拿到的账面净资产只有 6 美元：\n"
      "每股被稀释 5 美元（占买入价的 45%）",
      fontsize=11, va="top", color=C_RED)

# ── B 组：储蓄机构转制 ──────────────────────────────────────────────
money_bar(ax, 5.85, 0, 1.15, 10, "你付出\n10 美元", fc=C_GOLD, fontsize=11.5)
money_bar(ax, 7.40, 0, 1.15, 20, "你得到\n20 美元", fc="#9ecfa5", ec=C_GREEN,
          fontsize=11.5)
plain(ax, 7.00, -1.0,
      "你付的是 10 美元，\n拿到的账面净资产有 20 美元：\n"
      "多出来的 10 美元是机构原有的钱",
      fontsize=11, va="top", color=C_GREEN)

# ── 两组之间的分隔竖虚线 ────────────────────────────────────────────
vline(ax, 4.85, 0, 27.2, color=C_GRAY, lw=1.1, ls=":")

save(fig, "w11d0_mutual_to_stock.png")
