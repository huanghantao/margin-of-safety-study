"""Week 11 第 4 章配图之一：HBJ 公司的市值怎么在 4 个月里消失的。

数字全部来自原书 p219–p220（不是编造的）：
  1989 年 8 月  债券 + 股票总市值 46 亿美元
  1989 年 9 月  卖出主题公园，税后拿回 10 亿美元
                理论上总市值应降到 36 亿美元
  1990 年 1 月 31 日  实际总市值只有 10 亿美元
  卡拉曼估算的公司价值区间：7 亿 ~ 14 亿美元（p220）
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, style_axes, label, plain, money_bar,
                             C_BLUE, C_GREEN, C_RED, C_GOLD, F_GREEN)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12.4, 7.4))

# 卡拉曼估算的价值区间（画在最底层）
ax.axhspan(7, 14, xmin=0.015, xmax=0.985, fc=F_GREEN, ec=C_GREEN, lw=1.2,
           zorder=1)

BARS = [
    (1.10, 46, "46 亿美元", C_GOLD,
     "1989 年 8 月\n债券加股票的总市值"),
    (4.10, 36, "36 亿美元", C_BLUE,
     "理论值：卖掉主题公园\n拿回 10 亿后应降到"),
    (7.10, 10, "10 亿美元", C_RED,
     "1990 年 1 月 31 日\n实际的总市值"),
]

for x, v, txt, color, cap in BARS:
    money_bar(ax, x, 0, 1.90, v, txt, fc=color, fontsize=12.5)
    plain(ax, x + 0.95, -1.7, cap, fontsize=11, ha="center", va="top",
          color="#333333")

label(ax, 10.40, 10.5,
      "卡拉曼估算的公司价值区间\n7 亿 ~ 14 亿美元（p220）",
      fontsize=11, color=C_GREEN, ha="left", va="center")

label(ax, 10.40, 31.0,
      "4 个月里\n总市值少了 26 亿美元\n跌幅超过 2/3\n\n"
      "少掉的这 26 亿\n不是生意变差变出来的\n是信心破灭跌出来的",
      fontsize=11, color=C_RED, ha="left", va="center")

plain(ax, 5.05, 51.5,
      "HBJ：从垃圾债投资者的宠儿，到人人都在卖",
      fontsize=13.5, ha="center", va="center", weight="bold")

style_axes(ax, ylabel="亿美元", grid_axis="y")
ax.set_xlim(0, 15.2)
ax.set_ylim(-10.0, 56)
ax.set_xticks([])
ax.set_yticks([0, 10, 20, 30, 40, 50])

save(fig, "w11d4_hbj_marketcap.png")
