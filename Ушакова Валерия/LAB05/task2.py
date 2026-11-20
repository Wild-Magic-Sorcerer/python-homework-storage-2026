#!/usr/bin/env python3


import argparse
import sys

# Константы для операций (чтобы не было магических чисел)
DIVISION_BY_ZERO = "Ошибка: Деление на ноль невозможно!"


def calculate(x: float, y: float, operation: str) -> float:
    """
    Выполняет математическую операцию над двумя числами.

    :param x: Первое число.
    :param y: Второе число.
    :param operation: Название операции ('add', 'sub', 'mul', 'div').
    :return: Результат операции.
    :raises ValueError: При попытке деления на ноль или неизвестной операции.
    """
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        if y == 0:
            raise ValueError(DIVISION_BY_ZERO)
        return x / y
    else:
        raise ValueError("Неизвестная операция!")


def main() -> None:
    """
    Главная функция для парсинга аргументов и вывода результата.
    """
    parser = argparse.ArgumentParser(
        prog='calculator',
        description='Калькулятор для вычисления операций над двумя числами',
        epilog='Хорошего дня!'
    )

    # Позиционные аргументы (обязательные)
    parser.add_argument('x', type=float, help='Первое число (x)')
    parser.add_argument('y', type=float, help='Второе число (y)')

    # Необязательный аргумент операции
    parser.add_argument(
        '-o', '--operation',
        type=str,
        choices=['add', 'sub', 'mul', 'div'],
        help='Математическая операция: add (сложить), sub (вычесть), mul (умножить), div (разделить)'
    )

    # Аргумент точности (по умолчанию 2 знака)
    parser.add_argument(
        '-p', '--precision',
        type=int,
        default=2,
        help='Количество знаков после запятой (по умолчанию 2)'
    )

    # Аргумент для сохранения в файл
    parser.add_argument(
        '-f', '--file',
        type=str,
        help='Путь к файлу, куда будет сохранен результат'
    )

    args = parser.parse_args()

    # Если операция не указана, просто выводим числа
    if args.operation is None:
        print(f"Вы ввели числа: x = {args.x}, y = {args.y}")
        if args.file:
            try:
                with open(args.file, 'a', encoding='utf-8') as f:
                    f.write(f"Введены числа: x = {args.x}, y = {args.y}\n")
                print(f"Результат также сохранен в файл: {args.file}")
            except IOError as e:
                print(f"Ошибка записи в файл: {e}", file=sys.stderr)
                sys.exit(2)
        return

    # Выполняем операцию
    try:
        result = calculate(args.x, args.y, args.operation)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(2)

    # Форматируем вывод в зависимости от точности
    formatted_result = f"{result:.{args.precision}f}"
    output_text = f"Результат операции {args.operation} ({args.x} и {args.y}): {formatted_result}"

    print(output_text)

    # Сохраняем в файл, если он указан
    if args.file:
        try:
            # Открываем файл в режиме 'a' (append) - добавление в конец, без перезаписи!
            with open(args.file, 'a', encoding='utf-8') as f:
                f.write(output_text + "\n")
            print(f"Результат сохранен в файл: {args.file}")
        except IOError as e:
            print(f"Ошибка записи в файл: {e}", file=sys.stderr)
            sys.exit(2)


if __name__ == '__main__':
    main()
