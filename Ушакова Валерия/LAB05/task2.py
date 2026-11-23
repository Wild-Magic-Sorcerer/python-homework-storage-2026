#!/usr/bin/env python3

import argparse

DIVISION_BY_ZERO = "Ошибка: Деление на ноль невозможно!"
DEFAULT_PRECISION = 2
VALID_OPERATIONS = ('add', 'sub', 'mul', 'div')


def calculate(x: float, y: float, operation: str) -> float:
    """
    Выполняет математическую операцию над двумя числами.
    
    :param x: Первое число.
    :param y: Второе число.
    :param operation: Название операции ('add', 'sub', 'mul', 'div').
    :return: Результат операции.
    :raises ValueError: При попытке деления на ноль или неизвестной операции.
    """
    match operation:
        case 'add':
            return x + y
        case 'sub':
            return x - y
        case 'mul':
            return x * y
        case 'div':
            if y == 0:
                raise ValueError(DIVISION_BY_ZERO)
            return x / y
        case _:
            raise ValueError("Неизвестная операция!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='calculator',
        description='Калькулятор для вычисления операций над двумя числами',
        epilog='Хорошего дня!'
    )
    
    parser.add_argument('x', type=float, help='Первое число (x)')
    parser.add_argument('y', type=float, help='Второе число (y)')
    parser.add_argument('-o', '--operation', type=str, choices=VALID_OPERATIONS, help='Математическая операция')
    parser.add_argument('-p', '--precision', type=int, default=DEFAULT_PRECISION, help='Количество знаков после запятой')
    parser.add_argument('-f', '--file', type=str, help='Путь к файлу для сохранения результата')
    
    args = parser.parse_args()

    if args.operation is None:
        print(f"Вы ввели числа: x = {args.x}, y = {args.y}")
        if args.file:
            try:
                with open(args.file, 'a', encoding='utf-8') as f:
                    f.write(f"Введены числа: x = {args.x}, y = {args.y}\n")
                print(f"Результат также сохранен в файл: {args.file}")
            except IOError as e:
                print(f"Ошибка записи в файл: {e}")
                exit(2)
    else:
        try:
            result = calculate(args.x, args.y, args.operation)
        except ValueError as e:
            print(f"Ошибка: {e}")
            exit(2)

        formatted_result = f"{result:.{args.precision}f}"
        output_text = f"Результат операции {args.operation} ({args.x} и {args.y}): {formatted_result}"
        
        print(output_text)

        if args.file:
            try:
                with open(args.file, 'a', encoding='utf-8') as f:
                    f.write(output_text + "\n")
                print(f"Результат сохранен в файл: {args.file}")
            except IOError as e:
                print(f"Ошибка записи в файл: {e}")
                exit(2)
