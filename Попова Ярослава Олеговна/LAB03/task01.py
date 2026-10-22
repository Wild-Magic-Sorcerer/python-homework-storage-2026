#!/usr/bin/env python3
DELIMITER = None

def get_number_categories(numbers: list[int]) -> list[tuple[int, str]]:
    """
    Принимает список чисел и определяет их категорию с помощью лямбда-функции.
    Возвращает список пар (число, категория).
    """
    categorize = lambda x: "zero" if x == 0 else (
        "negative" if x < 0 else (
            "positive even" if x % 2 == 0 else "positive odd"
        )
    )

    return [(num, categorize(num)) for num in numbers]

if __name__ == '__main__':
    while True:
        raw = input("Введите целые числа через пробел: ")
        parts = raw.strip().split(DELIMITER)

        if not parts:
            print("Ошибка! Вы ничего не ввели")
            continue

        try:
            nums = [int(x) for x in parts]
            break
        except ValueError:
            print("Ошибка! Нужно вводить только целые числа.")

    results = get_number_categories(nums)

    print("Результаты проверки:")
    for num, category in results:
        print(f"{num} — {category}")
