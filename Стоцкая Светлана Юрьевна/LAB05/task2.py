#!/usr/bin/env python3

import argparse

ACCURACY = 2

def operations(operation, value_1, value_2):
    """
    Вычисляет результат простейших арифметических операций для двух чисел.
    :param operation: Та операция, которую нужно провести.
    :param value_1: Первое число.
    :param value_2: Второе число.
    :return: Результат сложения, вычитания, умножения или деления чисел.
    :raises ValueError: Если происходит деление на ноль или данная операция не определена.
    """
    if operation == "add":
        return value_1 + value_2
    elif operation == "sub":
        return value_1 - value_2
    elif operation == "mul":
        return value_1 * value_2
    elif operation == "div":
        if value_2 == 0:
            raise ValueError("На ноль делить нельзя!")
        return value_1 / value_2
    else:
        raise ValueError(f"Данная операция {operation} не определена.")

def save_to_file(some_file, value):
    """
    Записывает результат проведённой арифметической операции в конец файла.
    :param some_file: Путь до файла.
    :param value: Результат операции, который надо записать в файл.
    :return: None
    """
    with open(some_file, "a") as file:
        file.write(f"В результате было получено {value}." +"\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "simple_math", description = "Скрипт для выполнения простейших арифметических операций с двумя числами", epilog = "Посчитали всё, что нужно!")
    parser.add_argument("x", type = float, help = "Первое число")
    parser.add_argument("y", type = float, help = "Второе число")
    parser.add_argument("-o", "--operation", type = str, default = None,
        choices = ["add", "sub", "mul", "div", None], help = "Операции сложения, вычитания, умножения и деления")
    parser.add_argument("-a", "--accuracy", type = int, default = ACCURACY, help = "Количество знаков после запятой")
    parser.add_argument("-f", "--file", type = str, help = "Путь до файла для сохранения результата операции")
    args = parser.parse_args()
    if args.operation:
        result = operations(args.operation, args.x, args.y)
    else:
        print(f"x = {args.x}, y = {args.y}")
