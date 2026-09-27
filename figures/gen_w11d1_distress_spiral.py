"""Week 11 第 1 章配图之一：财政困境的自我强化螺旋。

原书 p204 描述的顺序：现金不够用 -> 短期债务无法再融资 -> 供应商停供 ->
客户停止购买 -> 雇员离开 -> 现金更少。本图把它画成一条向下的阶梯，
每一格都比上一格更难回头。

图里没有任何数值坐标，纯概念图，所以用 0~10 的相对坐标。
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, plain, label,
                             C_RED, C_ORANGE, C_GRAY,
                             F_RED, F_ORANGE, F_GOLD, F_GRAY)

fig, ax = fig_ax(12.4, 8.0, xlim=(0, 10.2), ylim=(0, 11.6))

plain(ax, 5.0, 11.0, "财政困境的螺旋：每一步都让下一步更难",
      fontsize=14.5, weight="bold")

W, H, X = 8.0, 0.98, 0.35
ROWS = [
    (9.50, "① 现金不够用", "账上的钱付不齐利息，也还不清到期的债", F_RED, C_RED),
    (7.75, "② 借不到新钱", "旧的短期债务到期了，却没人愿意再借给它", F_RED, C_RED),
    (6.00, "③ 供应商停止发货", "或者改成一笔一笔收现金，不再给账期", F_ORANGE, C_ORANGE),
    (4.25, "④ 客户不敢再买", "怕以后没人保修、没人供配件，转头找别家", F_ORANGE, C_ORANGE),
    (2.50, "⑤ 员工陆续离开", "去找更安稳、压力更小的工作", F_GOLD, C_GRAY),
    (0.75, "回到 ①：现金比开始时更少", "这一圈走完，下一圈只会更难走", F_GRAY, C_GRAY),
]

for y, title, sub, fc, ec in ROWS:
    box(ax, X, y, W, H, "", fc=fc, ec=ec)
    plain(ax, X + 0.40, y + H / 2, title, fontsize=12.5, ha="left",
          va="center", weight="bold")
    plain(ax, X + 4.15, y + H / 2, sub, fontsize=11, ha="left", va="center",
          color="#444444")

for i in range(len(ROWS) - 1):
    y_top = ROWS[i][0]
    y_bot = ROWS[i + 1][0] + H
    arrow(ax, (X + W / 2, y_top), (X + W / 2, y_bot), color=C_RED, lw=2.0)

label(ax, 9.35, 5.0,
      "每一格都在\n消耗企业的\n长期价值：\n\n"
      "供应商关系、\n客户信任、\n熟练员工，\n\n都不是钱\n能马上买回来的",
      fontsize=10.5, color=C_RED, ha="center", va="center")

plain(ax, 4.35, 0.18,
      "同一条螺旋，转得快还是转得慢，取决于这家企业靠什么活着（原书 p204）",
      fontsize=11, color=C_GRAY, va="center")

save(fig, "w11d1_distress_spiral.png")
