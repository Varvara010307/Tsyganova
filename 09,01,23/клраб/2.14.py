number = input("Введите трехзначное число: ")

if len(number) == 3 and number.isdigit():
    new_number = number[1:] + number[0]

    print("Полученное число: ", new_number)
else:
    print("Пожалуйста, введите корректное трехзначное число.")