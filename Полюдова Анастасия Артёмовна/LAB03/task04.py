#!/usr/bin/env python3


from functools import reduce


STANDARD_DELIMITED: str = ' '
MAG_NUMBER: int = 7


def type_text():
    """
    Функция, которая получает текст от пользователя
    и возвращает список введённых слов.

    :return: Список введённых слов.
    """
    text: str = input('Введите слова через пробел: ').strip()

    if not text:
        print('Пустовато..')
        return []

    return text.split(STANDARD_DELIMITED)


def handle_text(value: list[str]):
    """
    Функция, которая обрабатывает список строк с помощью filter, map и reduce.

    :param value: Список строк, введенных пользователем.

    :return: Словарь с промежуточными и итоговыми результатами.
    """
    var_1 = lambda x: len(x) >= MAG_NUMBER
    result_1: list[str] = list(filter(var_1, value))

    var_2 = lambda x: {'word': x, 'length': len(x)}
    result_2: list[dict] = list(map(var_2, result_1))

    if not result_1:
        return {
            'filtered_words': result_1,
            'words_w_length': result_2,
            'the_longest': None,
            'total': 0
        }

    var_3 = lambda x, y: x if len(x) > len(y) else y
    result_3: str = reduce(var_3, result_1)

    lengths: list[int] = list(map(len, result_1))

    var_4 = lambda x, y: x + y
    result_4: int = reduce(var_4, lengths, 0)

    return {
        'filtered_words': result_1,
        'words_w_length': result_2,
        'the_longest': result_3,
        'total': result_4
    }


if __name__ == '__main__':
    value_1 = type_text()

    if value_1 :
        value_2: dict = handle_text(value_1)

        print(f'Исходный список: {value_1}')
        print(f'Слова длиной не менее {MAG_NUMBER} символов: 'f'{value_2["filtered_words"]}')
        print(f'Слова и их длины: 'f'{value_2["words_w_length"]}')
        print( f'Слово с максимальной длиной: 'f'{value_2["the_longest"]}')
        print(f'Суммарное количество букв: 'f'{value_2["total"]}')
        
