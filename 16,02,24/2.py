def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

side1 = 3
side2 = 4
side3 = 5

if is_right_triangle(side1, side2, side3):
    print(f"Треугольник со сторонами {side1}, {side2}, {side3} является прямоугольным.")
else:
    print(f"Треугольник со сторонами {side1}, {side2}, {side3} не является прямоугольным.")