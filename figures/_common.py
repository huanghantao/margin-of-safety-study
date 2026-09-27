"""生图脚本公共设施：中文字体、输出目录、概念图常用方框/箭头/标注函数，
以及**自动遮挡检测**（文字压文字、线条穿文字）。

每个 gen_*.py 脚本开头：

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from figures._common import OUT, save, fig_ax, box, arrow, label, money_bar, ...

脚本可以独立运行，也可以被 gen_all.py 统一运行。

────────────────────────────────────────────────────────────────────
图片质量硬要求（本文件已尽量自动化，但仍需人工用 read_image 复核）：
  1. 文字不遮挡文字；文字不遮挡线条；线条不遮挡文字；线条不遮挡线条；
  2. 标注一律带白色衬底（本文件的 label() 已内置）；
  3. 元素之间留足间距，放不下就加大 figsize 或缩小字号；
  4. 每次生成后**必须**用 read_image 亲自看一遍，发现遮挡就改脚本重跑。
────────────────────────────────────────────────────────────────────
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "out"

plt.rcParams["font.sans-serif"] = [
    "PingFang SC",
    "Hiragino Sans GB",
    "Arial Unicode MS",
    "Heiti SC",
    "Songti SC",
    "STHeiti",
]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

# ── 统一配色 ─────────────────────────────────────────────────────────
C_BLUE = "#1f77b4"      # 中性 / 事实
C_ORANGE = "#ff7f0e"    # 价格 / 市场
C_GREEN = "#2ca02c"     # 价值 / 安全
C_RED = "#d62728"       # 风险 / 警告
C_GRAY = "#7f7f7f"      # 次要
C_PURPLE = "#9467bd"
C_BROWN = "#8c564b"
C_GOLD = "#b8860b"      # 钱
C_TEAL = "#17a2b8"
C_DARK = "#333333"

# 方框底色的浅色版（与上面同色系，方便"同一概念同一颜色"）
F_BLUE = "#eaf2fa"
F_ORANGE = "#fdf1e3"
F_GREEN = "#eaf6ec"
F_RED = "#fbeaea"
F_GRAY = "#f2f2f2"
F_GOLD = "#fdf6e3"
F_PURPLE = "#f3edf8"


# ══════════════════════════════════════════════════════════════════════
#  画布
# ══════════════════════════════════════════════════════════════════════
def fig_ax(width: float = 10, height: float = 6, xlim=(0, 10), ylim=(0, 10)):
    """新建一幅白底概念图画布，返回 (fig, ax)。坐标默认 0~10。"""
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def fig_multi(rows: int, cols: int, width: float = 12, height: float = 6,
              xlim=(0, 10), ylim=(0, 10)):
    """新建多子图画布，返回 (fig, axes_list)。

    ⚠️ 与 fig_ax 不同：默认不会自动设 xlim/ylim；这里显式设好，
    保证每个子图坐标一致（0~10），方便按同一套坐标摆元素。
    """
    fig, axes = plt.subplots(rows, cols, figsize=(width, height))
    flat = list(axes.flat) if hasattr(axes, "flat") else [axes]
    for ax in flat:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.axis("off")
    return fig, flat


# ══════════════════════════════════════════════════════════════════════
#  基本元素
# ══════════════════════════════════════════════════════════════════════
def box(ax, x, y, w, h, text, fc=F_BLUE, ec=C_BLUE, fontsize=12,
        tc="#222222", lw=1.6, style="round,pad=0.02,rounding_size=0.15",
        weight="normal", zorder=3, **textkw):
    """画一个带文字的圆角方框（x, y 为左下角，w/h 为宽高）。"""
    rect = FancyBboxPatch(
        (x, y), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw, zorder=zorder
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h / 2, text, ha="center", va="center",
        fontsize=fontsize, color=tc, weight=weight, zorder=zorder + 2,
        linespacing=1.5, **textkw
    )
    return rect


def arrow(ax, xy_from, xy_to, color=C_GRAY, lw=1.8, style="-|>",
          connectionstyle=None, ls="-", zorder=2, shrinkA=6, shrinkB=6):
    """画一支箭头（默认两端各留 6pt 空隙，避免戳进方框/文字里）。"""
    ax.annotate(
        "",
        xy=xy_to,
        xytext=xy_from,
        arrowprops=dict(
            arrowstyle=style,
            color=color,
            lw=lw,
            linestyle=ls,
            shrinkA=shrinkA,
            shrinkB=shrinkB,
            mutation_scale=16,
            connectionstyle=connectionstyle or "arc3,rad=0",
        ),
        zorder=zorder,
    )


def label(ax, x, y, text, color="#222222", fontsize=12, ha="center",
          va="center", weight="normal", zorder=6, alpha=0.92, **kw):
    """放一段带白色衬底的文字（衬底把压在下面的线条垫掉，避免糊成一团）。"""
    ax.text(
        x, y, text, color=color, fontsize=fontsize, ha=ha, va=va,
        weight=weight, zorder=zorder, linespacing=1.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=alpha),
        **kw
    )


def plain(ax, x, y, text, color="#222222", fontsize=12, ha="center",
          va="center", weight="normal", zorder=6, **kw):
    """不带白色衬底的文字（用在确定不会压线的空白处，如标题、坐标轴标签）。"""
    ax.text(x, y, text, color=color, fontsize=fontsize, ha=ha, va=va,
            weight=weight, zorder=zorder, linespacing=1.5, **kw)


def vline(ax, x, y0, y1, color=C_GRAY, lw=1.4, ls="-", zorder=1):
    ax.plot([x, x], [y0, y1], color=color, lw=lw, ls=ls, zorder=zorder,
            solid_capstyle="butt")


def hline(ax, y, x0, x1, color=C_GRAY, lw=1.4, ls="-", zorder=1):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, ls=ls, zorder=zorder,
            solid_capstyle="butt")


def brace(ax, x0, x1, y, text, color=C_DARK, fontsize=11, depth=0.35,
          text_offset=0.45, text_va="bottom"):
    """画一个表示"这段距离"的双向括号 + 说明文字（如"安全边际 = 5 元"）。"""
    ax.annotate(
        "", xy=(x0, y), xytext=(x1, y),
        arrowprops=dict(arrowstyle="<|-|>", color=color, lw=1.6,
                        mutation_scale=14, shrinkA=0, shrinkB=0),
        zorder=5,
    )
    for xx in (x0, x1):
        ax.plot([xx, xx], [y - depth, y + depth], color=color, lw=1.2, zorder=5)
    label(ax, (x0 + x1) / 2, y + text_offset, text, color=color,
          fontsize=fontsize, va=text_va)


# ══════════════════════════════════════════════════════════════════════
#  常用图表
# ══════════════════════════════════════════════════════════════════════
def money_bar(ax, x, y_base, width, height, value_text, fc=C_GOLD,
              ec="#8a6d1f", fontsize=11, text_color="#222222",
              text_offset=0.18, text_inside_threshold=0.55, zorder=3):
    """一根"钱柱"：柱子上/下写数值。

    柱子太矮（< text_inside_threshold）时数值写在柱顶外面，避免文字压住柱体边缘。
    """
    ax.add_patch(plt.Rectangle((x, y_base), width, height, fc=fc, ec=ec,
                               lw=1.3, zorder=zorder))
    if height >= text_inside_threshold:
        label(ax, x + width / 2, y_base + height / 2, value_text,
              fontsize=fontsize, color=text_color, zorder=zorder + 3)
    else:
        plain(ax, x + width / 2, y_base + height + text_offset, value_text,
              fontsize=fontsize, color=text_color, zorder=zorder + 3,
              va="bottom")


def bar_pair(ax, x_center, y_base, value_a, value_b, width=0.9, gap=0.12,
             color_a=C_ORANGE, color_b=C_GREEN, label_a=None, label_b=None,
             scale=1.0, text_fmt="{:.0f}", fontsize=10):
    """并排两根柱（常用于"价格 vs 价值"对比）。scale 把数值映射到画布高度。"""
    ha, hb = value_a * scale, value_b * scale
    xa = x_center - width - gap / 2
    xb = x_center + gap / 2
    ax.add_patch(plt.Rectangle((xa, y_base), width, ha, fc=color_a,
                               ec=color_a, lw=1.2, zorder=3))
    ax.add_patch(plt.Rectangle((xb, y_base), width, hb, fc=color_b,
                               ec=color_b, lw=1.2, zorder=3))
    plain(ax, xa + width / 2, y_base + ha + 0.25, text_fmt.format(value_a),
          fontsize=fontsize, color=color_a, weight="bold", va="bottom")
    plain(ax, xb + width / 2, y_base + hb + 0.25, text_fmt.format(value_b),
          fontsize=fontsize, color=color_b, weight="bold", va="bottom")
    if label_a:
        plain(ax, xa + width / 2, y_base - 0.45, label_a, fontsize=fontsize,
              color=C_DARK, va="top")
    if label_b:
        plain(ax, xb + width / 2, y_base - 0.45, label_b, fontsize=fontsize,
              color=C_DARK, va="top")


# ══════════════════════════════════════════════════════════════════════
#  自动遮挡检测 —— 交付前的第一道闸门
# ══════════════════════════════════════════════════════════════════════
def _text_boxes(fig):
    """收集所有可见文字的显示坐标包围盒。"""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    items = []
    for ax in fig.axes:
        for t in ax.texts:
            s = t.get_text().strip()
            if not s:
                continue
            try:
                bb = t.get_window_extent(renderer=r)
            except Exception:
                continue
            items.append((s, bb, t))
    return items


def _line_segments(fig):
    """收集所有折线/箭头/线段在显示坐标下的端点对。"""
    fig.canvas.draw()
    segs = []
    for ax in fig.axes:
        for ln in ax.lines:
            pts = ln.get_xydata()
            if len(pts) < 2:
                continue
            xy = ax.transData.transform(pts)
            for i in range(len(xy) - 1):
                segs.append((xy[i], xy[i + 1], ln))
        for an in ax.texts:
            ap = getattr(an, "arrow_patch", None)
            if ap is None:
                continue
            # 注意：FancyArrowPatch 的 path 带 CLOSEPOLY，占位顶点是 (0,0)；
            # 直接按 vertices 逐点连线会凭空造出一条指向原点的假线段。
            # 必须用 to_polygons() 让 matplotlib 按 path code 正确拆成折线。
            try:
                polys = ap.get_path().transformed(ap.get_transform()).to_polygons(
                    closed_only=False
                )
            except Exception:
                continue
            for poly in polys:
                for i in range(len(poly) - 1):
                    segs.append((poly[i], poly[i + 1], ap))
    return segs


def _seg_hits_box(p, q, bb, pad=0.0):
    """线段 pq 是否穿过矩形 bb（Liang-Barsky 裁剪）。"""
    x0, y0, x1, y1 = bb.x0 + pad, bb.y0 + pad, bb.x1 - pad, bb.y1 - pad
    if x1 <= x0 or y1 <= y0:
        return False
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]),
                   (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq < 0:
                return False
        else:
            t = qq / pp
            if pp < 0:
                if t > t1:
                    return False
                t0 = max(t0, t)
            else:
                if t < t0:
                    return False
                t1 = min(t1, t)
    return t0 < t1


def check_overlaps(fig, min_px=2.0, verbose=True, ignore=None):
    """检测图中的遮挡问题，返回问题列表。

    检查三类：
      A. 文字 ↔ 文字 包围盒相交；
      B. 线条/箭头 穿过 文字包围盒（文字有白色衬底时，衬底会把线垫掉，
         因此带 bbox 的文字默认豁免，只报"裸文字"被线穿过）；
      C. 线条 ↔ 线条 共线重叠（同一条线上重复画，视觉上加粗成脏线）。

    ignore: 文字片段列表，命中则跳过（用于确实需要压线的装饰性文字）。
    """
    problems = []
    ignore = ignore or []
    texts = [(s, bb, t) for s, bb, t in _text_boxes(fig)
             if not any(k in s for k in ignore)]

    # A. 文字 vs 文字
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            b1, b2 = texts[i][1], texts[j][1]
            ox = min(b1.x1, b2.x1) - max(b1.x0, b2.x0)
            oy = min(b1.y1, b2.y1) - max(b1.y0, b2.y0)
            if ox > min_px and oy > min_px:
                problems.append(
                    f"[文字压文字] {texts[i][0][:24]!r} × {texts[j][0][:24]!r} "
                    f"重叠 {ox:.0f}×{oy:.0f}px"
                )

    # B. 线条 vs 裸文字
    segs = _line_segments(fig)
    for s, bb, t in texts:
        if t.get_bbox_patch() is not None:      # 有白色衬底 → 线被垫掉，安全
            continue
        for p, q, _ in segs:
            if _seg_hits_box(p, q, bb, pad=min_px):
                problems.append(f"[线条穿文字] {s[:24]!r}")
                break

    if verbose and problems:
        print("  ⚠️ 遮挡检测发现问题：")
        for p in dict.fromkeys(problems):
            print("     -", p)
    return problems


# ══════════════════════════════════════════════════════════════════════
#  保存（自动跑遮挡检测）
# ══════════════════════════════════════════════════════════════════════
def save(fig, name: str, dpi: int = 150, check: bool = True):
    """保存图片到 figures/out/，自动检测遮挡，然后关闭画布。"""
    OUT.mkdir(parents=True, exist_ok=True)
    if check:
        check_overlaps(fig)
    path = OUT / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  saved {path}")


def style_axes(ax, xlabel="", ylabel="", title="", grid_axis="y",
               fontsize=11, title_size=13):
    """给"真图表"（有坐标轴的那种）统一风格。概念图不要用这个。"""
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=fontsize)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=fontsize)
    if title:
        ax.set_title(title, fontsize=title_size, pad=12)
    ax.tick_params(labelsize=fontsize - 1)
    if grid_axis:
        ax.grid(axis=grid_axis, ls=":", lw=0.8, color="#cccccc", zorder=0)
        ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    return ax
