#!/usr/bin/env python3

import argparse

SORT_CHOICES = ('asc', 'desc', 'none')
DEFAULT_MIN_LENGTH = 0
ERROR_EMPTY_LIST = "Ошибка: Вы не передали ни одной строки."


def process_strings(strings: list[str], min_length: int, unique: bool, sort_order: str) -> list[str]:
    """
    Применяет фильтры и сортировку к списку строк.
    
    :param strings: Исходный список строк.
    :param min_length: Минимальная длина строки (включительно).
    :param unique: Флаг, нужно ли удалять дубликаты.
    :param sort_order: Порядок сортировки ('asc', 'desc' или 'none').
    :return: Обработанный список строк.
    """
    filtered = [s for s in strings if len(s) >= min_length]

    if unique:
        filtered = list(dict.fromkeys(filtered))

    match sort_order:
        case 'asc':
            filtered.sort()
        case 'desc':
            filtered.sort(reverse=True)
        case 'none':
            pass

    return filtered


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='string_processor',
        description='Скрипт для обработки и фильтрации списка строк',
        epilog='Всего хорошего!'
    )
    
    parser.add_argument('strings', nargs='+', type=str, help='Строки для обработки')
    parser.add_argument('-c', '--count', action='store_true', help='Вывести только количество строк')
    parser.add_argument('-u', '--unique', action='store_true', help='Оставить только уникальные строки')
    parser.add_argument('-l', '--length', type=int, default=DEFAULT_MIN_LENGTH, help='Минимальная длина строки')
    parser.add_argument('-s', '--sort', type=str, choices=SORT_CHOICES, default='none', help='Сортировка')
    
    args = parser.parse_args()

    if not args.strings or all(s.strip() == "" for s in args.strings):
        print(ERROR_EMPTY_LIST)
        exit(2)

    result = process_strings(args.strings, args.length, args.unique, args.sort)

    if args.count:
        print(len(result))
    else:
        for string in result:
            print(string)
