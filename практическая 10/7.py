def prime_factor(a, divisor=2):
    if a <= 1:
        return

    if a % divisor == 0:
        if a != divisor:
            print(divisor, end="*")
            prime_factor(a // divisor, divisor)
        else:
            print(divisor)
    else:
        prime_factor(a, divisor + 1)


nums = int(input("Введите натур число: "))
print(f"{nums} = ", end="")
prime_factor(nums)