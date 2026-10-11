#!/usr/bin/env python3


def fact_rec(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)


def fact_iter(n: int):
    result: int = 1

    for i in range(2, n + 1):
        result *= i

    return result


if __name__ == '__main__':
    value: str = input('Введите целое число: ').strip()

    if not value:
        print('Пустовато..')
    else:
        try:
            number: int = int(value)

            if number < 0:
                print('Не нужно вводить отрицательное число')
            else:
                result_1: int = fact_rec(number)
                result_2: int = fact_iter(number)
                print('Рекурсивный метод:', result_1)
                print('Итеративный метод:', result_2)

        except ValueError:
            print('Нужно ввести целое число')
