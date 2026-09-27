"""一键重新生成所有配图。

用法：
    python3 figures/gen_all.py            # 全部重跑
    python3 figures/gen_all.py w3 w7      # 只重跑 Week 3 和 Week 7 的脚本

每张图生成时会自动跑一次遮挡检测（文字压文字 / 线条穿文字），
有问题的会在终端打印 ⚠️ 提示。
"""

import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent


def main() -> int:
    wanted = [a.lower() for a in sys.argv[1:]]
    scripts = sorted(HERE.glob("gen_w*.py"))
    if wanted:
        scripts = [s for s in scripts
                   if any(s.name.lower().startswith(f"gen_{w}") for w in wanted)]

    failed = []
    for s in scripts:
        print(f"==> {s.name}")
        r = subprocess.run([sys.executable, str(s)])
        if r.returncode != 0:
            failed.append(s.name)

    print()
    if failed:
        print("以下脚本失败：")
        for f in failed:
            print("  ", f)
        return 1
    print(f"全部 {len(scripts)} 个脚本完成。图片在 figures/out/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
