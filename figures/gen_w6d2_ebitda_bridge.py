"""Week 6 第 2 章配图：从净利润到真正的自由现金流（EBITDA 桥）。

**以下全部是简化示意数字（单位：万元），用于教学，不是任何一家真实公司的财报。**

  营业收入 100  ->  现金成本费用 70  ->  折旧和摊销 15  ->  EBIT 15
  EBIT 15 - 利息 12 - 所得税 1 = 净利润 2
  EBITDA = EBIT 15 + 折旧摊销 15 = 30
  真正的自由现金流 = 净利润 2 + 折旧摊销 15 - 资本开支 18 - 营运资金增加 5 = -6
  验算：EBITDA 30 - 资本开支 18 - 营运资金 5 - 利息 12 - 所得税 1 = -6
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED)

import matplotlib.pyplot as plt


ROWS = [
    # (纵轴位置从下往上, 名称, 起点, 终点, 柱子颜色, 数值文字, 文字放在哪一端,
    #  与下一行之间的虚线连接画在哪个横坐标上)
    (9, "净利润", 0, 2, C_BLUE, "+2", "right", 2),
    (8, "加回：折旧和摊销", 2, 17, C_GREEN, "+15", "right", 17),
    (7, "加回：利息支出", 17, 29, C_GREEN, "+12", "right", 29),
    (6, "加回：所得税", 29, 30, C_GREEN, "+1", "right", 30),
    (5, "EBITDA（小计）", 0, 30, C_GOLD, "= 30", "right", 30),
    (4, "减：资本开支", 12, 30, C_RED, "-18", "left", 12),
    (3, "减：营运资金增加", 7, 12, C_RED, "-5", "left", 7),
    (2, "减：真金白银付的利息", -5, 7, C_RED, "-12", "left", -5),
    (1, "减：真金白银交的税", -6, -5, C_RED, "-1", "left", -6),
    (0, "真正的自由现金流", -6, 0, C_BLUE, "= -6", "left", None),
]


def main():
    fig, ax = plt.subplots(figsize=(11.5, 7.4))

    for y, name, x0, x1, color, txt, side, cx in ROWS:
        ax.barh(y, x1 - x0, left=x0, height=0.62, color=color,
                alpha=0.9, zorder=3)
        if side == "right":
            ax.text(x1 + 0.7, y, txt, ha="left", va="center", fontsize=11,
                    color=color, weight="bold", zorder=6)
        else:
            ax.text(x0 - 0.7, y, txt, ha="right", va="center", fontsize=11,
                    color=color, weight="bold", zorder=6)

    # 相邻两根柱子之间的虚线连接（水流图的"落差线"）
    for i in range(len(ROWS) - 1):
        y_top, _, _, _, _, _, _, cx = ROWS[i]
        y_bot = ROWS[i + 1][0]
        ax.plot([cx, cx], [y_top - 0.31, y_bot + 0.31],
                color=C_GRAY, lw=1.0, ls=":", zorder=2)

    vline(ax, 0, -0.62, 9.62, color="#666666", lw=1.4, ls="--", zorder=4)

    ax.set_yticks([r[0] for r in ROWS])
    ax.set_yticklabels([r[1] for r in ROWS], fontsize=10.5)
    ax.set_ylim(-0.7, 9.9)
    ax.set_xlim(-13, 47)
    style_axes(ax, xlabel="万元（简化示意数字，用于教学）",
               title="同一家公司：EBITDA 30 万元，真实现金流 -6 万元",
               grid_axis="x")

    label(ax, 32.5, 4.0,
          "看起来：EBITDA 30 万元，\n是利息 12 万元的 2.5 倍，\n"
          "负债好像很安全",
          color=C_GOLD, fontsize=10.5, ha="left", va="center")
    label(ax, 32.5, 0.9,
          "实际上：真实现金流 -6 万元，\n"
          "利息和税已经付掉了，\n设备也一定要换",
          color=C_RED, fontsize=10.5, ha="left", va="center")

    fig.text(0.5, -0.01,
             "差额就藏在三件事里：折旧对应机器迟早要换（资本开支）、"
             "生意变大要垫钱（营运资金）、利息和税必须真金白银付出去。",
             ha="center", fontsize=10.5, color=C_GRAY)

    save(fig, "w6d2_ebitda_bridge.png")


main()
