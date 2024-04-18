from random import randint
n= 22
a= [randint(-170, 170) for i in range(n)]
print (*a)
b = []
c = []
for i in range(22):
    if a[i] >= 0:
        b.append(a[i])
    else:
        c.append(a[i])
bs = sum(i for i in b)
cs = sum(i for i in c)
print (f'р рост девочек {bs/len(b)}')
print (f'р рост мальчиков {-cs/len(c)}')