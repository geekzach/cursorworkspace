% m01_verify_rtb.m — M01：检查 Robotics / Spatial Math 是否可用
% 需已安装 RTB.mltbx（见 guides/matlab/M01-...）

clc;
fprintf('=== M01 verify Robotics Toolbox ===\n');

names = {};
oks = {};
details = {};

% SE3 类（Spatial Math，随 RTB 安装）
hasSE3 = (exist('SE3', 'class') == 8) || (exist('SE3', 'file') == 2);
if hasSE3
    names{end+1} = 'SE3'; %#ok<AGROW>
    oks{end+1} = true; %#ok<AGROW>
    details{end+1} = which('SE3'); %#ok<AGROW>
else
    names{end+1} = 'SE3'; %#ok<AGROW>
    oks{end+1} = false; %#ok<AGROW>
    details{end+1} = '未找到 SE3 — 请安装 RTB.mltbx'; %#ok<AGROW>
end

hasTrplot = ~isempty(which('trplot'));
names{end+1} = 'trplot'; %#ok<AGROW>
oks{end+1} = hasTrplot; %#ok<AGROW>
if hasTrplot
    details{end+1} = which('trplot'); %#ok<AGROW>
else
    details{end+1} = '未找到 trplot'; %#ok<AGROW>
end

try
    T = SE3.Rz(0.1) * SE3.Tx(0.5);
    okMul = isa(T, 'SE3');
    names{end+1} = 'SE3 multiply'; %#ok<AGROW>
    oks{end+1} = okMul; %#ok<AGROW>
    details{end+1} = class(T); %#ok<AGROW>
catch ME
    names{end+1} = 'SE3 multiply'; %#ok<AGROW>
    oks{end+1} = false; %#ok<AGROW>
    details{end+1} = ME.message; %#ok<AGROW>
end

allOk = true;
for k = 1:numel(names)
    if oks{k}
        tag = 'OK';
    else
        tag = 'FAIL';
        allOk = false;
    end
    fprintf('[%s] %s — %s\n', tag, names{k}, details{k});
end

if allOk
    fprintf('=== M01 verify: 全部通过，可运行 m01_plot_frames ===\n');
else
    fprintf('=== M01 verify: 有失败项，见 guides/matlab/M01-Robotics-Toolbox安装与坐标系.md ===\n');
end
