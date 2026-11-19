#!/usr/bin/env python3
import argparse
import random
import string

MIN_LENGTH = 8
MAX_LENGTH = 64
FILE_WRITE_MODE = 'w'

def generate_passwords(length: int, count: int, no_digits: bool, no_specials: bool) -> list[str]:
    """
    Генерирует список случайных паролей по заданным правилам.

    length: длина каждого пароля
    count: количество паролей для генерации
    no_digits: флаг исключения цифр
    no_specials: флаг исключения специальных символов
    return: список сгенерированных паролей
    """
    pool = string.ascii_letters

    if not no_digits:
        pool += string.digits

    if not no_specials:
        pool += string.punctuation

    if not pool:
        raise ValueError("Генерация невозможна: исключены все доступные символы.")

    passwords = []
    for _ in range(count):
        pwd = "".join(random.choices(pool, k=length))
        passwords.append(pwd)

    return passwords


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Генератор надежных паролей.")
    parser.add_argument("length", type=int, help="Длина пароля (от 8 до 64)")
    parser.add_argument("count", type=int, help="Количество паролей для генерации")
    parser.add_argument("--no-digits", action="store_true", help="Исключить цифры из пароля")
    parser.add_argument("--no-specials", action="store_true", help="Исключить спецсимволы из пароля")
    parser.add_argument("--file", type=str, default=None, help="Файл для сохранения паролей")

    args = parser.parse_args()

    if not (MIN_LENGTH <= args.length <= MAX_LENGTH):
        parser.error(f"Длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH} символов.")

    try:
        result_passwords = generate_passwords(args.length, args.count, args.no_digits, args.no_specials)

        print(f"Сгенерировано паролей: {args.count}")
        for p in result_passwords:
            print(p)

        if args.file:
            with open(args.file, FILE_WRITE_MODE) as file:
                for p in result_passwords:
                    file.write(f"{p}\n")
            print(f"\nПароли успешно сохранены в файл: {args.file}")

    except ValueError as e:
        parser.error(str(e))

