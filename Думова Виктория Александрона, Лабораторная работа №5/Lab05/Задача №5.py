#!/usr/bin/env python3

import argparse
import random
import string
import sys

MIN_LENGTH = 8
MAX_LENGTH = 64
MIN_COUNT = 1
EXIT_INVALID = 2
DIGITS = string.digits
SPECIAL = "!@#$%^&*()-_=+"
LETTERS = string.ascii_letters
OUTPUT_SEPARATOR = "\n"

def build_alphabet(no_digits: bool, no_special: bool) -> str:
    """Формирует набор символов для генерации паролей.

    Args:
        no_digits: Если True — исключить цифры из набора.
        no_special: Если True — исключить специальные символы из набора.

    Returns:
        str: Строка, содержащая все допустимые символы.

    Raises:
        Нет.
    """
    alphabet = LETTERS
    if not no_digits:
        alphabet += DIGITS
    if not no_special:
        alphabet += SPECIAL
    return alphabet

def main() -> None:
    """Разбирает аргументы CLI, генерирует пароли и сохраняет их в файл.

    Args:
        Нет.

    Returns:
        None.

    Raises:
        SystemExit: Если длина вне MIN_LENGTH..MAX_LENGTH, количество меньше MIN_COUNT
            или набор символов пуст после исключений.
    """
    parser = argparse.ArgumentParser(description="Генератор паролей")
    parser.add_argument("length", type=int, help=f"Длина пароля ({MIN_LENGTH}–{MAX_LENGTH})")
    parser.add_argument("count", type=int, help="Количество паролей")
    parser.add_argument("--no-digits", action="store_true", help="Исключить цифры")
    parser.add_argument("--no-special", action="store_true", help="Исключить специальные символы")
    parser.add_argument("--output", default=None, help="Файл для сохранения паролей")
    args = parser.parse_args()

    if not (MIN_LENGTH <= args.length <= MAX_LENGTH):
        print(f"Ошибка: длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH}.", file=sys.stderr)
        sys.exit(EXIT_INVALID)

    if args.count < MIN_COUNT:
        print("Ошибка: количество паролей должно быть положительным.", file=sys.stderr)
        sys.exit(EXIT_INVALID)

    alphabet = build_alphabet(args.no_digits, args.no_special)
    if not alphabet:
        print("Ошибка: после исключения символов генерация невозможна.", file=sys.stderr)
        sys.exit(EXIT_INVALID)

    passwords = ["".join(random.choice(alphabet) for _ in range(args.length))
                 for _ in range(args.count)]

    for password in passwords:
        print(password)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            for password in passwords:
                file.write(password + OUTPUT_SEPARATOR)

if __name__ == "__main__":
    TEST_ARGS = ["12", "3", "--no-special", "--output", "passwords.txt"]
    if len(sys.argv) == 1:
        print("--- Тест, что оно работает ---")
        sys.argv.extend(TEST_ARGS)
    main()
