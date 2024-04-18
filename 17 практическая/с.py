def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

user_input = input("Введите символьную строку: ")
longest_word, length = find_longest_word(user_input)
print (f"Самое длинное слово:{longest_word}")
print (f"Длина самого длинного слова:{length}")