def is_valid_move_for_knight(a, b, c, d):
    if (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1):
        return True
    else:
        return False

a, b = 2, 3  # Положение
c, d = 4, 4  # Цель

if is_valid_move_for_knight(a, b, c, d):
    print(f"Ход из клетки ({a}, {b}) в клетку ({c}, {d}) возможен для коня.")
else:
    print(f"Ход из клетки ({a}, {b}) в клетку ({c}, {d}) невозможен для коня.")