"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


my_string = input('Вводи строку ')
counts = set()
for i in range(len(my_string)):
    for j in range(1, len(my_string) + 1):
        if i < j:
            counts.add(hash(my_string[i:j]))
counts.remove(hash(my_string))
print(f'{my_string} - {len(counts)} уникальных подстрок')
