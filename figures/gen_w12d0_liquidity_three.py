"""W12 第 0 章配图：流动性的三层含义（概念图）。

把原书第十三章开头关于流动性的内容整理成三层：
  ① 资产本身的流动性（想卖的时候卖得掉吗）
  ② 投资组合的流动性（手里有没有随时能动的现金）
  ③ 人生的流动性（你什么时候需要这笔钱）
每层配一个生活类比 + 一个 A 股/港股 落地。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_ORANGE, C_GREEN, C_GRAY,
                             F_BLUE, F_ORANGE, F_GREEN)

fig, ax = fig_ax(12.4, 7.6, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5.0, 9.62, "流动性：三层含义，缺一层都会出事",
      fontsize=16, weight="bold", color="#222222")
plain(ax, 5.0, 9.05, "原书第十三章把它放在投资组合管理的第一条（p223–p226）",
      fontsize=11.5, color=C_GRAY)

rows = [
    ("第一层", "资产的流动性：这件东西想卖的时候，卖得掉吗？",
     "生活类比：房子挂牌半年才成交，余额宝点一下当天就到账。",
     "A 股/港股：跌停板、停牌、一天没几笔成交的小盘股——想卖也卖不掉。",
     C_BLUE, F_BLUE),
    ("第二层", "组合的流动性：你的组合里有多少随时能动的现金？",
     "生活类比：家里要留一笔应急钱，不能全押在定期存款和金条上。",
     "A 股/港股：满仓的人遇到急事，只能在最坏的价位割肉卖出。",
     C_ORANGE, F_ORANGE),
    ("第三层", "人生的流动性：你什么时候需要用到这笔钱？",
     "生活类比：明年要交首付的钱，和二十年后养老的钱，是两笔完全不同的钱。",
     "A 股/港股：急着要用的钱不能进股市——不是股票不好，是你的时间表由不得你。",
     C_GREEN, F_GREEN),
]

y_top = 8.35
h = 2.05
gap = 0.52

for i, (badge, title, life, ashare, ec, fc) in enumerate(rows):
    y = y_top - i * (h + gap) - h
    box(ax, 0.25, y, 1.45, h, badge, fc="#ffffff", ec=ec,
        fontsize=13.5, tc=ec, weight="bold")
    box(ax, 2.10, y, 7.65, h, "", fc=fc, ec=ec, lw=1.5)
    plain(ax, 2.42, y + h - 0.46, title, fontsize=12.8, weight="bold",
          color="#222222", ha="left")
    plain(ax, 2.42, y + h - 1.10, life, fontsize=11.2, color="#333333", ha="left")
    plain(ax, 2.42, y + h - 1.68, ashare, fontsize=11.2, color="#333333", ha="left")

plain(ax, 5.0, 0.36,
      "流动性差的代价不是「收益率低一点」，而是「必须在最坏的价位卖出」。",
      fontsize=12.6, weight="bold", color="#b03030")

save(fig, "w12d0_liquidity_three.png")
