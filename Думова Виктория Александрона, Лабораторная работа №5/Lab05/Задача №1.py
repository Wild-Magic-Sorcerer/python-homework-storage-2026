#!/usr/bin/env python3

import argparse
import sys

MIN_AGE = 0
MAX_AGE = 120
EXIT_INVALID = 2

def positive_int_0_120(value: str) -> int:
    """Преобразует строку в int и проверяет диапазон MIN_AGE..MAX_AGE.

    Args:
        value: Строковое представление возраста.

    Returns:
        int: Проверенный возраст в диапазоне [MIN_AGE, MAX_AGE].

    Raises:
        SystemExit: Если значение не является целым числом или вне диапазона (код EXIT_INVALID).
    """
    try:
        number = int(value)
    except ValueError:
        print(f"Ошибка: возраст '{value}' не является целым числом.", file=sys.stderr)
        sys.exit(EXIT_INVALID)
    if not (MIN_AGE <= number <= MAX_AGE):
        print(f"Ошибка: возраст должен быть от {MIN_AGE} до {MAX_AGE}, получено {number}.", file=sys.stderr)
        sys.exit(EXIT_INVALID)
    return number

def main() -> None:
    """Разбирает аргументы CLI и выводит приветствие.

    Args:
        Нет.

    Returns:
        None.

    Raises:
        SystemExit: При некорректном возрасте или ошибках argparse.
    """
    parser = argparse.ArgumentParser(description="Приветствие пользователя")
    parser.add_argument("name", help="Имя пользователя")
    parser.add_argument("--age", type=positive_int_0_120, default=None,
                        help=f"Возраст (целое число от {MIN_AGE} до {MAX_AGE})")
    parser.add_argument("--greet", action="store_true",
                        help="Использовать обращение «Уважаемый(ая)»")
    args = parser.parse_args()

    prefix = "Уважаемый(ая) " if args.greet else ""
    if args.age is not None:
        print(f"{prefix}{args.name}, ваш возраст: {args.age}.")
    else:
        print(f"{prefix}{args.name}!")

if __name__ == "__main__":
    TEST_ARGS = ["Виктория", "--age", "19", "--greet"]
    if len(sys.argv) == 1:
        print("--- Запуск с тестовыми аргументами ---")
        sys.argv.extend(TEST_ARGS)
    main()
