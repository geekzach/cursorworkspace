# M01 · Peter Corke Robotics Toolbox：安装、验证与坐标系

**预计**：课堂 1 课时（含安装等待） · **脚本**：`m01_verify_rtb.m`、`m01_plot_frames.m`

## 学什么

- 在 **MATLAB** 里安装 **Robotics Toolbox for MATLAB**（当前主线 **RTB 10.x**，与《Robotics, Vision & Control》第 2 版配套）。
- 验证 `SE3`、齐次变换、**坐标系可视化**（`trplot`）。
- 为后续正运动学、DH、末端位姿打基础。

## 安装（推荐：`.mltbx` 一键装）

机房电脑若已装好，可跳过，直接跑验证脚本。

1. 从 Peter Corke 站点下载 **Robotics Toolbox for MATLAB (Latest .mltbx)**：  
   [https://petercorke.com/resources/downloads/](https://petercorke.com/resources/downloads/)
2. 或在 GitHub 发布页下载 **`RTB.mltbx`**（与上面同源）：  
   [https://github.com/petercorke/robotics-toolbox-matlab/releases](https://github.com/petercorke/robotics-toolbox-matlab/releases)
3. 在 MATLAB 里 **双击 `RTB.mltbx`**，或拖进命令窗口 → 按提示 **安装**。
4. 安装后可在 **主页 → 附加功能 → 管理附加功能** 里看到 Robotics Toolbox。

说明：`.mltbx` 会把 **Spatial Math** 等依赖一起装好，比手工 `git clone` 适合机房统一镜像。

**备选（自己电脑、需编译）**：按官方 README 从 GitHub 克隆 `robotics-toolbox-matlab`、`spatial-math`、`toolbox-common-matlab` 后 `make`，再在 MATLAB 里 `startup_rvc`。步骤见：  
[https://github.com/petercorke/robotics-toolbox-matlab#installation](https://github.com/petercorke/robotics-toolbox-matlab#installation)

## 验证与可视化

仓库根目录：

```matlab
run('code/matlab/setup_repo_path.m')
m01_verify_rtb    % 检查 SE3 / trplot 是否可用
m01_plot_frames   % 画两个坐标系 {A}、{B}
```

`m01_verify_rtb` 全部 `[OK]` 再画帧；若有 `[FAIL]`，先确认附加功能已启用，再 `restoredefaultpath; rehash toolboxcache` 后重装或重启 MATLAB。

## 推荐资源

| 资源 | 说明 |
|------|------|
| [Robotics Toolbox for MATLAB（GitHub）](https://github.com/petercorke/robotics-toolbox-matlab) | 文档与 Installation |
| [Spatial Math Toolbox 文档](https://petercorke.com/spatial-math/) | `SE3`、`SO3` 对象 |

## 验收

- `which SE3` 有路径；`m01_plot_frames` 出现带 **X/Y/Z** 轴的坐标系图。
- 能说出：齐次变换 **T** 把「坐标系 B 相对 A」的位姿编码成 4×4 矩阵（本课先会用 `SE3` 构造与画图即可）。
