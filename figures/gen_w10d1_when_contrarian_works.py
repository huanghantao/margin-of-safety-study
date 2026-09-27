"""Week 10 第 1 章配图：逆向思维什么时候有用、什么时候只是自我感觉良好。

原书 p168：只有当主流意见确实影响到结果或概率时，逆向思维才派得上用场。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_ax, box, plain, arrow,
                             C_BLUE, C_GREEN, C_RED, C_GRAY,
                             F_GREEN, F_RED)

fig, ax = fig_ax(13.4, 7.8, xlim=(0, 12), ylim=(0, 10))

plain(ax, 6.0, 9.62, "逆向思维什么时候有用？", fontsize=15,
      weight="bold", color="#222222")

box(ax, 2.70, 8.35, 6.60, 0.95,
    "先过一个筛子：这个看法会不会影响价格或结果？",
    fc="#f7f7f7", ec=C_GRAY, fontsize=12.5, weight="bold")

arrow(ax, (6.0, 8.30), (6.0, 7.90), color=C_GRAY, lw=1.8)

box(ax, 3.00, 6.95, 6.00, 0.90,
    "主流意见会不会把价格推离价值？",
    fc="#f7f7f7", ec=C_GRAY, fontsize=12.5)

arrow(ax, (5.30, 6.90), (3.20, 6.20), color=C_RED, lw=1.8)
arrow(ax, (6.70, 6.90), (8.80, 6.20), color=C_GREEN, lw=1.8)

box(ax, 0.35, 5.30, 5.50, 0.85, "不会影响 → 逆向没有用",
    fc=F_RED, ec=C_RED, fontsize=12, weight="bold")
box(ax, 0.35, 2.85, 5.50, 2.25,
    "例子：所有人都相信「太阳明天还会升起」。\n"
    "你偏要说不会——这不叫逆向，这叫胡说。\n\n"
    "因为没有任何人的看法能把太阳的价格推高\n"
    "或压低，你的「反对」换不来便宜的价格，\n"
    "也换不来更好的赔率。",
    fc="white", ec=C_RED, fontsize=10, tc="#333333")

box(ax, 6.15, 5.30, 5.50, 0.85, "会影响 → 逆向才有用",
    fc=F_GREEN, ec=C_GREEN, fontsize=12, weight="bold")
box(ax, 6.15, 2.85, 5.50, 2.25,
    "例子：1983 年人群忽视并抨击 Nabisco 公司，\n"
    "股价低于其他优秀企业（原书 p168）。\n\n"
    "当所有人都看多时，价格被推高、预期回报被\n"
    "压低——此时你的「反对」才换得来有利的\n"
    "赔率。",
    fc="white", ec=C_GREEN, fontsize=10, tc="#333333")

box(ax, 0.35, 0.55, 11.30, 1.95,
    "自检问题：如果全市场都同意这个看法，这只证券的价格会变成什么样？\n"
    "如果答案是「什么也不会变」——你的逆向没有价值，只是自我感觉良好。\n"
    "如果答案是「价格早就被推到远离价值的地方」——这里才是逆向该去的地方。",
    fc="#f7f7f7", ec=C_GRAY, fontsize=11, tc="#222222")

save(fig, "w10d1_when_contrarian_works.png")
