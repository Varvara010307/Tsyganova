def find_rect_size(s):
    sizes = []
    for num in range(1, s + 1):
        if s % num == 0:
            sizes.append((num, s // num))
    return sizes


s = 12
result = find_rect_size(s)
print(result)