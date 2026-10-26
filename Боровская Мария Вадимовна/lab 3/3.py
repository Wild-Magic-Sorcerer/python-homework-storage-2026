#!/usr/bin/env python3


def generate_numbers() -> list:
    """
    Генерирует список из 20 псевдослучайных чисел

    :return: Список из 20 целых чисел от -100 до 100
    """
    return [
        15, -42, 9, -99, 27, 0, 81, -18, 33, -3,
        54, -72, 12, -45, 63, 7, -21, 90, -54, 1,
    ]


def main() -> None:
    """
    Применяет фильтры к списку чисел и выводит результат

    :return: None
    """
    numbers = generate_numbers()

    div_3_not_9 = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))
    abs_gt_20 = list(filter(lambda x: abs(x) > 20, numbers))
    both = list(filter(
        lambda x: x % 3 == 0 and x % 9 != 0 and abs(x) > 20,
        numbers,
    ))

    print(div_3_not_9, len(div_3_not_9))
    print(abs_gt_20, len(abs_gt_20))
    print(both, len(both))


main()
