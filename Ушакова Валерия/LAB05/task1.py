#!/usr/bin/env python3


import argparse
import sys


def create_parser() -> argparse.ArgumentParser:
    """
    Создает и настраивает парсер аргументов командной строки.

    :return: Настроенный объект ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        prog='greeter',
        description='Я скрипт, который приветствует человека',
        epilog='Всего хорошего!'
    )

    parser.add_argument('name', type=str, help='Имя пользователя')
    "Обязательный позиционный аргумент"

    parser.add_argument('--age', type=int, help='Возраст пользователя (от 0 до 120)')
    "Необязательный аргумент возраста"

    parser.add_argument('-g', '--greet', action='store_true', help='Официальное приветствие')
    "Флаг официального приветствия"
    return parser


def validate_age(age: int) -> None:
    """
    Проверяет корректность возраста.

    :param age: Возраст пользователя.
    :raises ValueError: Если возраст не входит в диапазон от 0 до 120.
    """
    if age < 0 or age > 120:
        raise ValueError(f"Возраст должен быть от 0 до 120. Вы ввели: {age}")


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()


    if args.age is not None:
        try:
            validate_age(args.age)
        except ValueError as e:
            print(f"Ошибка: {e}", file=sys.stderr)
            sys.exit(2)


    if args.greet:
        greeting = f"Уважаемый(ая) {args.name}, здравствуйте!"
    else:
        greeting = f"Привет, {args.name}"

    if args.age is not None:
        print(f"{greeting}, вам {args.age}.")
    else:
        print(f"{greeting}.")
