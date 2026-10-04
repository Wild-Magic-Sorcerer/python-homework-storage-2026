#!/usr/bin/env python3
def multiply_ints(*args):
    ints = [x for x in args if isinstance(x, int) and not isinstance(x, bool)]
    if not ints:
        print("Целочисленных аргументов нет.\nПолученные значения:")
        for value in args:
            print(f"{value!r} — тип {type(value).__name__}")
        return None
    result = 1
    for number in ints:
        result *= number
    return print(f"Произведение целочисленных аргументов: {result}")


if __name__ == '__main__':
    result = multiply_ints(2, "abc", 3.5, 4, [1, 2])
    result = multiply_ints("abc", 3.5, [1, 2])
