number = input("Введите четырехзначное число: ")

if len(number) == 4 and number.isdigit():
    digits = [int(digit) for digit in number]

    sum_of_digits = sum(digits)

    product_of_digits = 1
    for digit in digits:
        product_of_digits *= digit

    print("Сумма цифр числа:", sum_of_digits)
    print("Произведение цифр числа:", product_of_digits)
else:
    print("Пожалуйста, введите корректное четырехзначное число.")