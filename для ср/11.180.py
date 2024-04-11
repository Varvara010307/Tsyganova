def find_first(arr):
    first_index = arr.index(5)
    last_index = len(arr) - arr[::-1].index(5) - 1
    return first_index, last_index

arr= [5, 3, 7, 5, 9, 2, 1, 7, 6, -3]
first_index, last_index = find_first(arr)
print(arr)
print (first_index)
print (last_index)