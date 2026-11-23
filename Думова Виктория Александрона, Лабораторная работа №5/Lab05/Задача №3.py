#!/usr/bin/env python3

import argparse
import random
import sys

EXIT_INVALID = 2
SORT_ASC = "asc"
SORT_DESC = "desc"
SORT_NONE = "none"
SORT_CHOICES = (SORT_ASC, SORT_DESC, SORT_NONE)
DEFAULT_MIN_LENGTH = 0

def main() -> None:
    """Разбирает аргументы CLI, фильтрует и сортирует строки, выводит результат.

    Args:
        Нет.

    Returns:
        None.

    Raises:
        SystemExit: Если не передано ни одной строки или неверный --sort.
    """
    parser = argparse.ArgumentParser(description="Обработка строковых аргументов")
    parser.add_argument("strings", nargs="*", help="Строки для обработки")
    parser.add_argument("--count", action="store_true", help="Вывести только количество строк после фильтрации")
    parser.add_argument("--random", action="store_true", help="Вывести только случайную строку")
    parser.add_argument("--min-length", type=int, default=DEFAULT_MIN_LENGTH, help="Минимальная длина строки")
    parser.add_argument("--sort", choices=SORT_CHOICES, default=SORT_NONE, help="Сортировка строк")
    args = parser.parse_args()

    if not args.strings:
        print("Ошибка: не передано ни одной строки.", file=sys.stderr)
        sys.exit(EXIT_INVALID)

    filtered = [s for s in args.strings if len(s) >= args.min_length]

    if args.sort == SORT_ASC:
        filtered.sort()
    elif args.sort == SORT_DESC:
        filtered.sort(reverse=True)

    if args.count:
        print(f"Количество: {len(filtered)}")
        return

    if args.random:
        if filtered:
            print(f"Случайная строка: {random.choice(filtered)}")
        else:
            print("Нет строк для вывода.", file=sys.stderr)
        return

    for line in filtered:
        print(line)

if __name__ == "__main__":
    TEST_ARGS = ["яблоко", "груша", "банан", "--min-length", "5", "--sort", "asc"]
    if len(sys.argv) == 1:
        print("--- Тест, что оно работает ---")
        sys.argv.extend(TEST_ARGS)
    main()
