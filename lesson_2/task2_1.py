# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
def function():
    pass

listed = [
    1,
    1.1,
    "one",
    ['1', 1],
    (1, 1.1),
    {'key': "1", 'key_1': 1},
    complex(1, 1.1),
    {1, 1.1},
    frozenset('one'),
    True,
    b'text',
    bytearray(b"some text"),
    iter(['1', '3', '4']),
    None,
    int,
    function,
    [i for i in range(1)]
]
for types in listed:
    print(type(types))
