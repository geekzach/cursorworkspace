# 机器人技术课 · MATLAB 课堂补充（M00–M02）

**定位**：课内一次性补充，和学期周导引 **T00–T04** 分开；不占 [`plan/`](../plan/SEMESTER_PLAN.md) 打卡表。  
**代码**：[`code/matlab/`](../../code/matlab/)（在仓库根目录用 MATLAB 打开并 `addpath` 后运行）。

| ID | 导引 | 脚本 |
|----|------|------|
| M00 | [MATLAB 零基础上手](M00-MATLAB零基础上手.md) | `code/matlab/m00_basics.m` |
| M01 | [Robotics Toolbox 安装与坐标系](M01-Robotics-Toolbox安装与坐标系.md) | `m01_verify_rtb.m`、`m01_plot_frames.m` |
| M02 | [课堂练习与小结](M02-课堂练习与小结.md) | `m02_run_checks.m` · 答案见 [M02-练习参考答案](M02-练习参考答案.md) |

**环境**：学校机房 **Windows + MATLAB**（R2019b 或更新更省心）；GNU Octave 仅作备选，见 M00 一句说明。

**怎么开始**（每次上课）：

1. 打开 MATLAB，**当前文件夹**切到本仓库根目录（含 `code/`、`guides/` 的那一层）。
2. 命令行执行：`run('code/matlab/setup_repo_path.m')`
3. 按 M00 → M01 → M02 顺序运行对应 `.m` 脚本。
