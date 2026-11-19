#!/usr/bin/env python3
import argparse

SORT_CHOICES = ["asc", "desc", "none"]
ERROR_EXIT_CODE = 2

def process_strings(strings: list[str], unique: bool, min_len: int, sort_type: str) -> list[str]:
    """
    Обрабатывает список строк: фильтрует по уникальности, длине и сортирует.

    strings: исходный список строк
    unique: флаг для удаления дубликатов
    min_len: минимальная допустимая длина строки
    sort_type: тип сортировки
    return: обработанный список строк
    """
    if unique:
        strings = list(set(strings))

    if min_len is not None:
        strings = [s for s in strings if len(s) >= min_len]

    if sort_type == "asc":
        strings.sort()
    elif sort_type == "desc":
        strings.sort(reverse=True)

    return strings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Утилита для обработки и фильтрации строк.")
    parser.add_argument("strings", type=str, nargs='*', help="Список строк для обработки")
    parser.add_argument("--unique", action="store_true", help="Оставить только уникальные строки")
    parser.add_argument("--count", action="store_true", help="Вывести только количество строк")
    parser.add_argument("--min-len", type=int, default=None, help="Минимальная длина строки")

    parser.add_argument("--sort", choices=SORT_CHOICES, default="none", help="Тип сортировки")

    args = parser.parse_args()

    if not args.strings:
        parser.error("Эй, неуважаемый пользователь! Вы забыли ввести строки для обработки.")

    result_strings = process_strings(args.strings, args.unique, args.min_len, args.sort)

    if args.count:
        print(len(result_strings))
    else:
        for line in result_strings:
            print(line)

