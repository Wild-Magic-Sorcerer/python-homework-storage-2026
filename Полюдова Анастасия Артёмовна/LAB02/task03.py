#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '


def func3(*args):
    result: int = 1
    check_int: bool = False

    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            result *= arg
            check_int = True

    if check_int:
        return result

    for arg in args:
        print(arg, '-', type(arg))

    return None


if __name__ == '__main__':
    text: str = input('Введите какие-то аргументы: ').strip()

    if not text:
        print('Пустовато..')
    else:
        result_1: list = []

        for var_1 in text.split(STANDARD_DELIMITED):
            try:
                var_2 = int(var_1)
            except ValueError:
                try:
                    var_2 = float(var_1)
                except ValueError:
                    var_2 = var_1

            result_1.append(var_2)

        result_2 = func3(*result_1)

        if result_2 is not None:
            print('Произведение:', result_2)
