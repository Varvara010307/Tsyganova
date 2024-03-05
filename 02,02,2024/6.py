def find_numbers(m, n):
    numbers = []
    for num in range(1, n):
        digits = [int(digit) for digit in str(num)]
        digit_sum = sum(digits)
        if digit_sum ** 2 == m:
            numbers.append(num)
            return numbers


m = 25
n = 100
result = find_numbers(m, n)
print(result)