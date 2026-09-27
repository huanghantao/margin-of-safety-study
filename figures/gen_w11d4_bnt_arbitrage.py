"""Week 11 第 4 章配图之二：新英格兰银行的市场间套利。

数字全部来自原书 p220–p221（不是编造的）：
  高级 + 次级债券票面合计约 7 亿美元，总市值不足 1 亿美元
  普通股总市值 2.5 亿美元——而普通股的权利等级**低于**债券

同一家公司，两个市场讲着两个完全不同的故事，这就是套利的入口。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, hline,
                             money_bar,
                             C_BLUE, C_ORANGE, C_RED, C_GRAY, F_BLUE, F_GRAY)

fig, ax = fig_ax(12.8, 7.8, xlim=(0, 10), ylim=(-5.4, 9.4))

plain(ax, 5.0, 8.9, "新英格兰银行：同一家公司，股和债讲着两个故事（原书 p220）",
      fontsize=13, weight="bold")

# ── 三根柱子 ────────────────────────────────────────────────────────
money_bar(ax, 0.70, 0, 1.60, 7.0, "票面约\n7 亿美元", fc=C_GRAY, ec="#555555",
          fontsize=11)
money_bar(ax, 2.95, 0, 1.60, 1.0, "市值\n不足 1 亿", fc=C_BLUE, fontsize=11,
          text_inside_threshold=1.2)
money_bar(ax, 5.20, 0, 1.60, 2.5, "市值\n2.5 亿美元", fc=C_ORANGE, fontsize=11)

plain(ax, 1.50, -0.60, "高级债券 + 次级债券", fontsize=11, ha="center",
      va="top", weight="bold")
plain(ax, 3.75, -0.60, "这些债券在市场上的\n总市值", fontsize=11,
      ha="center", va="top", weight="bold")
plain(ax, 6.00, -0.60, "普通股", fontsize=11, ha="center", va="top",
      weight="bold")

arrow(ax, (4.85, 1.0), (4.85, 2.5), color=C_RED, lw=2.0, style="<|-|>")
label(ax, 4.85, 3.15, "2.5 倍以上", fontsize=10.5, color=C_RED)

# ── 右侧两个说明框 ──────────────────────────────────────────────────
box(ax, 7.15, 4.80, 2.75, 3.30, "", fc=F_BLUE, ec=C_BLUE)
plain(ax, 8.52, 7.62, "权利等级是这样的", fontsize=11, weight="bold",
      color=C_BLUE)
plain(ax, 8.52, 6.30,
      "债券排在前面：\n还钱先还债券\n股票排在最后：\n还完所有人才轮到它",
      fontsize=10.5, va="center")

box(ax, 7.15, 0.60, 2.75, 3.30, "", fc=F_GRAY, ec=C_GRAY)
plain(ax, 8.52, 3.42, "现实却是反的", fontsize=11, weight="bold")
plain(ax, 8.52, 2.00,
      "排在前面的债券\n市值不到 1 亿\n排在最后的股票\n市值 2.5 亿",
      fontsize=10.5, va="center")

plain(ax, 4.30, -3.00,
      "这两件事不可能同时成立：要么债券太便宜，要么股票太贵。",
      fontsize=12, ha="center", va="center", weight="bold", color=C_RED)
plain(ax, 4.30, -3.95,
      "于是有人买入债券、同时做空等额普通股，把这个差距锁住——"
      "这就是市场间套利。",
      fontsize=11, ha="center", va="center", color="#333333")

save(fig, "w11d4_bnt_arbitrage.png")
