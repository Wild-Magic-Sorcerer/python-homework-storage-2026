#!/usr/bin/env python3

import argparse

SORT_MODES = ("asc", "desc", "none")
DEFAULT_SORT = "none"


def filter_strings(strings, unique, min_length):
    """
    отфильтровывает строки

    :param strings: список строк
    :param unique: убирать дубликаты
    :param min_length: минимальная длина или None
    :return: список
    """
    result = strings.copy()

    if unique:
        no_dupes = []
        for word in result:
            if word not in no_dupes:
                no_dupes.append(word)
        result = no_dupes

    if min_length is not None:
        result = [s for s in result if len(s) >= min_length]

    return result


def sort_strings(strings, sort_order):
    """
    отсортировывает строки

    :param strings: список строк
    :param sort_order: asc / desc / none
    :return: список
    """
    if sort_order == "asc":
        return sorted(strings)
    elif sort_order == "desc":
        return sorted(strings, reverse=True)
    return strings


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="string_processor",
        description="Обработка строк.",
        epilog="Работа завершена!",
    )
    parser.add_argument("strings", nargs="*", help="Строки")
    parser.add_argument("-c", "--count", action="store_true",
                        help="Только количество")
    parser.add_argument("-u", "--unique", action="store_true",
                        help="Только уникальные")
    parser.add_argument("-l", "--min-length", type=int,
                        help="Минимальная длина")
    parser.add_argument("-s", "--sort", choices=SORT_MODES,
                        default=DEFAULT_SORT, help="Сортировка")
    args = parser.parse_args()

    if not args.strings:
        parser.error("Вы не передали ни одной строки!")

    filtered = filter_strings(args.strings, args.unique, args.min_length)
    final = sort_strings(filtered, args.sort)

    if args.count:
        print(f"Количество строк после фильтрации: {len(final)}")
    else:
        for s in final:
            print(s)
