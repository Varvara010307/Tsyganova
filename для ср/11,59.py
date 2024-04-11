'''Определить частное от деления суммы положительных элементов массива
на модуль суммы отрицательных элементов.'''
def find_quotient(arr):
    sum_plus=sum(x for x in arr if x>0)
    sum_min=sum(abs(x) for x in arr if x<0)
    if sum_min == 0:
        return "елить на 0 нельзя"
    return sum_plus / sum_min

array = [1, -2, 3, -4, 5]
result = find_quotient(array)
print(result)