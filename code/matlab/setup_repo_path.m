% setup_repo_path.m — 把 code/matlab 加入 MATLAB 路径（本课脚本用）
% 在仓库根目录执行: run('code/matlab/setup_repo_path.m')

thisFile = mfilename('fullpath');
matlabDir = fileparts(thisFile);
repoRoot = fileparts(fileparts(matlabDir));

addpath(matlabDir);
fprintf('[setup] repo root: %s\n', repoRoot);
fprintf('[setup] added path: %s\n', matlabDir);
