"""Week 2 第 4 章配图：三种估值思路，各问各的问题。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, fig_ax, box, label, plain,
                             C_BLUE, C_GOLD, C_GREEN,
                             F_BLUE, F_GOLD, F_GREEN)

fig, ax = fig_ax(12, 6.8, xlim=(0, 12), ylim=(0, 10))

plain(ax, 6, 9.75, "三种估值思路：同一家公司，三种问法", fontsize=15,
      weight="bold", color="#222222")

cards = [
    (0.15, F_GREEN, C_GREEN,
     "① 看资产（资产法）\n"
     "它有什么：现金、存货、厂房、地皮\n"
     "怎么算：资产按能卖的价格加起来，\n"
     "　　　　再减掉欠别人的债\n"
     "什么时候好用：重资产、清算类公司\n"
     "弱点：账面数字可能是虚的，\n"
     "　　　好品牌、好口碑算不进去"),
    (4.2, F_BLUE, C_BLUE,
     "② 看盈利（盈利法）\n"
     "它一年赚多少：净利润、每股盈利\n"
     "怎么算：每股盈利 乘以 一个倍数\n"
     "什么时候好用：盈利稳定的生意\n"
     "　　　　　　　（水电、白酒）\n"
     "弱点：倍数给多少全凭判断，\n"
     "　　　而且盈利会上下波动"),
    (8.25, F_GOLD, C_GOLD,
     "③ 看现金流（现金流法）\n"
     "它未来能收回多少钱：自由现金流\n"
     "怎么算：一年一年预测，再折回今天\n"
     "什么时候好用：现金流稳定的公司\n"
     "弱点：预测最不可靠，\n"
     "　　　贴现率一改，结果大变"),
]

for x, fc, ec, text in cards:
    box(ax, x, 1.5, 3.6, 7.8, text, fc=fc, ec=ec, fontsize=11)

label(ax, 6, 0.7,
      "三种思路经常一起用：算出来的数字不一样，才说明价值是一个区间",
      fontsize=12, color="#222222")

save(fig, "w2d4_three_methods.png")
