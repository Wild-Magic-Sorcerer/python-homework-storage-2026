#!/usr/bin/env python3

import argparse

def valid_precision(value):
    """
    Функция, которая проверяет значение точности

    :param value: Строка из командной строки
    :return: Значение точности
    """
    try:
        precision = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Вышла ошибка. {value} - явно не число.")

    if precision < 0:
        raise argparse.ArgumentTypeError("Ошибка! Тут должно быть положительное число!")

    return precision

if __name__ == '__main__':

    def calculate_script():
        """
        Функция калькулятора. Разделяет аргументы, выполняет операцию и выводит/сохраняет результат

        :return: Ничего не возвращает, выводит результат на экран и/или записывает в файл
        """
        parser = argparse.ArgumentParser(
            prog = 'Калькулятор',
            description = 'Простой калькулятор с возможностью сохранения результата в файл',
            epilog = 'Пример: python task5.2.py 10 5 -o add -p 2 -f result.txt'
        )

        parser.add_argument(
            'x',
            type = float,
            help = 'Первое число'
        )
        parser.add_argument(
            'y',
            type = float,
            help = 'Второе число'
        )

        parser.add_argument(
            '-o', '--operation',
            choise = ['add', 'sub', 'mul', 'div'],
            help = 'Операции: add (сложение), sub (вычитание), mul (умножение), div (деление)',
        )
        parser.add_argument(
            '-p', '--precision',
            type = valid_precision,
            default = 2,
            help = 'Количество знаков после запятой (по умолчанию 2)'
        )
        parser.add_argument(
            '-f', '--file',
            type = str,
            default = None,
            help ='Имя файла для сохранения результата'
        )

        args = parser.parse_args()

        if args.operation is None:
            result_text = f"Числа: х = {args.x}, y = {args.y} "
            print(result_text)

            if args.file:
                with open(args.file, 'a', encoding='utf-8') as f:
                    f.write(result_text + '\n')
                print(f"Результат сохранен в файл '{args.file}'")
            return

        x = args.x
        y = args.y
        op = args.operation

        if op == 'div' and y == 0:
            print("Ошибка! Делить на 0 нельзя!")
            return

        operations = {
            'add': ('+', x + y),
            'sub': ('-', x - y),
            'mul': ('*', x * y),
            'div': ('/', x / y),
        }
        symbol, result = operations[op]
        formated_result = f"Результат:.{args.precision}"

        result_text = f"{x} {symbol} {y} = {formated_result}"
        print(result_text)

        if args.file:
            with open (args.file, 'a', encoding='utf-8') as f:
                f.write(result_text + '\n')
            print(f"Результат дописан в файл '{args.file}'")
