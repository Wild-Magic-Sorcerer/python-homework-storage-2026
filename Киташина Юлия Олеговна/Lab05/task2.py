#!/usr/bin/env python3
import argparse
from io import SEEK_END
from pathlib import Path


def calculate(x: float, y: float, operation: str) -> float:
    """Выполняет выбранную арифметическую операцию.

    :param x: Левый операнд
    :param y: Правый операнд
    :param operation: Операция add, sub, mul или div
    :return: Результат вычисления
    """
    if operation == "add":
        return x + y
    if operation == "sub":
        return x - y
    if operation == "mul":
        return x * y
    if operation == "div":
        if y == 0:
            raise ValueError("Делить на ноль нельзя")
        return x / y
    raise ValueError("Неизвестная операция")


def append_result(path: Path, result: str) -> None:
    """Добавляет одну строку в историю вычислений.

    :param path: Путь к файлу истории
    :param result: Результат с заданной точностью
    :return: Ничего не возвращает (None)
    """
    with path.open("a+b") as history:
        separator = b""
        if history.tell() > 0:
            history.seek(-1, SEEK_END)
            if history.read(1) not in (b"\n", b"\r"):
                separator = b"\n"
        history.write(separator + result.encode("utf-8") + b"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Вычисления с двумя числами.")
    parser.add_argument("x", type=float, help="первое число")
    parser.add_argument("y", type=float, help="второе число")
    parser.add_argument("--operation", choices=("add", "sub", "mul", "div"))
    parser.add_argument("--precision", type=int, help="знаки после запятой")
    parser.add_argument("--output", type=Path, help="файл истории")
    args = parser.parse_args()

    if args.precision is not None and args.precision < 0:
        parser.error("Точность должна быть неотрицательной")
    if args.operation is None:
        print(args.x, args.y)
    else:
        try:
            result = calculate(args.x, args.y, args.operation)
        except ValueError as error:
            parser.error(str(error))
        line = str(result)
        if args.precision is not None:
            line = f"{result:.{args.precision}f}"
        if args.output is not None:
            try:
                append_result(args.output, line)
            except OSError as error:
                parser.error(f"Не удалось записать историю: {error}")
        print(line)
