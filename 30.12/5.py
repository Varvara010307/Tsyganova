'''Напишите программу, которая получает натуральные числа A и B (A<B) и выводит все простые числа на отрезке [A; B].
Пример:
Введите границы диапазона:
10 20
11 13 17 19
'''
s=''
a,b=map(int,input('границы диапазона:\n').split())
for i in range(a,b+1):
    k=0
    for j in range(2,i) :
        if i % j==0:
            k+=1
            if k>2:
                break
    if k ==2:
        s += str(i) + ' '
        # print(i)
print (', '.join(i for i in s.split()))