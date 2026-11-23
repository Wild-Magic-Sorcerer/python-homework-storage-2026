#!/usr/bin/env python3

import argparse

def valid_age(value):
    """
    Функция, которая будет проверять возраст: является ли вводимое значение целым числом в диапазоне от 0 до 120

    :param value: Строка из командной строки
    :return: Возраст
    """
    try:
        age = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Ошибка!! Возраст может быть только целым числом. Взгляни еще раз: {value} - это не оно!")
    if not 0 <= age <= 120:
        raise argparse.ArgumentTypeError("Возраст может быть в диапазоне от 0 до 120.")
    return age


if __name__ == '__main__':
    def greeting_script():
        """
        Разделение аргументов командной строки. Выводит приветствие в консоль

        :return: Ничего не возвращает, выводит результат на экран
        """

        parser = argparse.ArgumentParser(
            prog = 'Приветствие',
            description = 'Выводит приветствие для пользователя',
            epilog = 'Пример: python task5.1.py Анастасия -a 23, -g'
        )
        parser.add_argument(
            '-a', '--age',
            type = valid_age,
            default = None,
            help = 'Возраст пользователя (целое число от 0 до 120)'
        )
        parser.add_argument(
            '-g', '--greeting',
            action = 'store_true',
            help = 'Сделать приветствие более официальным ("Уважаемый(ая)")'
        )
        args = parser.parse_args()

        if args.greeting:
            greeting_word = "Уважаемый(ая)"
        else:
            greeting_word = "Привет"

        if args.age is not None:
            print (f"{greeting_word}, {args.name}! Вам {args.age} лет")
        else:
            print(f"{greeting_word}, {args.name}!")
