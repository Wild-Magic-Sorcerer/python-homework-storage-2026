import argparse
import random
import string
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Генератор паролей')

    parser.add_argument('length', type=int, help='Длина пароля (от 8 до 64)')
    parser.add_argument('count', type=int, help='Количество паролей')
    parser.add_argument('--no-number', action='store_true', help='Исключить цифры')
    parser.add_argument('--no-special', action='store_true', help='Исключить спецсимволы')
    parser.add_argument('--output', help='Файл для сохранения паролей')
    
    args = parser.parse_args()

    if args.length > 64 or args.length < 8:
        parser.error('Длина пароля должна быть от 8 до 64!')

    symbols = string.ascii_letters

    if not args.no_number:
        symbols += string.digits

    if not args.no_special:
        symbols += string.punctuation

    if len(symbols) == 0:
        parser.error('Нельзя сгенерировать пароль!')

    passwords = []
    for _ in range(args.count):
        password = ''.join(random.choice(symbols) for _ in range(args.length))
        passwords.append(password)

    if args.output:
        if os.path.exists(args.output):
            parser.error(f'Файл "{args.output}" уже существует!')

        with open(args.output, 'w', encoding='utf-8') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
        print(f'Пароли записаны в "{args.output}"')
    else:
        for pwd in passwords:
            print(pwd)
