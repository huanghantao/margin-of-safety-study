"""W5 第 1 章配图：机构自愿接受的八副镣铐（清单图）。

依据原书 p55–p58 的内容整理成八条，每条给一句"代价"。
"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, plain,
                             C_RED, C_DARK, F_RED, F_ORANGE)

fig, ax = fig_ax(13.5, 8.0, xlim=(0, 14), ylim=(1.4, 9.7))

plain(ax, 7.0, 9.25, "机构投资者自愿戴上的八副镣铐", fontsize=17,
      color=C_DARK, weight="bold")
plain(ax, 7.0, 8.72, "没有人逼他们；是“怕落后”和“怕出错”让他们自己定下了这些规矩",
      fontsize=12, color=C_RED)

items = [
    ("① 现金上限", "最多只能拿一点点现金，\n看到便宜货的时候没钱买"),
    ("② 只买“名单内”的股票", "低价股、未上市、困境企业、\n不分红的公司，一律不碰"),
    ("③ 必须永远满仓", "不管有没有好机会，\n钱都得全部投出去"),
    ("④ 风格与分类牢笼", "消费基金不能买银行股，\n垃圾债基金只能买垃圾债"),
    ("⑤ 季末账面粉饰", "买进当季的赢家、卖掉输家，\n让季报和年报好看一点"),
    ("⑥ 卖出比买入难得多", "流动性差、卖了还得再买一个、\n监管不喜欢高换手"),
    ("⑦ 时间被会议和营销吃掉", "看年报的时间，\n被客户会议和路演切碎"),
    ("⑧ 分析与决策分家", "出错的代价太高，干脆放弃\n基本面分析，改用公式"),
]

x_left, x_right = 0.45, 7.35
w, h = 6.2, 1.42
ys = [6.72, 5.02, 3.32, 1.62]

for i, (title, sub) in enumerate(items):
    col = i // 4               # 0 = 左列, 1 = 右列
    row = i % 4
    x = x_left if col == 0 else x_right
    y = ys[row]
    fc = F_RED if col == 0 else F_ORANGE
    box(ax, x, y, w, h, f"{title}\n{sub}", fc=fc, ec=C_RED, fontsize=11.5,
        tc="#222222", lw=1.5)

save(fig, "w5d1_eight_shackles.png")
