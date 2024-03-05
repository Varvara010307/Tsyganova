a = int(input('Введите четырёхзначное число: '))
thousands = a // 1000
hundreds = (a // 100) % 10
tens = (a // 10) % 10
units = a % 10
print(a)
print(thousands)
print(hundreds)
print(tens)
print(units)

