n=int(input('Введиьте число n='))
for i in range (1, n+1):
    digits = [int(d) for d in str(i)]
    is_divisible = True
    for digit in digits:
        if digit != 0 and i % digit != 0:
            is_divisible = False
    if is_divisible :
        print (i, end=' ')
