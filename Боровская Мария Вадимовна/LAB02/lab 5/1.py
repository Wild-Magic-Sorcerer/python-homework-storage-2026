#!/usr/bin/env python3

import argparse

MIN_AGE = 0
MAX_AGE = 120


def age_check(value):
    """
    проверяет возраст

    :param value: строка от пользователя
    :return: целое число
    :raises argparse.ArgumentTypeError: если не число или вне диапазона
    """
    try:
        age = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' не целое число")
    if not (MIN_AGE <= age <= MAX_AGE):
        raise argparse.ArgumentTypeError(
            f"возраст от {MIN_AGE} до {MAX_AGE}"
        )
    return age


def generate_greeting(name, age=None, formally=False):
    """
    собирает строку приветствия

    :param name: имя пользователя
    :param age: возраст или None
    :param formally: формальное обращение
    :return: готовая строка приветствия
    """
    prefix = "Уважаемый(ая)" if formally else "Привет"
    if age is None:
        return f"{prefix}, {name}!"
    return f"{prefix}, {name}! Тебе {age} лет."


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="greeting_script",
        description="Скрипт для приветствия пользователя.",
        epilog="Всего хорошего!",
    )
    parser.add_argument("name", help="Имя пользователя")
    parser.add_argument("-a", "--age", type=age_check,
                        help=f"Возраст {MIN_AGE}–{MAX_AGE}")
    parser.add_argument("-g", "--formally", action="store_true",
                        help="Формальное приветствие")
    args = parser.parse_args()

    print(generate_greeting(args.name, args.age, args.formally))
