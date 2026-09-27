"""W3 第 2 章图二：市场先生的两种用法 —— 当"指导"还是当"服务"。

左边把报价当答案，右边把报价当菜单。结果完全不同。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, plain,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_DARK,
                             F_BLUE, F_ORANGE, F_GREEN, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.8)

plain(ax, 5.0, 9.72, "同一个市场先生，两种用法，两种结局",
      fontsize=14, weight="bold", color=C_DARK)

# ── 左：当成指导 ────────────────────────────────────────────
box(ax, 0.15, 8.40, 4.55, 0.85, "把报价当成“指导”（错）",
    fc=F_RED, ec=C_RED, fontsize=12.5, weight="bold")
box(ax, 0.15, 6.95, 4.55, 1.00,
    "他一涨：“他一定知道\n什么我不知道的事” → 赶紧追买",
    fc="white", ec=C_RED, fontsize=11.5)
box(ax, 0.15, 5.50, 4.55, 1.00,
    "他一跌：“他一定知道\n什么我不知道的事” → 吓得割肉",
    fc="white", ec=C_RED, fontsize=11.5)
box(ax, 0.15, 3.80, 4.55, 1.30,
    "结局：买在他最亢奋的时候，\n卖在他最沮丧的时候。\n他什么也没说，是你自己听错了。",
    fc=F_RED, ec=C_RED, fontsize=11.5, weight="bold")

# ── 右：当成服务 ────────────────────────────────────────────
box(ax, 5.30, 8.40, 4.55, 0.85, "把报价当成“服务”（对）",
    fc=F_GREEN, ec=C_GREEN, fontsize=12.5, weight="bold")
box(ax, 5.30, 6.95, 4.55, 1.00,
    "他报得离谱地低：\n拿你的估值一比 → 便宜就买一点",
    fc="white", ec=C_GREEN, fontsize=11.5)
box(ax, 5.30, 5.50, 4.55, 1.00,
    "他报得离谱地高：\n拿你的估值一比 → 贵了就卖，或者不理",
    fc="white", ec=C_GREEN, fontsize=11.5)
box(ax, 5.30, 3.80, 4.55, 1.30,
    "结局：他只是每天来给你报价的人，\n报价不用白不用。\n他有情绪，你不需要有。",
    fc=F_GREEN, ec=C_GREEN, fontsize=11.5, weight="bold")

# ── 底部结论 ────────────────────────────────────────────────
box(ax, 0.15, 2.05, 9.70, 1.30,
    "判断标准只有一句话：\n"
    "你的买卖决定，是根据“价格和价值比谁高”，还是根据“价格昨天涨了还是跌了”？",
    fc=F_GRAY, ec=C_GRAY, fontsize=12)
plain(ax, 5.0, 1.55, "前者是投资，后者就是把市场先生当成了老师。",
      fontsize=11.5, color=C_GRAY)

save(fig, "w3d2_serve_or_guide.png")
