#!/usr/bin/env python3

import argparse

DEFAULT_PRECISION = 2
OPERATIONS = ("add", "sub", "mul", "div")


def calculate(x, y, operation):
    """
    считает

    :param x: первое число
    :param y: второе число
    :param operation: add / sub / mul / div
    :return: результат
    :raises ValueError: деление на ноль или неизвестная операция
    """
    match operation:
        case "add":
            return x + y
        case "sub":
            return x - y
        case "mul":
            return x * y
        case "div":
            if y == 0:
                raise ValueError("деление на ноль невозможно!")
            return x / y
        case _:
            raise ValueError(f"неизвестная операция: {operation}")


def save_result(filepath, text):
    """
    дописывает результат в файл

    :param filepath: путь к файлу
    :param text: текст
    """
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(text + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="calculator_script",
        description="калькулятор с сохранением истории.",
        epilog="удачных вычислений!",
    )
    parser.add_argument("x", type=float, help="первое число")
    parser.add_argument("y", type=float, help="второе число")
    parser.add_argument("-o", "--operation", choices=OPERATIONS,
                        help="операция: add, sub, mul, div")
    parser.add_argument("-p", "--precision", type=int,
                        default=DEFAULT_PRECISION,
                        help="знаков после запятой")
    parser.add_argument("-f", "--file", help="файл для сохранения")
    args = parser.parse_args()

    if not args.operation:
        print(f"x = {args.x}, y = {args.y}")
    else:
        try:
            result = calculate(args.x, args.y, args.operation)
            line = f"{result:.{args.precision}f}"
            print(line)
            if args.file:
                save_result(args.file, line)
                print(f"результат в файле: {args.file}")
        except ValueError as error:
            print(f"ошибка вычисления: {error}")
