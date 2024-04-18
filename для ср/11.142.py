'''*Изменить знак у максимального по модулю элемента массива. Минимальный элемент массива при этом не определять'''
from random import randint
n=int (input('введите колво эл-ов:\n' ))
A= [randint(-100, 100) for _ in range(n)]
print(f'массив:\n{" ".join(str(i) for i in A)}')
k=max(A, key=abs)
l=A.index(k)
A[l]*=-1
print('езультат', *A)