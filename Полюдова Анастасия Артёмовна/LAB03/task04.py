#!/usr/bin/env python3


from functools import reduce


STANDARD_DELIMITED: str = ' '


def type_text():
    """
    Функция, которая получает текст от пользователя
    и возвращает список введённых слов.

    :return: Список введённых слов или None при пустом вводе.
    """
    text: str = input('Введите слова: ').strip()

    if not text:
        print('Пустовато..')
        return None

    return text.split(STANDARD_DELIMITED)


def handle_text(value: list[str]):
    """
    Функция, которая обрабатывает список строк с помощью filter, map и reduce.

    :param value: Список строк, введенных пользователем.

    :return: Словарь с промежуточными и итоговыми результатами.
    """
    var_1 = lambda x: len(x) >= 7
    result_1: list[str] = list(filter(var_1, value))

    var_2 = lambda x: {'word': x, 'length': len(x)}
    result_2: list[dict] = list(map(var_2, result_1))

    if not result_1:
        return {
            'key_1': result_1,
            'key_2': result_2,
            'key_3': None,
            'key_4': 0
        }

    var_3 = lambda x, y: x if len(x) > len(y) else y
    result_3: str = reduce(var_3, result_1)

    lengths: list[int] = list(map(len, result_1))

    var_4 = lambda x, y: x + y
    result_4: int = reduce(var_4, lengths, 0)

    return {
        'key_1': result_1,
        'key_2': result_2,
        'key_3': result_3,
        'key_4': result_4
    }


if __name__ == '__main__':
    value_1 = type_text()

    if value_1 is not None:
        value_2: dict = handle_text(value_1)

        print('Исходный список:', value_1)
        print('Слова длиной не менее 7 символов:', value_2['key_1'])
        print('Слова и их длины:', value_2['key_2'])
        print('Слово с максимальной длиной:', value_2['key_3'])
        print('Суммарное количество букв:', value_2['key_4'])
