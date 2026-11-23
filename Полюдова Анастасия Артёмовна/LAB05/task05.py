#!/usr/bin/env python3


import argparse
import random
import string


MIN_LENGTH = 8
MAX_LENGTH = 64


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='task05.py',
                                    description='Скрипт для генерации паролей.')
    parse.add_argument('-l', '--length', type=int, required=True, help='Длина пароля')
    parse.add_argument('-c','--count', type=int, required=True, help='Кол-во паролей')
    parse.add_argument('--no-digits', action='store_true', help='Исключение цифр')
    parse.add_argument('--no-special', action='store_true', help='Исключение специальных символов')
    parse.add_argument('-f', '--file', type=str, help='Файл для сохранения паролей')

    args = parse.parse_args()

    length = args.length
    count = args.count
    no_digits = args.no_digits
    no_special = args.no_special
    file_name = args.file

    if length < MIN_LENGTH or length > MAX_LENGTH:
        parse.error(f'Длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH}')

    if count <= 0:
        parse.error('Кол-во паролей должно быть больше 0')

    symbols = string.ascii_letters

    if not no_digits:
        symbols += string.digits

    if not no_special:
        symbols += string.punctuation

    if not symbols:
        parse.error('Недостаточно символов для генерации пароля')

    passwords = []

    for _ in range(count):
        password = ''

        for _ in range(length):
            password += random.choice(symbols)

        passwords.append(password)

    for password in passwords:
        print(password)

    if file_name:
        with open(file_name, 'a', encoding='utf-8') as file:
            for password in passwords:
                file.write(password + '\n')
