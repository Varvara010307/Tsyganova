n = int(input())
sum=0
for m in range (1,n):
    sum+= len(str(m))
    if sum >= n:
        print (m)
        break