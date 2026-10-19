#!/usr/bin/env python3


def dec_results(func):
    """
    Декоратор для вывода количества элементов в возвращаемом списке.
    
    :param func: Функция, возвращающая список
    :return: Обёрнутая функция
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"  Найдено элементов: {len(result)}")
        return result
    return wrapper


@dec_results
def filter_del_by_3_not_9(numbers: list[int]) -> list[int]:
    """
    Фильтрует числа, делящиеся на 3, но не на 9.
    
    :param numbers: Исходный список целых чисел
    :return: Список отфильтрованных чисел
    """
    return list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))


@dec_results
def filter_more_than_20(numbers: list[int]) -> list[int]:
    """
    Фильтрует числа, абсолютное значение которых больше 20.
    
    :param numbers: Исходный список целых чисел
    :return: Список отфильтрованных чисел
    """
    return list(filter(lambda x: abs(x) > 20, numbers))


@dec_results
def filter_both(numbers: list[int]) -> list[int]:
    """
    Фильтрует числа, удовлетворяющие обоим условиям одновременно.
    
    :param numbers: Исходный список целых чисел
    :return: Список отфильтрованных чисел
    """
    return list(filter(lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20, numbers))



if __name__ == "__main__":
    
    numbers: list[int] = [
        45, -12, 89, 3, -67, 102, -5, 24, 0, -99, 
        18, 76, -33, 50, -8, 15, -42, 61, 9, -100
    ]

    print(f"Исходный список из ({len(numbers)} чисел):")
    print(numbers)
    print("*" * 40)

    print("Делятся на 3, но не на 9:\n")
    result_1: list[int] = filter_del_by_3_not_9(numbers)
    print(f"  Список: {result_1}")

    print("Строго > 20:\n")
    result_2: list[int] = filter_more_than_20(numbers)
    print(f"  Список: {result_2}")

    print("Оба условия одновременно:\n")
    result_3: list[int] = filter_both(numbers)
    print(f"  Список: {result_3}")
