load('Distance.mat')
%load('Distance.mat')
xyz = spec2rgb(color24PrSpec);
lab = XYZ2Lab_0(xyz,[94.81 100 107.32]);
rgb = lab2rgb(lab);
S = repmat([100],numel(Distance(:,1)),1);
c = rgb;
scatter3(Distance(:,1),Distance(:,2),Distance(:,3),S(:,1),rgb,'filled')