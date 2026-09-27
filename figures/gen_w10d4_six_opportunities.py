"""Week 10 第 4 章配图：六种机会速查卡。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_ORANGE, C_GREEN, C_RED, C_GRAY, C_GOLD,
                             F_BLUE, F_ORANGE, F_GREEN, F_RED, F_GRAY)

fig, ax = fig_ax(14.2, 9.2, xlim=(0, 12), ylim=(0, 10))

plain(ax, 6.0, 9.62, "六种机会速查卡：机制、为什么便宜、A 股/港股在哪里找",
      fontsize=15, weight="bold", color="#222222")
plain(ax, 6.0, 9.12, "（《安全边际》第十章，原书 p176–p194）",
      fontsize=10.5, color=C_GRAY)

CARDS = [
    dict(
        fc=F_GREEN, ec=C_GREEN, head="① 清算",
        body=("机制：公司不再「持续经营」，把资产卖掉、还完债，\n"
              "剩下的钱分给股东。\n"
              "为什么便宜：机构不愿持有正在关门的公司，套利者\n"
              "也嫌它拖得太久（p176）。\n"
              "A 股 / 港股：退市整理期、破产重整、港股清盘、\n"
              "主动卖资产后特别分红。"),
    ),
    dict(
        fc=F_BLUE, ec=C_BLUE, head="② 复杂证券",
        body=("机制：现金流不按固定节奏发，而是「盈利到某个水平」\n"
              "或「某资产卖到某个价格」才发（p180）。\n"
              "为什么便宜：太晦涩，多数人直接把它排除在研究范围外。\n"
              "A 股 / 港股：可转债的修正与回售条款、重整里的\n"
              "债转股与留债、重组里的业绩承诺补偿。"),
    ),
    dict(
        fc=F_ORANGE, ec=C_ORANGE, head="③ 认股权配售",
        body=("机制：公司不给外人发股，而是给老股东一张「按低价、\n"
              "按持股比例认购新股」的权利（p182）。\n"
              "为什么便宜：不认购就被大幅稀释；权利本身很小、\n"
              "没人跟踪、几乎没有公开信息。\n"
              "A 股 / 港股：配股、可转债的优先配售。"),
    ),
    dict(
        fc=F_RED, ec=C_RED, head="④ 风险套利",
        body=("机制：买「正在被收购」的股票，赚收购价与现价之间\n"
              "的差价；赔的是交易失败、价格跌回消息公布前（p184）。\n"
              "为什么便宜：机构被限制「不能投机收购」，只能卖出；\n"
              "专业套利者在小案子里没有优势。\n"
              "A 股 / 港股：吸收合并换股、全面要约收购、私有化。"),
    ),
    dict(
        fc=F_GREEN, ec=C_GREEN, head="⑤ 分拆企业",
        body=("机制：母公司把子公司的股份直接发给自己的股东，\n"
              "而不是卖给外人（p190）。\n"
              "为什么便宜：拿到小公司股票的人无脑卖，机构嫌小，\n"
              "指数不要，分析师不跟踪——卖家不是知道得更多，\n"
              "而是知道得极少（p191）。\n"
              "A 股 / 港股：分拆上市、介绍上市、重组剥离。"),
    ),
    dict(
        fc=F_GRAY, ec=C_GRAY, head="⑥ 缝隙本身的周期",
        body=("机制：一个缝隙赚钱 → 热钱涌入 → 价格被推高、回报\n"
              "下降 → 亏钱 → 赎回迫使卖出 → 热钱离场 → 机会回来\n"
              "（p188–p190）。\n"
              "为什么重要：你必须在别人狂热时少下注、在别人绝望时\n"
              "还敢下注。\n"
              "A 股 / 港股：打新、定增、可转债、ST 重组都走过这条路。"),
    ),
]

for i, c in enumerate(CARDS):
    col, row = divmod(i, 3)
    x = 0.35 + col * 5.95
    y = 6.15 - row * 2.80
    box(ax, x, y + 2.05, 5.55, 0.62, c["head"], fc=c["fc"], ec=c["ec"],
        fontsize=12, weight="bold")
    box(ax, x, y, 5.55, 1.95, c["body"], fc="white", ec=c["ec"],
        fontsize=9, tc="#333333")

save(fig, "w10d4_six_opportunities.png")
