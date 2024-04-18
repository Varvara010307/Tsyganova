def pri_el(arr):
    ev_ele = [num for num in arr if num % 2 == 0]
    return ev_ele
arr = [7, 60, 9, 4, 8, 2, 1]
ev_ele = pri_el(arr)
print (ev_ele)