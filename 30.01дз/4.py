a,b=map(int,input('границы диапазона:\n').split())
for i in range(a,b+1):
    k=True
    for j in range(2,i) :
        if i % j==0:
            k = False

    if k:
        print (i, end=' ')