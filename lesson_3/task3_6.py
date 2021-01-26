# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# Данный код работает как с 1 словом, так и со строкой разделенной пробелами
def int_func_title(word):
    return word.title()


print(int_func_title(input("Введите слово:\n")))


#Без title
def int_func(string):
    string_list = string.split()
    for i in range(len(string_list)):
        if string_list[i][0].isalpha():
            string_list[i] = string_list[i][0].upper() + string_list[i][1:]
    string = " ".join(string_list)
    return string

# альтернативное решение
# def int_func(string):
#     string_list = []
#     for word in string.split():
#         if word[0].isalpha():
#             string_list.append(word[0].upper() + word[1:])
#         else:
#             string_list.append(word)
#     string = " ".join(string_list)
#     return string

# через enumerate()
# def int_func(string):
#     string_list = string.split()
#     for i, word in string.split():
#         if word[0].isalpha():
#             string_list[i] = word[0].upper() + word[1:]
#     string = " ".join(string_list)
#     return string



print(int_func(input("Введите предложение:\n")))
