def asd(n):
    for digit in str(n):
        if digit == '0' or n % int(digit) != 0:
            return False
    return True


N = int(input('Введите N: '))
numbers = [num for num in range(1, N + 1) if asd(num)]
print(" ".join(map(str, numbers)))