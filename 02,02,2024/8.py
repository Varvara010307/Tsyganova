def find_divisors_sum(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum


for num in range(1, 10000):
    divisors_sum = find_divisors_sum(num)
    if num != divisors_sum and num == find_divisors_sum(divisors_sum):
        print(num, divisors_sum)