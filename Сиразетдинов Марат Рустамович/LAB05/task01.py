import argparse

MIN_AGE = 0
MAX_AGE = 120


def age_verify(value):
    """
    выполняет проверку возраста
    :param value:
    :return: целое число
    :raise: поднимает argparse.ArgumentTypeError если число не в диапазоне или не целое
    """
    try:
        age = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f'Возраст должен быть целым числом, вы написали: {value}'
        )

    if not (MIN_AGE <= age <= MAX_AGE):
        raise argparse.ArgumentTypeError(
            f'Возраст должен быть в диапазоне {MIN_AGE}–{MAX_AGE}, ввы написали: {age}'
        )

    return age


def greeting_creator(name, age, formally):
    """
    собирает строку приветствия
    :param name: имя пользователя
    :param age: возраст или none
    :param formally: формальное обращение
    :return: собранное обращение
    """
    prefix = 'Уважаемый(ая) ' if formally else 'Привет, '
    greeting = f'{prefix}{name}!'

    if age is not None:
        greeting += f' Ваш возраст: {age}!'

    return greeting


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт для приветствия пользователя')
    parser.add_argument('name', help='Имя пользователя')
    parser.add_argument('--age', type=age_verify, help=f'Возраст пользователя от {MIN_AGE} до {MAX_AGE} лет')
    parser.add_argument('--formally', action='store_true', help='Флаг официального приветствия')
    args = parser.parse_args()

    print(greeting_creator(args.name, args.age, args.formally))
