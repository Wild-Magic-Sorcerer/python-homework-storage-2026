#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '
GL: str = 'уеыаоэяиюё'


def check_gl(word: str) -> bool:
    count: int = 0

    for letter in word.lower():
        if letter in GL:
            count += 1

    return count >= 3


def func4(**kwargs) -> dict:
    result: dict = {}

    for arg_name, arg_value in kwargs.items():
        if isinstance(arg_value, str) and check_gl(arg_value):
            result[arg_name] = arg_value

    return result


if __name__ == '__main__':
    text: str = input('Введите аргументы в формате имя=значение: ').strip()

    if not text:
        print('Пустовато..')
    else:
        result_1: dict = {}

        for var_1 in text.split(STANDARD_DELIMITED):
            if '=' in var_1:
                key, value = var_1.split('=', 1)
                result_1[key] = value

        result_2: dict = func4(**result_1)

        if not result_2:
            print('Подходящих значений нет')
        else:
            print('Результат:', result_2)
            