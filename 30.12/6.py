m=int(input('m='))
n=int(input('n='))
for i in range (1, n):
    a= sum(int(digit) for digit in str(i))
    if m == (i+i)**2:
        print (i)