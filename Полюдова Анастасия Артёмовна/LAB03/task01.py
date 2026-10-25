#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '


lambda_func = lambda x: ('positive even' if x > 0 and x % 2 == 0
    else 'positive odd' if x > 0 and x % 2 != 0
    else 'negative' if x < 0
    else 'zero')


def type_sh():
    """
    Функция, которая получает текст от пользователя и возвращает список целых чисел.

    :return: Преобразованные целые значения или None,
    если ни одно значение не удалось преобразовать.
    """
    text: str = input('Введите целые числа: ').strip()

    if not text:
        print('Пустовато..')
        return None

    numbers: list[int] = []

    for x in text.split(STANDARD_DELIMITED):
        try:
            number: int = int(x)
        except ValueError:
            continue

        numbers.append(number)

    if not numbers:
        print('???')
        return None

    return numbers


if __name__ == '__main__':
    result_1 = type_sh()

    if result_1 is not None:
        for res in result_1:
            result_2: str = lambda_func(res)
            print(res, ':', result_2)
