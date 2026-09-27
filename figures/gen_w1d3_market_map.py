"""Week 1 第 3 章配图：A 股、港股、美股——交易所在哪、去哪里查资料。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, arrow, label, plain, brace,
                             hline, vline, money_bar, bar_pair, style_axes,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_GREEN, F_ORANGE, F_GOLD, F_RED, F_GRAY)

fig, ax = fig_ax(11.5, 7.6, xlim=(0, 10), ylim=(0, 10))

plain(ax, 5, 9.62, "三个市场：A 股、港股、美股", fontsize=15, weight="bold")

COLW, GAP = 2.90, 0.40
xs = [0.25 + i * (COLW + GAP) for i in range(3)]

heads = ["A 股（中国大陆）", "港股（中国香港）", "美股（美国）"]
hcol = [(F_RED, C_RED), (F_GREEN, C_GREEN), (F_BLUE, C_BLUE)]
for x, t, (fc, ec) in zip(xs, heads, hcol):
    box(ax, x, 8.00, COLW, 1.10, t, fc=fc, ec=ec, fontsize=12.5, weight="bold")

body = [
    ("上海证券交易所\n　· 主板：大型成熟公司\n　· 科创板：硬科技公司\n"
     "深圳证券交易所\n　· 主板：成熟公司\n　· 创业板：成长型公司\n"
     "北京证券交易所\n　· 创新型中小企业\n"
     "指数：上证指数、沪深300"),
    ("香港交易所\n（港交所 / HKEX）\n　· 主板：绝大多数公司\n　· GEM：中小型公司\n"
     "特点：\n　· 可用港股通买一部分\n　· 允许「同股不同权」\n"
     "指数：恒生指数、\n恒生科技指数"),
    ("纽约证券交易所\n（NYSE）\n　· 历史最久、大盘股为主\n"
     "纳斯达克\n（NASDAQ）\n　· 科技公司集中\n"
     "特点：\n　· 用美元交易\n　· 交易时间在中国深夜\n"
     "指数：标普500、\n纳斯达克指数"),
]
for x, t in zip(xs, body):
    box(ax, x, 2.90, COLW, 4.75, t, fc="#fbfbfb", ec=C_GRAY, fontsize=9.5,
        multialignment="left")

box(ax, 0.25, 0.35, 9.50, 2.10,
    "查公司原始资料，认准这两个官方入口\n"
    "巨潮资讯网 cninfo.com.cn　——　A 股公司年报、季报、公告的指定披露网站\n"
    "香港交易所「披露易」 hkexnews.hk　——　港股公司年报、公告、招股书的官方平台",
    fc=F_GOLD, ec=C_GOLD, fontsize=11)

save(fig, "w1d3_market_map.png")
