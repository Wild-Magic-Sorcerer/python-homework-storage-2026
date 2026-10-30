import random


def generate_numbers():
    """
    Генерирует список из 20 случайных целых чисел от -100 до 100
    :return: Список случайных целых чисел
    """
    return [random.randint(-100, 100) for i in range(20)]


def filter_divisible_3_not_9(numbers):
    """
    Отбирает числа, которые делятся на 3, но не делятся на 9
    :param numbers: Исходный список целых чисел
    :return: Отфильтрованный список целых чисел
    """
    return list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))


def filter_abs_more_than_20(numbers):
    """
    Отбирает числа, абсолютное значение которых больше 20
    :param numbers: Исходный список целых чисел
    :return: Отфильтрованный список целых чисел
    """
    return list(filter(lambda x: abs(x) > 20, numbers))


def filter_both_conditions(numbers):
    """
    Отбирает числа, удовлетворяющие обоим условиям фильтрации
    :param numbers: Исходный список целых чисел
    :return: Отфильтрованный список целых чисел
    """
    return list(filter(lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20, numbers))


def print_results(title, filtered_list):
    """
    Выводит заголовок с длиной списка и сам список элементов
    :param title: Заголовок для вывода результатов
    :param filtered_list: Список отфильтрованных целых чисел
    :return:
    """
    print(f"\n{title} (длина {len(filtered_list)}):")
    print(filtered_list)


def main():
    """
    Основная управляющая функция программы
    :return:
    """
    numbers = generate_numbers()
    print(f"Исходный список чисел:\n{numbers}")

    divisible_3_not_9 = filter_divisible_3_not_9(numbers)
    more_than_20 = filter_abs_more_than_20(numbers)
    both = filter_both_conditions(numbers)

    print_results("Делятся на 3, но не на 9", divisible_3_not_9)
    print_results("Абсолютное значение > 20", more_than_20)
    print_results("Удовлетворяют обоим условиям", both)


if __name__ == "__main__":
    main()
