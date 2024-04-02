def squared (a, b, k):
    current_row = a
    while current_row <= b:
        row = []
        for i in range (current_row, current_row + 10):
            if i**2 % k != 0:
                row.append(str(i**2))
        print (' '.join(row))
        current_row += 10


a, b, k = map(int,input().split())
squared(a, b, k)