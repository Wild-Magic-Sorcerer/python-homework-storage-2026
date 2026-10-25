#!/usr/bin/env python3


from random import randint


def filter_func(value: list[int]) -> dict:
    """
    Функция, которая фильтрует список целых чисел по заданным условиям.

    :param value: Исходный список целых чисел, который необходимо отфильтровать.

    :return: Словарь со списками подходящих чисел.
    """
    var_1 = lambda x: x % 3 == 0 and x % 9 != 0
    result_1: list[int] = list(filter(var_1, value))

    var_2 = lambda x: abs(x) > 20
    result_2: list[int] = list(filter(var_2, value))

    var_3 = lambda x: x % 3 == 0 and x % 9 != 0 and abs(x) > 20
    result_3: list[int] = list(filter(var_3, value))

    return {
        'key_1': result_1,
        'key_2': result_2,
        'key_3': result_3
    }


if __name__ == '__main__':
    numbers: list[int] = [randint(-100, 100) for _ in range(20)]

    result: dict = filter_func(numbers)

    print('Числа, которые делятся на 3, но не делятся на 9:', result['key_1'])
    print('Длина:', len(result['key_1']))

    print('Числа, абсолютное значение которых больше 20:', result['key_2'])
    print('Длина:', len(result['key_2']))

    print('Числа, которые удовлетворяют обоим условиям:', result['key_3'])
    print('Длина:', len(result['key_3']))
    
