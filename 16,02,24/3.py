def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

number = 66
if is_perfect_number(number):
    print(f"{number} является совершенным числом.")
else:
    print(f"{number} не является совершенным числом.")