opts = detectImportOptions('multifield.0030.txt');
opts.SelectedVariableNames = [5]; %He mass abundance
opts.DataLines = [14731200 15475200]; %z=100 to z=104
M = readmatrix('multifield.0030.txt',opts);
x= 0:599;
y= 0:247;
z= 0:4;
[X,Y,Z] = meshgrid(x,y,z);
v= M(X+Y*600+Z*600*248+1);
clf;
point =[400, 50, 1];
vals =[-1, 2, 6];
a=1;b=2;c=2;
d= a*-point(1)+b*-point(2)+c*-point(3);
h=obliqueslicing(X,Y,Z,v,a,b,c,d);
for i = vals
    delete(h);
    a=1;b=2;c=2;
    d= a*-(point(1)+i)+b*-(point(2)+i)+c*-(point(3)+i);
    h=obliqueslicing(X,Y,Z,v,a,b,c,d);
    pause(3);
end
close;
function [h] = obliqueslicing(X,Y,Z,v,a,b,c,d)
    [ys,zs] = meshgrid(0:247,0:4);
    xs = -b/a.*ys -c/a.*zs -d/a; 
    h=slice(X, Y, Z, v, xs, ys, zs,'nearest');
    set(h,'EdgeColor','none')
    colorbar;
end
