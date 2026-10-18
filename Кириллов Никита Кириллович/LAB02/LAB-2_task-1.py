'''
Задание №1 Реализуйте функцию, принимающую список строк и возвращающую новый список,
в котором остаются только те строки, длина которых больше среднего значения длины
строки в исходном списке.
'''

DELIMITER = ' '

def long_strings(words):
    lengths = [len(word) for word in words]
    average_len = sum(lengths) / len(lengths)

    return [word for word in words if len(word) > average_len]


if __name__ == '__main__':
    user_answer = input("Введите слова через пробел: ").split(DELIMITER)

    if not user_answer:
        print("Ошибка! Введите список строк!")

    else:
        result = long_strings(user_answer)

    print(f"Список со строками длиннее среднего значения: {result}")
