def count_digits(num):
    return len(str(num))


N = int(input())

M = 1
S = 0

while S < N:
    S += count_digits(M)
    M += 1

print(M - 1)