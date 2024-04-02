a1 = 5
a2 = 2
b = 7

result_units = (a1 + b) % 10
carry = (a1 + b) // 10
result_tens = a2 + carry

print("Tens digit of the resulting number:", result_tens)
print("Units digit of the resulting number:", result_units)