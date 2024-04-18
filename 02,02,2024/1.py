def count_com(target_weight, weights):
    dp = [0] * (target_weight + 1)
    dp[0] = 1
    for weight in weights:
        for i in range(weight, target_weight + 1):
            dp[i] += dp[i - weight]
    return dp[target_weight]


target_weight = 185
weights = [15, 17, 21]

combinations = count_com(target_weight, weights)
print('Количество способов купить мастику ровно на 185 кг:', combinations)