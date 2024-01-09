import math
x1,y1=[int(i)for i in input().split()]
x2,y2=[int(j)for j in input().split()]
d=((x2-x1)**2 + (y2-y1)**2)**0.5
print ('длина=', d)