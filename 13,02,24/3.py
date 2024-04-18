def sum_num(num):
    summa = 0
    while num:
        summa += num % 10
        num //= 10
    return summa


a = int(input('Введите первое натуральное число: '))
b = int(input('Введите второе натуральное число: '))

print(('Во втором числе, сумма цифр больше', 'В первом числе, сумма цифр больше')[sum_num(a) > sum_num(b)])