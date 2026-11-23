#!/usr/bin/env python3


import argparse


MIN_AGE = 0
MAX_AGE = 120


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='task01',
                                    description='Маленький скрипт с информацией о пользователе.')
    parse.add_argument('name', type=str, help='Имя пользователя')
    parse.add_argument('-a', '--age', type=int, help='Возраст пользователя')
    parse.add_argument('-w', '--welcome', action='store_true', help='Приветствие')
    args = parse.parse_args()

    name = args.name
    age = args.age

    if age is not None:
        if age < MIN_AGE or age > MAX_AGE:
            parse.error(f'Возраст должен быть от {MIN_AGE} до {MAX_AGE}')

    if args.welcome:
        print(f'Уважаемый(ая), {name}!')

    if age is not None:
        print(f'Имя: {name}, возраст: {age}')
    else:
        print(f'Имя: {name}')
