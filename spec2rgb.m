function XYZ=spec2rgb(SR,S,deg)

% 物体色三刺激值计算原理与实例
% 由光谱反射率计算颜色的三刺激值
% 输入参数：
%    SR--光谱反射率，n×2的矩阵，第一列是波长，第2~m列是光谱反射率数据
%    S－光源，'A'表示A光源，'C'表示C光源，'D50','D55','D65','D75',默认D65
%    deg--视场，2表示2°视场，10表示10°视场，默认2°视场
% 输出参数：
%    XYZ－颜色的三刺激值
%
%  编写：wangtengfeng wangtengfeng@whu.edu.cn

%

if nargin==0    % 如果没有参数
  dis('请输入光谱反射率数据，注意是n×2的矩阵，第一列是波长，第2列是光谱反射率数据');
   return;
else if nargin ==1   % 如果是一个参数
       Illcode = 'D65' ; % 光源默认为D65
       degcode = 10;   % 默认10°视场
    else if nargin ==2   % 如果是二个参数  视场默认2°
           Illcode = S;   % 光源
           degcode = 2;   % 默认2°视场
       else if nargin ==3      % 如果 是3个参数 
           Illcode = S;   % 光源
           degcode = deg;  %  视场
           else 
               Illcode = 'D65' ; % 光源默认为D65
               degcode = 2;   % 默认2°视场
           end
       end
    end
end 

 RSPD=getRSPD(Illcode); 

 % 获得CIE标准观察者的数据

if degcode== 10
    CIE_Std = CIE1964Std_XYZ; 
else
    CIE_Std = CIE1931Std_XYZ;
end 

 

% SR和RSPD波长的范围和间隔可能不一样，下面找出两者共有的波长
[comn,iColorS,iIll] = intersect(SR(:,1),RSPD(:,1));

% SR和RSPD以及CIE_Std波长的范围和间隔可能不一样，下面找出3者共有的波长
[comn,iCIE_Std,ic] = intersect(CIE_Std(:,1),comn);
[c,iSR,ic] = intersect(SR(:,1),comn);
[c,iRSPD,ic] = intersect(RSPD(:,1),comn);

if RSPD(iRSPD,2)==0
    XYZ= [0 0 0];
    return
end
   
K=100/sum(RSPD(iRSPD,2).*CIE_Std(iCIE_Std,3));  % 计算K值

 
[a,sample_num]=size(SR);
XYZ=zeros(sample_num-1,3);
for ii=2:sample_num
   Xt=K*sum(RSPD(iRSPD,2).*CIE_Std(iCIE_Std,2).*SR(iSR,ii)); % 计算X刺激值
   Yt=K*sum(RSPD(iRSPD,2).*CIE_Std(iCIE_Std,3).*SR(iSR,ii)); % 计算Y刺激值
   Zt=K*sum(RSPD(iRSPD,2).*CIE_Std(iCIE_Std,4).*SR(iSR,ii)); % 计算Z刺激值
   XYZ(ii-1,:)=[Xt,Yt,Zt];
end