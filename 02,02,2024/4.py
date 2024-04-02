def asd(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


A, B = map(int, input("Введите границы диапазона: ").split())

prime_numbers = [num for num in range(A, B + 1) if asd(num)]
print(" ".join(map(str, prime_numbers)))