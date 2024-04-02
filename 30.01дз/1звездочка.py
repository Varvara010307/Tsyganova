for i in range(1,10000):
    k=0
    w=0
    for y in range(1,i) :
        if i % y==0:
            k += y
    for j in range(1,k) :
        if k % j==0:
            w += j
    if i == w and i != k and i == min(i,k):
        print (i, k)