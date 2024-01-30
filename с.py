import math

'''формула h=(1/2)*g*t^2 '''
h = float(input('высота(м)='))
g = 9.8
t = math.sqrt(h / ((1 / 2) * g))
print('время(с)=', t)
