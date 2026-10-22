#!/usr/bin/env python3

import random

def filter_nums(numbers: list[int]) -> tuple[list[int], list[int], list[int]]:
    """
    Фильтрует список чисел по трем условиям с помощью filter и lambda.
    Возвращает три новых списка.
    """

    cond1 = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))

    cond2 = list(filter(lambda x: abs(x) > 20, numbers))

    cond3 = list(filter(lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20, numbers))

    return cond1, cond2, cond3

if __name__ == '__main__':

    random_nums = [random.randint(-100, 100) for _ in range(20)]

    print(f"Исходный список ({len(random_nums)} шт.):\n{random_nums}\n")

    res1, res2, res3 = filter_nums(random_nums)

    print(f"1. Делятся на 3, но не на 9 (длина {len(res1)}):")
    print(res1)

    print(f"2. Модуль больше 20 (длина {len(res2)}):")
    print(res2)

    print(f"3. Подходят под оба условия (длина {len(res3)}):")
    print(res3)
