import argparse
import secrets
import string

MIN_LENGTH = 8
MAX_LENGTH = 64
SPECIAL_CHARS = '!@#$%^&*()-_=+[]{};:,.<>?'


def generate_passwords(length, count, no_digits, no_special):
    """
    Генерирует список случайных паролей
    :param length:длина каждого пароля
    :param count:кол-во паролей для генерации
    :param no_digits:флаг исключения цифр в пароле
    :param no_special:флаг исключения специальных знаков в пароле
    :return:
    """
    alphabet = string.ascii_letters

    if not no_digits:
        alphabet += string.digits

    if not no_special:
        alphabet += SPECIAL_CHARS

    if not alphabet:
        raise ValueError('Не осталось доступных символов для генерации пароля')

    passwords = []
    for _ in range(count):
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        passwords.append(password)

    return passwords


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скрипт для генерации случайных паролей'
    )
    parser.add_argument('--length', type=int, default=12, help='длина пароля (от 8 до 64)')
    parser.add_argument('--count', type=int, default=1, help='количество паролей для генерации')
    parser.add_argument('--no-digits', action='store_true', help='исключить цифры из пароля')
    parser.add_argument('--no-special', action='store_true', help='исключить специальные символы из пароля')
    parser.add_argument('--output', help='путь к файлу для сохранения паролей')
    args = parser.parse_args()

    if not (MIN_LENGTH < args.length < MAX_LENGTH):
        parser.error(f'Длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH}')

    if args.count < 1:
        parser.error('Количество паролей должно быть больше нуля')

    try:
        generated = generate_passwords(args.length, args.count, args.no_digits, args.no_special)
    except ValueError as error:
        parser.error(str(error))

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write('\n'.join(generated) + '\n')
        print(f'Пароли сохранены в файл: {args.output}')
    else:
        for pwd in generated:
            print(pwd)