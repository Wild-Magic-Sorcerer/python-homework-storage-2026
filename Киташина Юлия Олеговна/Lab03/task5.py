#!/usr/bin/env python3
REPEATS = 3


def repeat(times: int):
    """
    Создаёт декоратор, который вызывает функцию times раз.

    :param times: Сколько раз вызвать функцию
    :return: Декоратор для функции
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for number in range(1, times + 1):
                print("Вызов " + str(number) + " из " + str(times)
                      + ", функция " + func.__name__)
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


@repeat(REPEATS)
def square(value: int) -> int:
    """
    Возводит число в квадрат.

    :param value: Целое число
    :return: Квадрат числа
    """
    return value * value


def main() -> None:
    """
    Вызывает декорированную функцию и печатает список результатов.
    """
    print("Результаты:", square(5))


main()
