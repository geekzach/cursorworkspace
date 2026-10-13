% m01_plot_frames.m — M01：用 trplot 画两个坐标系
% 依赖: m01_verify_rtb 通过

clc;
fprintf('=== M01 plot frames ===\n');

if isempty(which('SE3')) || isempty(which('trplot'))
    error('m01_plot_frames:MissingToolbox', ...
        '请先安装 Robotics Toolbox 并运行 m01_verify_rtb');
end

% 坐标系 {A}：原点，无旋转
TA = SE3;

% 坐标系 {B}：平移 + 绕 Z 转 45°
TB = SE3(1, 0.5, 0) * SE3.Rz(pi/4);

figure('Name', 'M01: 坐标系 A 与 B');
clf;
hold on;
grid on;
axis equal;
view(3);

trplot(TA, 'frame', 'A', 'color', 'r', 'text', true, 'length', 0.5);
trplot(TB, 'frame', 'B', 'color', 'b', 'text', true, 'length', 0.5);

xlabel('X'); ylabel('Y'); zlabel('Z');
title('M01: SE3 + trplot 示例');

fprintf('TB 平移 t = [%.3f, %.3f, %.3f]\n', TB.t(1), TB.t(2), TB.t(3));
fprintf('=== M01 plot done ===\n');
