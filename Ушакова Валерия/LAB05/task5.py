#!/usr/bin/env python3


import argparse
import sys

LETTERS = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = tuple("0123456789")
SPECIAL_CHARS = tuple("!@#$%^&*()-_=+[]{};:,.<>?/")


def generate_password(length: int, use_digits: bool, use_special: bool, salt: int) -> str:
    """
    Генерирует случайный пароль на основе встроенных функций Python.

    :param length: Длина пароля.
    :param use_digits: Использовать ли цифры.
    :param use_special: Использовать ли спецсимволы.
    :param salt: Уникальное число (зерно), чтобы пароли отличались.
    :return: Строка с паролем.
    """

    characters = LETTERS

    if use_digits:
        characters += DIGITS

    if use_special:
        characters += SPECIAL_CHARS

    password = ""
    seed = salt

    for _ in range(length):
        seed = (seed * 9301 + 49297) % 233280
        index = seed % len(characters)
        password += characters[index]

    return password


def save_to_file(passwords: list[str], filename: str) -> None:
    """
    Сохраняет список паролей в файл.

    :param passwords: Список строк с паролями.
    :param filename: Имя файла для сохранения.
    :raises IOError: Если не удалось записать файл.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
    except IOError as e:
        print(f"Ошибка записи в файл: {e}", file=sys.stderr)
        sys.exit(2)


def main() -> None:
    """
    Главная функция для парсинга аргументов и запуска генерации.
    """
    parser = argparse.ArgumentParser(
        prog='password_generator',
        description='Генератор паролей',
        epilog='Пока-покааа!'
    )

    parser.add_argument('-l', '--length', type=int, required=True, help='Длина пароля (от 8 до 64)')
    parser.add_argument('-c', '--count', type=int, required=True, help='Количество паролей')

    parser.add_argument('--no-digits', action='store_true', help='Исключить цифры')
    parser.add_argument('--no-special', action='store_true', help='Исключить спецсимволы')

    parser.add_argument('-f', '--file', type=str, help='Файл для сохранения паролей')

    args = parser.parse_args()

    if args.length < 8 or args.length > 64:
        print("Ошибка: Длина пароля должна быть от 8 до 64 символов.", file=sys.stderr)
        sys.exit(2)
    if args.count <= 0:
        print("Ошибка: Количество паролей должно быть больше нуля.", file=sys.stderr)
        sys.exit(2)

    passwords = []

    use_digits = not args.no_digits
    use_special = not args.no_special

    base_salt = id(args)

    for i in range(args.count):
        pwd = generate_password(args.length, use_digits, use_special, base_salt + i)
        passwords.append(pwd)
        print(pwd)


    if args.file:
        save_to_file(passwords, args.file)
        print(f"\nПароли успешно сохранены в файл: {args.file}")


if __name__ == '__main__':
    main()
