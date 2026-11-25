#!/usr/bin/env python3

import argparse

MIN_AGE = 0
MAX_AGE = 120
CHECK_FAIL = "wrong"

def users_age(value):
    """
    Проверяет, входит ли возраст пользователя в данный диапазон возрастов.
    :param value: Возраст пользователя.
    :return: Возраст пользователя, если он соответствует требованиям.
    :raises argparse.ArgumentError: Если возраст не лежит в данном диапазоне.
    """
    try:
        new_value = int(value)
    except ValueError:
        raise argparse.ArgumentError(f"{value} - некорректный возраст, так как это не целое число.")
    if new_value < MIN_AGE or new_value > MAX_AGE:
        return CHECK_FAIL
    return new_value

def introduction(name, age):
    """
    Уважительно приветствует пользователя.
    :param name: Имя пользователя.
    :param age: Возраст пользователя.
    :return: Строка с приветствием пользователя.
    """
    return f"Уважаемый(ая) {name} {age} лет от роду, приветствуем Вас."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "user_introduction", description = "Скрипт, приветствующий пользователя", epilog = "Рады встрече с Вами.")
    parser.add_argument("name", type = str, help = "Имя пользователя")
    parser.add_argument("-a", "--age", type = int, help = "Возраст пользователя")
    parser.add_argument("-i", "--introduction", type = str, default = None, help = "Формальное приветствие")
    args = parser.parse_args()
    new_age = users_age(args.age)
    if new_age == CHECK_FAIL:
        raise argparse.ArgumentError(args.age, "Введите не любое число, а число из данного диапазона.")
    if args.introduction:
        final_string = introduction(args.name, new_age)
        print(final_string)
