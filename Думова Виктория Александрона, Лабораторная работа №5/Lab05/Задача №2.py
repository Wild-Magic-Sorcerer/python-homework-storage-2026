#!/usr/bin/env python3

import argparse
import sys

DEFAULT_PRECISION = 2
EXIT_DIV_ZERO = 2
OPERATIONS = ("add", "sub", "mul", "div")

def compute(x: float, y: float, op: str) -> float:
    """Выполняет арифметическую операцию над двумя числами.

    Args:
        x: Первый операнд.
        y: Второй операнд.
        op: Одна из операций OPERATIONS.

    Returns:
        float: Результат операции.

    Raises:
        SystemExit: Если op == 'div' и y == 0 (код EXIT_DIV_ZERO).
        ValueError: Если операция неизвестна.
    """
    if op == "add":
        return x + y
    if op == "sub":
        return x - y
    if op == "mul":
        return x * y
    if op == "div":
        if y == 0:
            print("Ошибка: деление на ноль невозможно.", file=sys.stderr)
            sys.exit(EXIT_DIV_ZERO)
        return x / y
    raise ValueError(op)

def main() -> None:
    """Разбирает аргументы CLI, вычисляет результат и сохраняет его.

    Args:
        Нет.

    Returns:
        None.

    Raises:
        SystemExit: При делении на ноль или ошибках argparse.
    """
    parser = argparse.ArgumentParser(description="Калькулятор")
    parser.add_argument("x", type=float, help="Первое число")
    parser.add_argument("y", type=float, help="Второе число")
    parser.add_argument("--operation", choices=OPERATIONS, default=None, help="Операция")
    parser.add_argument("--precision", type=int, default=DEFAULT_PRECISION, help="Количество знаков после запятой")
    parser.add_argument("--output", default=None, help="Файл для сохранения результата")
    args = parser.parse_args()

    if args.operation is None:
        print(f"x = {args.x}, y = {args.y}")
        return

    result = compute(args.x, args.y, args.operation)
    formatted = f"{result:.{args.precision}f}"
    print(f"Результат: {formatted}")

    if args.output:
        with open(args.output, "a", encoding="utf-8") as file:
            file.write(f"{args.x} {args.operation} {args.y} = {formatted}\n")

if __name__ == "__main__":
    TEST_ARGS = ["10", "5", "--operation", "div", "--precision", "3", "--output", "test_result.txt"]
    if len(sys.argv) == 1:
        print("--- Тест, что оно работает ---")
        sys.argv.extend(TEST_ARGS)
    main()
