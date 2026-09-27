"""Week 8 第 1 章配图：绝对表现 vs 相对表现。

左：两年里「我的组合」与「指数」的涨跌幅（简化示意数字，真实坐标柱状图）。
右：两块记分牌对同一件事给出相反结论。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

from figures._common import (fig_multi, save, box, plain, label, style_axes,
                             hline, C_BLUE, C_ORANGE, C_GRAY, F_BLUE, F_ORANGE)


fig, axes = fig_multi(1, 2, width=13.4, height=6.6)
axL, axR = axes

# ── 左图：真实的柱状图 ──────────────────────────────────────────────
axL.set_axis_on()
groups = ["第 1 年", "第 2 年", "两年累计"]
mine = [-20.0, 20.0, -4.0]
index = [-25.0, 35.0, 1.25]

width, gap = 0.30, 0.05
for i, (a, b) in enumerate(zip(mine, index)):
    xa = i - width - gap / 2
    xb = i + gap / 2
    axL.bar([xa], [a], width=width, color=C_BLUE, zorder=3)
    axL.bar([xb], [b], width=width, color=C_ORANGE, zorder=3)
    va_a, off_a = ("bottom", 1.2) if a >= 0 else ("top", -1.2)
    va_b, off_b = ("bottom", 1.2) if b >= 0 else ("top", -1.2)
    plain(axL, xa, a + off_a, f"{a:+.2f}%".replace(".00", ""), fontsize=11,
          color=C_BLUE, weight="bold", ha="center", va=va_a)
    plain(axL, xb, b + off_b, f"{b:+.2f}%".replace(".00", ""), fontsize=11,
          color=C_ORANGE, weight="bold", ha="center", va=va_b)

hline(axL, 0, -0.6, 2.6, color="#444444", lw=1.3, zorder=4)
axL.set_xlim(-0.6, 2.6)
axL.set_ylim(-38, 48)
axL.set_xticks([0, 1, 2])
axL.set_xticklabels(groups, fontsize=12)
axL.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=C_BLUE),
                    plt.Rectangle((0, 0), 1, 1, color=C_ORANGE)],
           labels=["我的组合", "指数（沪深 300 示意）"],
           loc="upper left", fontsize=10.5, frameon=False)
label(axL, 2.0, 30, "第 1 年：跑赢 5 个百分点，\n但自己的钱亏掉了两成",
      fontsize=11, color="#333333")
style_axes(axL, ylabel="当年涨跌幅", title="两块记分牌，记的是同一件事")

# ── 右图：两块记分牌 ────────────────────────────────────────────────
plain(axR, 5, 9.7, "你该看哪一块？", fontsize=13.5, weight="bold")

box(axR, 0.5, 6.3, 9.0, 2.5,
    "相对表现记分牌（跟别人比）\n\n你 -20%，指数 -25%\n→ 跑赢 5 个百分点，掌声响起来",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=11.5)

plain(axR, 5, 5.5, "同一件事，两块记分牌结论相反", fontsize=12, color=C_GRAY)

box(axR, 0.5, 2.0, 9.0, 2.5,
    "绝对表现记分牌（跟自己的钱包比）\n\n100 元变成 80 元\n→ 少了 20 元，超市不认「跑赢」",
    fc=F_BLUE, ec=C_BLUE, fontsize=11.5)

label(axR, 5, 0.9, "你无法用相对回报付款。", fontsize=12.5,
      color=C_BLUE, weight="bold")

save(fig, "w8d1_absolute_vs_relative.png")
