#!/usr/bin/env python3

import argparse

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{};:,.<>?/"

MIN_LENGTH = 8
MAX_LENGTH = 64

SEED_MULTIPLIER = 9301
SEED_INCREMENT = 49297
SEED_MODULUS = 233280


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
        seed = (seed * SEED_MULTIPLIER + SEED_INCREMENT) % SEED_MODULUS
        index = seed % len(characters)
        password += characters[index]
        
    return password


def save_to_file(passwords: list[str], filename: str) -> None:
    """
    Сохраняет список паролей в файл.
    
    :param passwords: Список строк с паролями.
    :param filename: Имя файла для сохранения.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
    except IOError as e:
        print(f"Ошибка записи в файл: {e}")
        exit(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='password_generator',
        description='Генератор паролей',
        epilog='Пока-покааа!'
    )
    
    parser.add_argument('-l', '--length', type=int, required=True, help=f'Длина пароля (от {MIN_LENGTH} до {MAX_LENGTH})')
    parser.add_argument('-c', '--count', type=int, required=True, help='Количество паролей')
    parser.add_argument('--no-digits', action='store_true', help='Исключить цифры')
    parser.add_argument('--no-special', action='store_true', help='Исключить спецсимволы')
    parser.add_argument('-f', '--file', type=str, help='Файл для сохранения паролей')
    
    args = parser.parse_args()

    if args.length < MIN_LENGTH or args.length > MAX_LENGTH:
        print(f"Ошибка: Длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH} символов.")
        exit(2)
        
    if args.count <= 0:
        print("Ошибка: Количество паролей должно быть больше нуля.")
        exit(2)

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
