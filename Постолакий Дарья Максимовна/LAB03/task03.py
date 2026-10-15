#!/usr/bin/env python3


import random

def generate_numbers(count, low, high):
    """
    Генерирует список случайных целых чисел.
    :param count: Количество чисел.
    :param low: Нижняя граница диапазона (включительно).
    :param high: Верхняя граница диапазона (включительно).
    :return: Список случайных целых чисел.
    :rtype: List
    """
    return [random.randint(low, high) for _ in range(count)]

def filter_numbers(list_numbers, condition):
    """
    Фильтрует список чисел по заданному условию.
    :param list_numbers: Список чисел.
    :param condition: Функция-условие, возвращающая True/False.
    :return: Список чисел, удовлетворяющих условию.
    :rtype: List
    """
    return list(filter(condition, list_numbers))

if __name__ == '__main__':
    numbers = generate_numbers(20, -100, 100)

    divisible_by_3_not_9 = lambda x: x % 3 == 0 and x % 9 != 0
    absolute_greater_20 = lambda x: abs(x) > 20
    both_conditions = lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20

    first = filter_numbers(numbers, divisible_by_3_not_9)
    second = filter_numbers(numbers, absolute_greater_20)
    third = filter_numbers(numbers, both_conditions)

    print(f"Исходный список: {numbers}")
    print()
    print(f"Делятся на 3, но не на 9: {first} (длина: {len(first)})")
    print(f"|x| > 20: {second} (длина: {len(second)})")
    print(f"Оба условия: {third} (длина: {len(third)})")
