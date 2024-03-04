def countw(n, max_num):
    if n == 0:
        return 1
    if n < 0:
        return 0

    ways = 0
    for i in range(1, min(max_num, n) + 1):
        ways += countw(n - i, i)

    return ways


def getw(n):
    return countw(n, n)


n = int(input("Введите нат число:\n"))

num_ways = getw(n)
print(f"Кол-во разложений: {num_ways}")