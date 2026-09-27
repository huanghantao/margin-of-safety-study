"""W12 第 4 章配图一：全课程知识地图（结算页）。

把 12 周串成一条竖线：四个阶段，每个阶段标出周次和核心关键词，
底部一行是终点——不是「会选股」，而是手里有一张能逐项打勾的清单。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain, arrow, vline,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_ORANGE, F_GREEN, F_GOLD)

fig, ax = fig_ax(13.0, 8.4, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5.0, 9.72, "十二周一条线：先看清别人怎么亏钱，再学会自己怎么不亏钱",
      fontsize=15.5, weight="bold", color="#222222")
plain(ax, 5.0, 9.22, "这门课没有选股公式，只有一条从「看懂」走到「打勾」的路",
      fontsize=11.0, color=C_GRAY)

stages = [
    ("第一阶段", "Week 1–2    看清规则，也拿到尺子", C_BLUE, F_BLUE,
     "股票是一家公司的一小片所有权 → A 股/港股在哪里交易 → "
     "资产、利润、现金三张表 → 四个常用倍数 → 三种估值思路"),
    ("第二阶段", "Week 3–6    看清别人是怎么亏钱的", C_RED, "#fbeaea",
     "投机者与昂贵的情绪 → 华尔街赚的是「你动手」的钱 → "
     "机构的季度排名压力 → 垃圾债的价值错觉：便宜不等于安全"),
    ("第三阶段", "Week 7–9    看清价值本身", C_GREEN, F_GREEN,
     "安全边际 = 保守估算的价值 - 买入价 → 绝对表现、风险不是波动 → "
     "现值法、清算价值、股市价值法：价值是一个范围"),
    ("第四阶段", "Week 10–12  看清机会，也守住纪律", C_GOLD, F_GOLD,
     "研究缝隙与六种机会 → 制度性机会与困境证券 → "
     "流动性、多样化、对冲、买卖纪律 → 一张买前逐项打勾的清单"),
]

h = 1.48
step = 2.10
y_top = 8.60

vline(ax, 0.30, 1.56, 7.86, color=C_GRAY, lw=2.6, zorder=1)

for i, (badge, title, ec, fc, detail) in enumerate(stages):
    y = y_top - i * step - h
    box(ax, 0.10, y + h / 2 - 0.26, 1.00, 0.52, f"{i + 1}", fc=ec, ec=ec,
        fontsize=13, tc="white", weight="bold", zorder=6)
    box(ax, 1.28, y, 8.50, h, "", fc=fc, ec=ec, lw=1.6)
    plain(ax, 1.62, y + h - 0.42, f"{badge} · {title}", fontsize=12.6,
          weight="bold", color="#222222", ha="left")
    plain(ax, 1.62, y + h - 1.12, detail, fontsize=10.6, color="#333333",
          ha="left")

plain(ax, 5.0, 0.36,
      "终点不是「会选股」，而是手里有一张买前能逐项打勾、"
      "并且敢对不合格的机会说「不」的清单。",
      fontsize=12.4, weight="bold", color="#222222")

save(fig, "w12d4_course_map.png")
