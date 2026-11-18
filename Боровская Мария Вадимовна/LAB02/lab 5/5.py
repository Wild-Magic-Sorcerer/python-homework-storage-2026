#!/usr/bin/env python3

import argparse
import random
import string

MIN_LENGTH = 8
MAX_LENGTH = 64
LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?"


def generate_password(length, use_digits, use_special):
    """
    генерирует пароль

    :param length: длина
    :param use_digits: включать цифры
    :param use_special: включать спецсимволы
    :return: пароль
    :raises ValueError: если нет символов
    """
    characters = LETTERS
    if use_digits:
        characters += DIGITS
    if use_special:
        characters += SPECIAL_CHARS

    if not characters:
        raise ValueError("слов, доступных для пароля, нет")

    return "".join(random.choice(characters) for _ in range(length))


def save_to_file(filepath, passwords_list):
    """
    сохранить пароли в файл.

    :param filepath: путь.
    :param passwords_list: список паролей.
    """
    with open(filepath, "w", encoding="utf-8") as file:
        for pwd in passwords_list:
            file.write(pwd + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="password_generator",
        description="генерация паролей.",
    )
    parser.add_argument("-l", "--length", type=int, required=True,
                        help=f"длина от {MIN_LENGTH} до {MAX_LENGTH}")
    parser.add_argument("-c", "--count", type=int, required=True,
                        help="количество паролей")
    parser.add_argument("-d", "--no-digits", action="store_true",
                        help="нет цифр")
    parser.add_argument("-s", "--no-special", action="store_true",
                        help="нет спецсимволов")
    parser.add_argument("-f", "--file", help="файл для сохранения")
    args = parser.parse_args()

    if not (MIN_LENGTH <= args.length <= MAX_LENGTH):
        parser.error(
            f"минимальная длина {MIN_LENGTH} "
            f"максимальная длина {MAX_LENGTH}!"
        )

    suffix = ""
    if args.no_digits and args.no_special:
        suffix = " (без цифр и спецсимволов)"
    elif args.no_digits:
        suffix = " (без цифр)"
    elif args.no_special:
        suffix = " (без спецсимволов)"

    try:
        passwords = []
        for _ in range(args.count):
            pwd = generate_password(args.length,
                                    not args.no_digits,
                                    not args.no_special)
            passwords.append(pwd)

        if args.file:
            save_to_file(args.file, passwords)
            print(f"пароли сохранены в файл: {args.file}")
        else:
            for i, pwd in enumerate(passwords, 1):
                print(f"пароль такой {i}{suffix}: {pwd}")
    except ValueError as error:
        print(error)
