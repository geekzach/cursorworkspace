% m02_run_checks.m — M02：串联检查 M00/M01 脚本是否可跑（不替代人工练习）

clc;
fprintf('=== M02 run checks ===\n');

repoRoot = fileparts(fileparts(fileparts(mfilename('fullpath'))));
setupPath = fullfile(repoRoot, 'code', 'matlab', 'setup_repo_path.m');
if ~isfile(setupPath)
    error('m02_run_checks:NoRepo', '找不到 %s，请把当前文件夹设为仓库根目录', setupPath);
end
run(setupPath);

pass = @(name, ok) fprintf('[%s] %s\n', tern(ok, 'PASS', 'FAIL'), name);

% M00：矩阵运算无图也可检查
try
    A = [1, 2; 3, 4];
    assert(det(A) == -2);
    pass('M00 matrix ops', true);
catch
    pass('M00 matrix ops', false);
end

% M01：工具箱
rtbOk = ~isempty(which('SE3')) && ~isempty(which('trplot'));
pass('M01 SE3/trplot on path', rtbOk);

if rtbOk
    try
        T = SE3.Rz(pi/2) * SE3.Tx(1);
        assert(isa(T, 'SE3'));
        pass('M01 SE3 chain (exercise 3 pattern)', true);
    catch
        pass('M01 SE3 chain (exercise 3 pattern)', false);
    end
else
    pass('M01 SE3 chain (exercise 3 pattern)', false);
end

% M02：练习 1 数值
try
    theta = pi/6;
    R = [cos(theta), -sin(theta); sin(theta), cos(theta)];
    assert(norm(R' * R - eye(2), 'fro') < 1e-10);
    pass('M02 exercise 1 (R''*R)', true);
catch
    pass('M02 exercise 1 (R''*R)', false);
end

fprintf('=== M02 checks done（图形题请肉眼验收 m00/m01 脚本）===\n');

function s = tern(cond, a, b)
    if cond
        s = a;
    else
        s = b;
    end
end
