
x = lab1269(:,2);
y = lab1269(:,3);
%rgb = rgb1269;

xyz = spec2rgb(spec1269pre);
lab_ques = XYZ2Lab_1(xyz,[94.81 100 107.32]);
rgb_1 = lab2rgb(lab_ques);
ans = deltaE2000(lab1269, lab_ques);

s=scatter(x,y,200,rgb_1,'filled');