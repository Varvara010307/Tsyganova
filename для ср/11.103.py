def count_sign_changes(arr):
    changes = 0
    if len(arr)< 2:
        return changes
    current_sign = arr[0] > 0

    for num in arr [1:]:
        if (num >0) != current_sign:
            changes += 1
            current_sign = num > 0
    return changes

import random
arr = [1, 2, -3, 4, -5]
result= count_sign_changes(arr)
print ('кол-во изменений знака в массиве:', result)

