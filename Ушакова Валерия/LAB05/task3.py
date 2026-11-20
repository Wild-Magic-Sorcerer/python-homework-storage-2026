#!/usr/bin/env python3


import argparse
import sys


def create_parser() -> argparse.ArgumentParser:
    """
    Создает и настраивает парсер аргументов командной строки.

    :return: Настроенный объект ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        prog='string_processor',
        description='Скрипт для обработки и фильтрации списка строк',
        epilog='Всего хорошего!'
    )

    parser.add_argument(
        'strings',
        nargs='+',
        type=str,
        help='Строки для обработки (передавать через пробел)'
    )

    parser.add_argument(
        '-c', '--count',
        action='store_true',
        help='Вывести только количество строк (после фильтрации)'
    )

    parser.add_argument(
        '-u', '--unique',
        action='store_true',
        help='Оставить только уникальные строки'
    )

    parser.add_argument(
        '-l', '--length',
        type=int,
        default=0,
        help='Минимальная длина строки для вывода (по умолчанию 0)'
    )

    parser.add_argument(
        '-s', '--sort',
        type=str,
        choices=['asc', 'desc', 'none'],
        default='none',
        help='Сортировка: asc (по возрастанию), desc (по убыванию), none (без сортировки)'
    )

    return parser


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

    if sort_order == 'asc':
        filtered.sort()
    elif sort_order == 'desc':
        filtered.sort(reverse=True)

    return filtered


def main() -> None:
    """
    Главная функция для запуска скрипта.

    :raises SystemExit: Если список аргументов пуст или введены неверные данные (код 2).
    """
    parser = create_parser()
    args = parser.parse_args()

    if not args.strings or all(s.strip() == "" for s in args.strings):
        print("Ошибка: Вы не передали ни одной строки.", file=sys.stderr)
        sys.exit(2)

    result = process_strings(args.strings, args.length, args.unique, args.sort)

    if args.count:
        print(len(result))
    else:
        for string in result:
            print(string)


if __name__ == '__main__':
    main()
