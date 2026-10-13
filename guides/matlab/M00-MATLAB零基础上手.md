# M00 · MATLAB 零基础上手

**预计**：课堂 1 课时 · **脚本**：`code/matlab/m00_basics.m`

## 学什么

- **脚本**：`.m` 文件、命令行 vs 编辑器「运行」、清屏 `clc`、注释 `%`。
- **向量与矩阵**：行/列向量、`'` 转置、`*` 与 `.*`、索引 `A(2,3)`。
- **绘图**：`plot`、`xlabel`/`ylabel`/`title`、`grid on`、`figure`。
- 和机器人课的关系：状态、雅可比、齐次变换后面全是矩阵；先把「算得对、画得出来」练熟。

## 怎么跑（Windows 机房）

1. MATLAB → **主页** → **打开** → 选仓库根目录。
2. 命令窗口：

```matlab
run('code/matlab/setup_repo_path.m')
m00_basics
```

3. 应弹出一张 **正弦曲线** 图，命令行打印矩阵维度与一段向量运算结果。

**GNU Octave（可选）**：本补充以 MATLAB 为准；Octave 可试跑 `m00_basics`，图形窗口行为可能略有差异，机器人 Toolbox 部分请用 MATLAB。

## 推荐资源

| 资源 | 说明 |
|------|------|
| [MathWorks MATLAB 入门](https://www.mathworks.com/help/matlab/getting-started-with-matlab.html) | 官方「入门」 |
| [MATLAB 矩阵与数组](https://www.mathworks.com/help/matlab/matrices-and-arrays.html) | 索引、运算 |

## 验收

- 能改 `m00_basics.m` 里 `omega` 或时间向量，重新运行仍出图。
- 口头说清：`a * b` 和 `a .* b` 什么时候不一样。
