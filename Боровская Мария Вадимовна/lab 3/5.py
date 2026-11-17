#!/usr/bin/env python3

def repeat(n: int):
    """
    Декоратор, который вызывает функцию n раз

    :param n
    :return: Функция-декоратор
    """
    def decorator(func):
        """
        Внутренний декоратор, принимающий функцию

        :param func
        :return: Функция-обертка (wrapper)
        """
        def wrapper(*args, **kwargs):
            """
            Обертка, выполняющая вызов функции n раз

            :param args
            :param kwargs
            :return: Список результатов всех вызовов
            """
            results = []
            for i in range(1, n + 1):
                print(f"  [Повтор {i}/{n}] Вызов {func.__name__}...")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


@repeat(3)
def square(num: int):
    """
    Возвращает квадрат числа

    :param num
    :return: Квадрат числа
    """
    return num ** 2


def main() -> None:
    """
    Запрашивает число, вызывает функцию и выводит результаты

    :return: None
    """

    while True:
        vvod = input("Введите число для возведения в квадрат: ").strip()

        if not vvod:
            print("Пусто. Не получилось((")
            continue

        try:
            num = int(vvod)
        except ValueError:
            print(f"Ошибка: '{vvod}' не является целым числом. Попробуйте еще раз.")
            continue

        results = square(num)

        print("\nСписок результатов:")
        for idx, val in enumerate(results, start=1):
            print(f"  {idx}) {val}")


main()
