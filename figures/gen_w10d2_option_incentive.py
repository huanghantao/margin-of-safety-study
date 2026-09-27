"""Week 10 第 2 章配图：管理层的钱从哪儿赚，决定他盯着什么（原书 p171）。"""

import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from figures._common import (save, fig_ax, box, plain,
                             C_ORANGE, C_GREEN, C_GRAY,
                             F_ORANGE, F_GREEN, F_GRAY)

fig, ax = fig_ax(13.4, 8.0, xlim=(0, 12), ylim=(0, 10))

plain(ax, 6.0, 9.62, "同一家公司，两种薪酬制度，两种管理层行为",
      fontsize=15, weight="bold", color="#222222")
plain(ax, 6.0, 9.15, "（《安全边际》第九章，原书 p171）",
      fontsize=10.5, color=C_GRAY)

# ── 左 ───────────────────────────────────────────────────────────────
box(ax, 0.35, 8.05, 5.60, 0.90,
    "薪酬挂钩收入 / 总资产 / 净利润",
    fc=F_ORANGE, ec=C_ORANGE, fontsize=12, weight="bold")
box(ax, 0.35, 4.10, 5.60, 3.75,
    "管理层关注：规模、排名、账面指标\n\n"
    "于是：并购做大、不愿分红、\n"
    "不愿分拆、把亏损藏在不容易\n"
    "看见的地方\n\n"
    "结果：股价与价值之间的缺口\n"
    "可以一直留在那里——反正没人\n"
    "考核它",
    fc="white", ec=C_ORANGE, fontsize=10.5, tc="#333333")
box(ax, 0.35, 3.15, 5.60, 0.75,
    "→ 股价长期低于价值，管理层也不着急",
    fc="#f7f7f7", ec=C_GRAY, fontsize=11, weight="bold")

# ── 右 ───────────────────────────────────────────────────────────────
box(ax, 6.05, 8.05, 5.60, 0.90,
    "薪酬挂钩股价（股票期权）",
    fc=F_GREEN, ec=C_GREEN, fontsize=12, weight="bold")
box(ax, 6.05, 4.10, 5.60, 3.75,
    "管理层关注：股价\n\n"
    "于是：分拆、调整资本结构、\n"
    "出售资产、从公开市场回购股票\n\n"
    "原书例子：股价 25 美元、潜在\n"
    "价值 50 美元时，管理层几乎肯定\n"
    "会动手去填这个缺口",
    fc="white", ec=C_GREEN, fontsize=10.5, tc="#333333")
box(ax, 6.05, 3.15, 5.60, 0.75,
    "→ 你那笔便宜货，被管理层亲手兑现",
    fc=F_GREEN, ec=C_GREEN, fontsize=11, weight="bold")

# ── 底部 ─────────────────────────────────────────────────────────────
box(ax, 0.35, 0.45, 11.30, 2.35,
    "你要问的三个问题：\n"
    "1. 管理层的钱是从哪儿赚来的——把公司做大，还是把股价做对？\n"
    "2. 如果是股价：他是靠做大价值把股价推上去，还是靠回购和砍研发把股价「做」上去？\n"
    "3. 期权与激励的行权条件，是绝对股价，还是相对同行的股价、净资产收益率这类真实经营指标？",
    fc="#f7f7f7", ec=C_GRAY, fontsize=11, tc="#222222")

save(fig, "w10d2_option_incentive.png")
