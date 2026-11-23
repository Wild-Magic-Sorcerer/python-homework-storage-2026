#!/usr/bin/env python3

import argparse

MIN_AGE = 0
MAX_AGE = 120
GREETING_FORMAL = "Уважаемый(ая) {}, здравствуйте!"
GREETING_CASUAL = "Привет, {}"


def validate_age(age: int) -> None:
    """
    Проверяет корректность возраста.

    :param age: Возраст пользователя.
    :raises ValueError: Если возраст не входит в диапазон от 0 до 120.
    """
    if age < MIN_AGE or age > MAX_AGE:
        raise ValueError(f"Возраст должен быть от {MIN_AGE} до {MAX_AGE}. Вы ввели: {age}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='greeter',
        description='Я скрипт, который приветствует человека',
        epilog='Всего хорошего!'
    )

    parser.add_argument('name', type=str, help='Имя пользователя')
    parser.add_argument('--age', type=int, help='Возраст пользователя')
    parser.add_argument('-g', '--greet', action='store_true', help='Официальное приветствие')

    args = parser.parse_args()

    if args.age is not None:
        try:
            validate_age(args.age)
        except ValueError as e:
            print(f"Ошибка: {e}")
            exit(2)

    if args.greet:
        greeting = GREETING_FORMAL.format(args.name)
    else:
        greeting = GREETING_CASUAL.format(args.name)

    if args.age is not None:
        print(f"{greeting} Вам {args.age} лет.")
    else:
        print(greeting)

