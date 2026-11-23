#!/usr/bin/env python3

import argparse
import random

LETTERS = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
NUMBERS = '0123456789'
SPECIALS = '!@#$%^&*()-_=+[]{}|:;,.<>?'

def generate_password(length, count, no_digits, no_special):
    """
    Генерирует список паролей на основе заданных параметров

    :param length: Длина одного пароля
    :param count: Количество паролей для генераций
    :param no_digits: Флаг исключающий цифры
    :param no_special: Флаг исключающий специальные символы
    :return: Список сгенерированных паролей. Пустой список, если генерация невозможна
    """
    char_pool = LETTERS
    if not no_digits:
        char_pool += NUMBERS
    if not no_special:
        char_pool += SPECIALS

    if not char_pool:
        print("Ошибка! Невозможно сгенерировать пароль, тк не осталось допустимых символов")
        return []

    passwords = []
    for _ in range(count):
        password = ''.join(random.choice(char_pool) for _ in range(length))
        passwords.append(password)
    return passwords


if __name__ == '__main__':

    def password_generator():
        """
        Деление аргументов, проверка длины, генерация паролей и вывод их

        :return: Ничего не возвращает, выводит результат на экран и/или в файл
        """
        parser = argparse.ArgumentParser(
            prog = 'Генератор паролей',
            description = 'Инструмент для генерации случайных паролей',
            epilog = 'python task5.5.py -l 12 -n 3 --no-digits -f pass.txt',
        )

        parser.add_argument(
            '-l', '--length',
            type = int,
            required = True,
            help = 'Длина пароля (целое число от 8 до 64'
        )
        parser.add_argument(
            '-n', '--count',
            type = int,
            required = True,
            help = 'Количество паролей для генерации'
        )
        parser.add_argument(
            '--no-digits',
            action = 'store_true',
            help = 'Исключить цифры из пароля'
        )
        parser.add_argument(
            '--no-special',
            action = 'store_true',
            help = 'Исключить специальные символы из пароля'
        )
        parser.add_argument(
            '-f', '--file',
            typy = str,
            default = None,
            help = 'Путь к файлу для сохранения паролей'
        )

        args = parser.parse_args()

        if not (8<=args.length<=64):
            print(f"Ошибка! Длина пароля должна быть от 8 до 64 символов, а вы ввели: {args.length}")
            return

        passwords = generate_password(args.length, args.count, args.no_digits, args.no_special)

        if not passwords:
            return

        print(f"Сгенерировано {args.count} пароль(ей) длиной: {args.length} символов")
        print('--'*40)
        for pwd in passwords:
            print(pwd)
        print('--'*40)

        if args.file:
            try:
                with open(args.file, 'w') as f:
                    for pwd in passwords:
                        f.write(f"{pwd}\n")
                print(f"Пароль(и) успешно сохранены в файл: {args.file}")
            except Exception as e:
                print(f"Ошибка при сохранении в файл: {e}")
