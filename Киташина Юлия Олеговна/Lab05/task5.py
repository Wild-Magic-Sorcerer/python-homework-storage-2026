#!/usr/bin/env python3
import argparse
import os
import secrets
import string
import sys
from pathlib import Path
from typing import TextIO


def write_passwords(length: int, count: int, alphabet: str,
                    stream: TextIO) -> None:
    """Генерирует и записывает по одному паролю на строку.

    :param length: Длина каждого пароля
    :param count: Число паролей
    :param alphabet: Разрешённые символы
    :param stream: Терминал или открытый для записи файл
    :return: Ничего не возвращает (None)
    """
    for _ in range(count):
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        print(password, file=stream)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор паролей.")
    parser.add_argument("--length", type=int, required=True, help="длина")
    parser.add_argument("--count", type=int, default=1, help="количество")
    parser.add_argument("--no-digits", action="store_true", help="без цифр")
    parser.add_argument("--no-special", action="store_true", help="без знаков")
    parser.add_argument("--output", type=Path, help="сохранить в новый файл")
    args = parser.parse_args()

    if not 8 <= args.length <= 64:
        parser.error("Длина пароля должна быть от 8 до 64")
    if args.count <= 0:
        parser.error("Количество паролей должно быть положительным")
    alphabet = string.ascii_letters
    if not args.no_digits:
        alphabet += string.digits
    if not args.no_special:
        alphabet += string.punctuation
    if not alphabet:
        parser.error("Для генерации не осталось разрешённых символов")

    if args.output is None:
        write_passwords(args.length, args.count, alphabet, sys.stdout)
    else:
        try:
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
            descriptor = os.open(args.output, flags, 0o600)
            with os.fdopen(descriptor, "w", encoding="utf-8") as target:
                write_passwords(args.length, args.count, alphabet, target)
        except FileExistsError:
            parser.error("Файл для паролей уже существует")
        except OSError as error:
            parser.error(f"Не удалось сохранить пароли: {error}")
