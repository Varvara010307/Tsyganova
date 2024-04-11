'''Заполните массив случайными числами в интервале [2,100] и подсчитайте среднее значение всех элементов, которые представляют собой простые числа.'''
from random import randint

def f(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+ 1):
        if num % i == 0:
            return False
    return True
n=int(input('введите кол-во элементов: \n'))
A=[randint(2,100) for _ in range(n)]
print(f'массив:\n{" ".join(str(i) for i in A)}')
s= sum(i for i in A if f(i))
k= sum(1 for i in A if f(i))
sr = None if k == 0 else s/k
print (sr)