import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт, который приветствует пользователя')
    parser.add_argument('name', help='Имя пользователя')
    parser.add_argument('--age', type=int, default=None, help='Возраст пользователя')
    parser.add_argument('--officially', action='store_true', help='Официальное приветствие')

    args = parser.parse_args()

    if args.age is not None:
        if 0 <= args.age <= 120:
            if args.officially:
                print(f'Уважаемый(ая) {args.name}! Тебе {args.age} лет.')
            else:
                print(f'Привет, {args.name}! Тебе {args.age} лет.')
        else:
            parser.error(f'Возраст должен быть от 0 до 120!')
    else:
        if args.officially:
            print(f'Уважаемый(ая) {args.name}!')
        else:
            print(f'Привет, {args.name}!')
