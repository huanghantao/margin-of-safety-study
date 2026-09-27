"""Week 9 第 5 章配图一（Esco 案例）：卡拉曼的逐年折现，钱都堆在哪一段。

Esco 电子公司 1990 年 10 月从爱默生电器公司分拆出来，股价 3 美元。
在「业绩毫无改善」的假设下，每股自由现金流是：
  第 1~5 年  每年 0.45 美元（商誉摊销带来的非现金自由现金流）
  第 6 年起  每年 0.90 美元（1996 年不再向爱默生支付担保费，多出 0.45 美元）
用 12% 一年一年折回今天：
  第 1~5 年分别 0.40、0.36、0.32、0.29、0.26，合计 1.62 美元；
  第 6 年以后那一整段，在第 5 年末值 0.90 除以 0.12 = 7.50 美元，
  再除以 1.7623 折回今天 = 4.26 美元。
合计 5.88 美元。原书 p154 给的数字是 5.87 美元。

柱子高度全部是真实坐标 —— 一眼就能看出：
72% 的价值压在第 6 年以后那个「永续」假设上。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (save, plain, label, hline,
                             C_BLUE, C_GOLD, C_RED, C_GREEN, style_axes)

v12 = [0.45, 0.45, 0.45, 0.45, 0.45]
mult = [1.0]
for _ in range(5):
    mult.append(round(mult[-1] * 1.12, 6))

pv = [round(v / m, 4) for v, m in zip(v12, mult[1:])]
tail = round(7.50 / mult[5], 4)          # 4.2563
total = round(sum(pv) + tail, 2)         # 5.878

fig, ax = plt.subplots(figsize=(12, 6.4))

xs = [0, 1, 2, 3, 4, 7]
heights = pv + [tail]
colors = [C_BLUE] * 5 + [C_GOLD]
ax.bar(xs, heights, width=0.62, color=colors, zorder=3)

for x, h in zip(xs, heights):
    plain(ax, x, h + 0.09, f"{h:.2f}", fontsize=11, weight="bold",
          color="#222222", va="bottom")

ax.set_xlim(-0.85, 9.6)
ax.set_ylim(0, 6.45)
ax.set_xticks(xs)
ax.set_xticklabels(["第 1 年", "第 2 年", "第 3 年", "第 4 年", "第 5 年",
                    "第 6 年起\n（永远）"], fontsize=11.5)

hline(ax, total, -0.85, 9.6, color=C_GREEN, lw=1.7, ls=(0, (5, 3)), zorder=1)
label(ax, 9.45, total + 0.08, f"加起来 {total:.2f} 美元（原书给的是 5.87）",
      fontsize=11, color=C_GREEN, ha="right")

label(ax, 2.2, 1.05,
      "前 5 年：每年 0.45 美元，折回今天只有 1.62 美元，占 28%",
      fontsize=11.5, color=C_BLUE)

label(ax, 7.0, 4.95, "第 6 年以后那一段，占了 72%",
      fontsize=11.5, color=C_GOLD)

style_axes(ax, xlabel="这笔钱在第几年到手（贴现率 12%）",
           ylabel="相当于今天多少钱（美元/股）",
           title="Esco 电子公司：每股现值 5.88 美元里，72% 来自第 6 年以后")

save(fig, "w9d5_esco_discount_bars.png")
