'''Два автомобиля едут друг за другом с постоянными скоростями
V1 и V2 км/час (V1>V2). Определить, какое расстояние будет между ними через
30 минут после того, как первый автомобиль опередил второй на S км.'''
v1,v2=[int(i)for i in input('введите скорости').split()]
s=(v1*0.5)-(v2*0.5)
print('расстояние между ними через 30 мин=', s, 'км')