#!/usr/bin/env python3
import argparse

ALLOWED_OPERATIONS = ["add", "sub", "mul", "div"]
FILE_APPEND_MODE = 'a'

def calculate(x: float, y: float, operation: str = None, precision: int = None) -> str:
    """
    Выполняет математическую операцию над двумя числами.

    x: первое позиционное число
    y: второе позиционное число
    operation: тип математической операции
    precision: количество знаков после запятой для форматирования
    return: строка с результатом вычисления или просто два числа
    """
    if operation is None:
        return f"Числа: {x}, {y}"

    if operation == "add":
        res = x + y
    elif operation == "sub":
        res = x - y
    elif operation == "mul":
        res = x * y
    elif operation == "div":
        if y == 0:
            raise ValueError("Ошибка: Деление на ноль!")
        res = x / y

    if precision is not None:
        return f"{res:.{precision}f}"

    return str(res)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Консольный калькулятор с сохранением истории.")
    parser.add_argument("x", type=float, help="Первое число")
    parser.add_argument("y", type=float, help="Второе число")

    parser.add_argument("--op", choices=ALLOWED_OPERATIONS, default=None, help="Операция")
    parser.add_argument("--precision", type=int, default=None, help="Количество знаков после запятой")
    parser.add_argument("--file", type=str, default=None, help="Имя файла для сохранения результата")

    args = parser.parse_args()

    try:
        result_str = calculate(args.x, args.y, args.op, args.precision)
        print(f"Результат: {result_str}")

        if args.file:
            with open(args.file, FILE_APPEND_MODE) as file:
                file.write(f"{result_str}\n")
            print(f"Результат успешно дописан в файл {args.file}")

    except ValueError as error:
        print(error)

