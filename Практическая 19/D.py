def encode_string(s):
    encoded_string = ''
    count = 1

    for i in range(len(s)):
        if i != len(s) - 1 and s[i] == s[i+1]:
            count += 1
        else:
            encoded_string += s[i] + str(count)
            count = 1
    return encoded_string

input_string = input('Bведите строку:')
encoded_string = encode_string(input_string)
print("Закодированная строка:", encoded_string)