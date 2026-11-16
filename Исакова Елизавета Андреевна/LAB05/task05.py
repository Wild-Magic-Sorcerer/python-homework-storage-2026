import argparse
import random
import string

MIN_LENGTH = 8
MAX_LENGTH = 64

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Генератор паролей')

    parser.add_argument('length', type=int, help=f'Длина пароля (от {MIN_LENGTH} до {MAX_LENGTH})')
    parser.add_argument('count', type=int, help='Количество паролей')
    parser.add_argument('--no-number', action='store_true', help='Исключить цифры')
    parser.add_argument('--no-special', action='store_true', help='Исключить спецсимволы')
    parser.add_argument('--output', help='Файл для сохранения паролей')

    args = parser.parse_args()

    if not (MIN_LENGTH <= args.length <= MAX_LENGTH):
        parser.error(f'Длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH}!')

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

    suffix = ""
    if args.no_number and args.no_special:
        suffix = " (без цифр и спецсимволов)"
    elif args.no_number:
        suffix = " (без цифр)"
    elif args.no_special:
        suffix = " (без спецсимволов)"

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
        print(f'Пароли записаны в "{args.output}"')
    else:
        for i, pwd in enumerate(passwords, 1):
            print(f"Пароль {i}{suffix}: {pwd}")
            
