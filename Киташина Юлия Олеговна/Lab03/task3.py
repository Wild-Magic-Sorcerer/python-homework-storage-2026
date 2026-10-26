#!/usr/bin/env python3
import random

COUNT = 20
LOW = -100
HIGH = 100
ABS_LIMIT = 20


def divisible_by_3_not_9(numbers: list[int]) -> list[int]:
    """
    Отбирает числа, которые делятся на 3, но не делятся на 9.

    :param numbers: Список целых чисел
    :type numbers: list[int]
    :return: Список подходящих чисел в исходном порядке
    """
    return list(filter(lambda n: n % 3 == 0 and n % 9 != 0, numbers))


def abs_greater_than_limit(numbers: list[int]) -> list[int]:
    """
    Отбирает числа, абсолютное значение которых больше ABS_LIMIT.

    :param numbers: Список целых чисел
    :type numbers: list[int]
    :return: Список подходящих чисел в исходном порядке
    """
    return list(filter(lambda n: abs(n) > ABS_LIMIT, numbers))


def both_conditions(numbers: list[int]) -> list[int]:
    """
    Отбирает числа, которые подходят под оба условия сразу.

    :param numbers: Список целых чисел
    :type numbers: list[int]
    :return: Список подходящих чисел в исходном порядке
    """
    return list(filter(lambda n: n % 3 == 0 and n % 9 != 0
                       and abs(n) > ABS_LIMIT, numbers))


numbers = [random.randint(LOW, HIGH) for _ in range(COUNT)]
print("Случайные числа:", numbers)
first = divisible_by_3_not_9(numbers)
print("Делятся на 3, но не на 9:", first, "длина", len(first))
second = abs_greater_than_limit(numbers)
print("По модулю больше " + str(ABS_LIMIT) + ":", second, "длина", len(second))
third = both_conditions(numbers)
print("Оба условия сразу:", third, "длина", len(third))
