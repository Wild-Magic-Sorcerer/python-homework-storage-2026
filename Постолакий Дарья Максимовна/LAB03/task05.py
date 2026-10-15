#!/usr/bin/env python3


def repeat(n):
    """
    Декоратор: вызывает функцию n раз и возвращает список результатов.
    :param n: Сколько раз вызывать функцию.
    :return: Декоратор, оборачивающий функцию.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(1, n + 1):
                print(f"Запуск {i} из {n}: вызываю {func.__name__}")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def double(x):
    """
    Удваивает число.
    :param x: Число.
    :return: X * 2.
    :rtype: int
    """
    return x * 2

if __name__ == '__main__':
    result = double(5)
    print(f"Результат: {result}")
