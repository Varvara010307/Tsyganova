import math

a = int(input('сторона 1'))
b = int(input('сторона 2'))
c = int(input('сторона 3'))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)