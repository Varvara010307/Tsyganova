# Ферзь может двигаться по диагонали, вертикали и горизонтали
def is_valid_move_for_queen(a, b, c, d):

    if a == c or b == d or abs(a - c) == abs(b - d):
        return True
    else:
        return False

a, b = 3, 4  # Положение
c, d = 6, 7  # Цель

if is_valid_move_for_queen(a, b, c, d):
    print(f"Ход из клетки ({a}, {b}) в клетку ({c}, {d}) возможен для ферзя.")
else:
    print(f"Ход из клетки ({a}, {b}) в клетку ({c}, {d}) невозможен для ферзя.")