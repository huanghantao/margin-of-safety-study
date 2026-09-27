"""W5 第 4 章配图：机构 vs 你 —— 五条约束的逐条对照。

左边是机构被绑住的地方，右边是你身上同样的位置。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain,
                             C_GRAY, C_GREEN, C_DARK, F_GRAY, F_GREEN)

fig, ax = fig_ax(13.5, 8.4, xlim=(0, 14), ylim=(0, 10.8))

plain(ax, 7.0, 10.35, "同一件事，两种处境：机构被绑住的地方，正是你的自由",
      fontsize=16, color=C_DARK, weight="bold")

box(ax, 0.3, 9.0, 5.6, 0.95, "机构投资者", fc=F_GRAY, ec=C_GRAY, fontsize=14,
    weight="bold")
box(ax, 8.1, 9.0, 5.6, 0.95, "个人投资者（你）", fc=F_GREEN, ec=C_GREEN,
    fontsize=14, weight="bold")

rows = [
    ("谁给你打分", "每个季度跟指数比排名，\n落后就要挨骂", "自己定 3 年目标，\n只看绝对收益"),
    ("钱会不会被抽走", "客户随时可以赎回，\n跌得越狠越要走", "钱是自己的；只要不是短期要用的，\n就没人按门铃"),
    ("能不能不买", "必须满仓，\n飞过来的每个球都要挥", "可以空仓、可以什么都不做，\n等最理想的那个球"),
    ("能买多大的公司", "只能在大公司里挤，\n小公司买不进也卖不出", "小池塘里没人跟你抢，\n被机构丢掉的地方常有机会"),
    ("做错了会怎样", "排名下滑、客户流失、\n职业生涯受影响", "只要不加杠杆、不用短钱，\n没人能逼你在最差的价格卖出"),
]

y = 7.35
h = 1.45
for topic, left, right in rows:
    box(ax, 0.3, y, 5.6, h, left, fc=F_GRAY, ec=C_GRAY, fontsize=11)
    box(ax, 8.1, y, 5.6, h, right, fc=F_GREEN, ec=C_GREEN, fontsize=11)
    plain(ax, 7.0, y + h / 2, topic, fontsize=11.5, color=C_DARK,
          weight="bold")
    y -= 1.72

save(fig, "w5d4_personal_edge.png")
