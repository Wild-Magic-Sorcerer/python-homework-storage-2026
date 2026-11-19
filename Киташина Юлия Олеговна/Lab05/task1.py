#!/usr/bin/env python3
import argparse


def read_age(text: str) -> int:
    """Проверяет возраст, переданный в командной строке.

    :param text: Значение аргумента --age
    :return: Целое число от 0 до 120
    """
    message = "Возраст должен быть целым числом от 0 до 120"
    try:
        age = int(text)
    except ValueError:
        raise argparse.ArgumentTypeError(message) from None
    if not 0 <= age <= 120:
        raise argparse.ArgumentTypeError(message)
    return age


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Вывести имя и возраст.")
    parser.add_argument("name", help="имя пользователя")
    parser.add_argument("--age", type=read_age, help="возраст от 0 до 120")
    parser.add_argument("--greet", action="store_true", help="приветствие")
    args = parser.parse_args()

    message = f"Уважаемый(ая) {args.name}" if args.greet else args.name
    if args.age is not None:
        message += f", возраст: {args.age}"
    print(message)
