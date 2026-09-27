"""Week 10 第 4 章配图：认股权配售的稀释机制。

用的是原书 p183–p184 的 XYZ 封闭式基金例子：
100 万份、每份净值 25 美元，每份可用 15 美元认购 1 份新股。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_multi, box, plain, money_bar, arrow,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GRAY)

fig, axes = fig_multi(1, 2, width=14.0, height=7.0)
axL, axR = axes

# ══ 左：每份净值的变化 ═════════════════════════════════════════════
plain(axL, 5.0, 9.55, "配售前后，「每份净值」变成多少（美元）",
      fontsize=12, weight="bold", color="#222222")

BASE, SCALE = 2.0, 0.20
money_bar(axL, 0.55, BASE, 1.70, 25.00 * SCALE, "25.00",
          fc=C_GOLD, ec="#8a6d1f", fontsize=11.5)
money_bar(axL, 2.95, BASE, 1.70, 15.00 * SCALE, "15.00",
          fc=F_BLUE, ec=C_BLUE, fontsize=11.5)
money_bar(axL, 5.35, BASE, 1.70, 20.00 * SCALE, "20.00",
          fc=C_ORANGE, ec="#b35a00", fontsize=11.5)
money_bar(axL, 7.75, BASE, 1.70, 20.13 * SCALE, "20.13",
          fc=F_ORANGE, ec=C_ORANGE, fontsize=11.5)

plain(axL, 1.40, 1.55, "配售前\n每份净值", fontsize=10, va="top",
      color="#333333")
plain(axL, 3.80, 1.55, "认购价\n（每份）", fontsize=10, va="top",
      color=C_BLUE)
plain(axL, 6.20, 1.55, "全部老股东\n都认购", fontsize=10, va="top",
      color="#333333")
plain(axL, 8.60, 1.55, "只有 95%\n认购", fontsize=10, va="top",
      color="#333333")

plain(axL, 5.0, 0.35,
      "稀释来自「低价配售」这件事本身，\n而不是来自别人不认购。",
      fontsize=10.5, color="#555555")

# ══ 右：同一件事，三种人的结果 ═════════════════════════════════════
plain(axR, 5.0, 9.55, "同一件事，三种人的结果",
      fontsize=12, weight="bold", color="#222222")

box(axR, 0.30, 7.30, 9.40, 1.70,
    "① 认购了的老股东\n每份成本 20.00 美元 → 手里每份净值 20.00 美元\n（掏了 15 美元，保住自己的持股比例）",
    fc=F_BLUE, ec=C_BLUE, fontsize=10.5, tc="#333333")
box(axR, 0.30, 5.20, 9.40, 1.70,
    "② 没认购的老股东\n每份成本 25.00 美元 → 手里每份净值 20.13 美元\n（什么都没做，账面立刻少了约 20%）",
    fc=F_GREEN, ec=C_GREEN, fontsize=10.5, tc="#333333")
box(axR, 0.30, 3.10, 9.40, 1.70,
    "③ 超比例认购「别人放弃的份额」的人\n以 15.00 美元买入 5 万份 → 按 20.00 美元净值计\n赚约 25 万美元，钱正是从 ② 那里稀释出来的",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=10.5, tc="#333333")
box(axR, 0.30, 0.60, 9.40, 2.00,
    "这就是原书要说的那句话：\n"
    "没有行使认股权的投资者「经常会持有现金」，\n"
    "从而为那些警惕的价值投资者创造了机会（p183）。",
    fc="#f7f7f7", ec=C_GRAY, fontsize=10.5, tc="#222222")

save(fig, "w10d4_rights_offering.png")
