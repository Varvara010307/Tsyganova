a = int(input('Введите первое натуральное число: '))
b = int(input('Введите второе натуральное число: '))
c = a
v = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
print(f'НОД{c, v} = {gcd}')