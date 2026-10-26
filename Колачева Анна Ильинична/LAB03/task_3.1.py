#!/usr/bin/env python3


def class_number(n: int) -> str:
    """
    Классифицирует целое число.
    
    :param n: Целое число для классификации
    :return: Строка с описанием критерия числа
    """
    if n > 0:
        return "positive even" if n % 2 == 0 else "positive odd"
    elif n < 0:
        return "negative"
    return "zero"


def get_valid_list() -> list[int]:
    """
    Запрашивает у пользователя список целых чисел.
    
    :return: Список валидных целых чисел
    """
    while True:
        try:
            raw_input: str = input("Введите числа через пробел: ")
            numbers: list[int] = [int(x) for x in raw_input.split()]
            return numbers
        except ValueError:
            print("Ошибка: введите только целые числа.")


def main() -> None:
    """
    Основная программа.
    """
    numbers: list[int] = get_valid_list()
    
    results: list[tuple[int, str]] = [(n, class_number(n)) for n in numbers]
    
    print("\nРезультаты:")
    print("-" * 30)
    for num, classification in results:
        print(f"{num:>6} → {classification}")


if __name__ == "__main__":
    main()
