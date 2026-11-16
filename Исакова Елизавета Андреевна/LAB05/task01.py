import argparse

MIN_AGE = 0
MAX_AGE = 120

def age_check(value):
    """
    Проверяет, что возраст является целым числом в диапазоне от MIN_AGE до MAX_AGE.
    :param value: Строка, введенная пользователем.
    :return: Целое число (возраст).
    :raises argparse.ArgumentTypeError: Если число не целое или вне диапазона.
    """
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f'Ожидалось целое число, получено: {value}')

    if not (MIN_AGE <= ivalue <= MAX_AGE):
        raise argparse.ArgumentTypeError(f'Возраст должен быть от {MIN_AGE} до {MAX_AGE}')

    return ivalue

def generate_greeting(name, age=None, formal_greeting=False):
    """
    Формирует строку приветствия.
    :param name: Имя пользователя.
    :param age: Возраст пользователя (может быть не передан).
    :param formal_greeting: Флаг, использовать ли формальное приветствие.
    :return: Строка приветствия.
    """
    prefix = 'Уважаемый(ая)' if formal_greeting else 'Привет'
    if age is not None:
        return f'{prefix} {name}! Тебе {age} лет.'
    return f'{prefix} {name}!'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт, который приветствует пользователя')
    parser.add_argument('name', help='Имя пользователя')
    # Передаем функцию age_check как тип, чтобы argparse сам проверял возраст
    parser.add_argument('--age', type=age_check, default=None, help='Возраст пользователя')
    parser.add_argument('--officially', action='store_true', help='Официальное приветствие')

    args = parser.parse_args()

    print(generate_greeting(args.name, args.age, args.officially))
    
