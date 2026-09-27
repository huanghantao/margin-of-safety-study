"""W3 第 3 章图二：一轮完整的市场情绪周期（真实坐标曲线 + 情绪阶段标注）。

说明：曲线形状是简化示意，用来标出"贪婪时买入、恐慌时卖出"这两个位置。
"""

import sys, pathlib

import matplotlib.pyplot as plt

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from figures._common import (save, label, plain, style_axes,
                             C_ORANGE, C_RED, C_GREEN, C_GRAY, C_DARK)

fig, ax = plt.subplots(figsize=(11.5, 7.0))

t = [0, 0.8, 1.6, 2.4, 3.2, 4.0, 4.6, 5.0, 5.6, 6.2, 6.8, 7.4, 8.0, 8.5, 9.0, 9.6, 10.2]
p = [100, 112, 130, 156, 186, 212, 228, 232, 218, 196, 170, 142, 116, 96, 84, 94, 112]

ax.plot(t, p, color=C_ORANGE, lw=2.8, zorder=4)
ax.fill_between(t, p, 0, color=C_ORANGE, alpha=0.07, zorder=1)

ax.plot([5.0], [232], marker="o", ms=13, mfc="none", mec=C_RED, mew=2.6, zorder=5)
ax.plot([9.0], [84], marker="o", ms=13, mfc="none", mec=C_GREEN, mew=2.6, zorder=5)

label(ax, 5.0, 268, "贪婪：“这次不一样”\n大多数人是在这个位置买入的",
      color=C_RED, fontsize=11.5, weight="bold", ha="center", va="center")
label(ax, 8.4, 245, "否认 → 恐惧：\n“只是回调，还会涨回来的”",
      color=C_DARK, fontsize=11.5, ha="center", va="center")
label(ax, 2.1, 42, "乐观 → 兴奋：\n新闻里全是好消息，\n连不炒股的人都在谈论股票",
      color=C_GREEN, fontsize=11.5, ha="center", va="center")
label(ax, 6.4, 25, "投降 → 绝望：“再也不碰股票了”\n大多数人是在这个位置割肉的",
      color=C_GREEN, fontsize=11.5, ha="center", va="center")

ax.set_xlim(-0.4, 10.8)
ax.set_ylim(0, 300)
ax.set_xticks([])
style_axes(ax, ylabel="股价（示意）",
           title="情绪周期：同一家公司，价格却走出了这样一条曲线",
           grid_axis="y")
plain(ax, 10.5, 122, "怀疑 → 希望：\n下一轮又开始了", fontsize=11,
      color=C_GRAY, ha="right", va="center")
plain(ax, -0.2, -34, "曲线形状为简化示意，用于教学", fontsize=10.5,
      color=C_GRAY, ha="left", va="center")

save(fig, "w3d3_emotion_cycle.png")
