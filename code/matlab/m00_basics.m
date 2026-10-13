% m00_basics.m — M00：向量、矩阵、简单绘图
% 先运行: run('code/matlab/setup_repo_path.m')

clc;
fprintf('=== M00 basics ===\n');

%% 标量与向量
a = [1, 2, 3];           % 行向量
b = [4; 5; 6];           % 列向量
c = a' + b;              % 同维列向量相加
fprintf('c = \n'); disp(c);

%% 矩阵
A = [1, 2; 3, 4];
B = [0, 1; 1, 0];
C = A * B;               % 矩阵乘
D = A .* B;              % 逐元素乘
fprintf('size(A) = [%d %d]\n', size(A, 1), size(A, 2));
fprintf('det(A) = %g\n', det(A));

%% 简单仿真：一阶响应 + 正弦激励
omega = 2 * pi * 0.5;    % Hz — 可改这里做课堂小改
t = linspace(0, 4, 400);
y = 1 - exp(-t) + 0.1 * sin(omega * t);

figure('Name', 'M00: 示例曲线');
plot(t, y, 'LineWidth', 1.2);
grid on;
xlabel('t (s)');
ylabel('y');
title('M00 示例：指数趋近 + 正弦扰动');

fprintf('=== M00 done: 应看到一张图 ===\n');
