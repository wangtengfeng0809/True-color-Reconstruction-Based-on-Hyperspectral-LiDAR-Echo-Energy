function [ Lab ] = XYZ2Lab_0( XYZ,XYZ0 )

%   XYZ数据转换为Lab数据，可批量处理
%   输入原始XYZ数据， n*3 矩阵
%   输入使用的光源的三刺激值XYZ0，1*3矩阵

X=XYZ(:,1);
Y=XYZ(:,2);
Z=XYZ(:,3);

X0=XYZ0(:,1);
Y0=XYZ0(:,2);
Z0=XYZ0(:,3);

L=116*f(Y./Y0)-16;
a=500*(f(X./X0)-f(Y./Y0));
b=200*(f(Y./Y0)-f(Z./Z0));

Lab(:,1)=L;
Lab(:,2)=a;
Lab(:,3)=b;

function [ ff ] = f( I )
if ( I > 0.008856 )
    ff = I.^(1.0/3);
else
    ff = 7.787*I+16.0/116;
end