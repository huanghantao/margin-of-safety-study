"""Week 7 第 5 章配图：价值骗子自查清单（听他说什么，看他做什么）。"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_ORANGE, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_ORANGE, F_RED, F_GOLD)

fig, ax = fig_ax(12.4, 7.8)

plain(ax, 5.0, 9.6, "价值骗子自查清单：听他说什么，看他做什么", fontsize=15,
      weight="bold")
plain(ax, 5.0, 9.05, "嘴上说的都对，问题出在账户里的行为", fontsize=11.5,
      color=C_GRAY)

box(ax, 0.3, 8.05, 4.3, 0.8, "他说的话", fc=F_BLUE, ec=C_BLUE, fontsize=12,
    weight="bold")
box(ax, 4.9, 8.05, 4.8, 0.8, "他的行为（账户里发生的事）", fc=F_ORANGE,
    ec=C_ORANGE, fontsize=12, weight="bold")

rows = [
    ("我只看价值，不看股价", "季报里的重仓股，一个季度换一遍"),
    ("好公司越跌越买", "跌 20% 就割肉，涨 20% 就追进去"),
    ("我给客户留足安全边际", "买的全是当下最热的赛道，估值创历史新高"),
    ("我只买看得懂的生意", "讲不清这家公司怎么赚钱，只说赛道好"),
    ("长期持有，做时间的朋友", "换手率极高，靠短期排名拉资金"),
]
for i, (left, right) in enumerate(rows):
    y = 6.75 - i * 1.3
    box(ax, 0.3, y, 4.3, 1.05, left, fc="#ffffff", ec=C_BLUE, fontsize=11.5)
    box(ax, 4.9, y, 4.8, 1.05, right, fc=F_RED, ec=C_RED, fontsize=11.5)

box(ax, 0.9, 0.15, 8.2, 1.05,
    "中了 3 条以上：把这只产品（或这个人）从你的名单里划掉",
    fc=F_GOLD, ec=C_GOLD, fontsize=12.5, weight="bold")

save(fig, "w7d5_value_pretender_checklist.png")
