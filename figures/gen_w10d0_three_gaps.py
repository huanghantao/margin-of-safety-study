"""Week 10 第 0 章配图：卡拉曼把价值投资的机会归为三类缝隙（原书 p163）。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_ax, box, plain,
                             C_BLUE, C_ORANGE, C_GREEN, C_GRAY,
                             F_BLUE, F_ORANGE, F_GREEN)

fig, ax = fig_ax(13.6, 8.8, xlim=(0, 12), ylim=(0, 10))

plain(ax, 6.0, 9.72, "卡拉曼的三类投资缝隙：好机会只在这三个地方出现",
      fontsize=15, weight="bold", color="#222222")
plain(ax, 6.0, 9.25, "（《安全边际》第九章，原书 p163）",
      fontsize=10.5, color=C_GRAY)

PANELS = [
    dict(
        x=0.35, fc=F_GREEN, ec=C_GREEN,
        head="第一类\n低于清算价值的打折证券",
        body=("机制：公司今天关门、把资产一件件卖掉、\n"
              "还完债，剩下的钱还比股价高。\n\n"
              "为什么会出现：没人愿意花时间给一家\n"
              "「快关门」的公司估值，也没人愿意\n"
              "拿着它。"),
        ashare=("A 股 / 港股对应\n"
                "破净股、退市整理期股票\n"
                "破产重整中的老股东\n"
                "港股私有化与清盘中的公司"),
    ),
    dict(
        x=4.30, fc=F_BLUE, ec=C_BLUE,
        head="第二类\n与回报率有关的情形",
        body=("机制：退出价格（收购价、赎回价）已知，\n"
              "时间表也大致知道，于是能直接算出\n"
              "年化回报率。\n\n"
              "为什么会出现：机构被限制去「投机收购」，\n"
              "只能把这类证券无脑卖掉。"),
        ashare=("A 股 / 港股对应\n"
                "吸收合并换股套利\n"
                "全面要约收购\n"
                "可转债的到期赎回与回售"),
    ),
    dict(
        x=8.25, fc=F_ORANGE, ec=C_ORANGE,
        head="第三类\n资产转换产生的机会",
        body=("机制：你手里的旧证券被换成新证券——\n"
              "现金、新债、新股，价值在转换前后\n"
              "被重新定价。\n\n"
              "为什么会出现：换出来的新证券太小、\n"
              "太复杂、没人跟踪，拿到的人第一\n"
              "反应就是卖。"),
        ashare=("A 股 / 港股对应\n"
                "分拆上市（A 拆 A、H 拆 A）\n"
                "重大资产重组与借壳\n"
                "破产重整中的债转股"),
    ),
]

W = 3.40
for p in PANELS:
    x = p["x"]
    box(ax, x, 8.05, W, 0.90, p["head"], fc=p["fc"], ec=p["ec"],
        fontsize=12, weight="bold")
    box(ax, x, 4.85, W, 3.00, p["body"], fc="white", ec=p["ec"],
        fontsize=10, tc="#333333")
    box(ax, x, 2.55, W, 1.90, p["ashare"], fc=p["fc"], ec=p["ec"],
        fontsize=10, tc="#333333")

box(ax, 0.35, 0.40, 11.30, 1.75,
    "三类机会的共同点：便宜不是来自「公司变好了」，而是来自「有人被迫卖出」\n"
    "机构限制、指数剔除、无人跟踪、年底调仓——价格无效来自别人的约束，不是来自你的预测",
    fc="#f7f7f7", ec=C_GRAY, fontsize=11, tc="#222222")

save(fig, "w10d0_three_gaps.png")
