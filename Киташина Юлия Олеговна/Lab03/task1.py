#!/usr/bin/env python3
DELIMITER = ","


def read_integers() -> list[int]:
    """
    Запрашивает у пользователя целые числа через разделитель.

    :return: Список целых чисел, введённых пользователем
    """
    while True:
        text = input("Введите целые числа через '" + DELIMITER + "': ")
        words = []
        for word in text.split(DELIMITER):
            word = word.strip()
            if word:
                words.append(word)
        if not words:
            print("Вы ничего не ввели, попробуйте ещё раз")
            continue
        numbers = []
        try:
            for word in words:
                numbers.append(int(word))
        except ValueError:
            print("Ошибка:", word, "- это не целое число, попробуйте ещё раз")
            continue
        return numbers


def classify_all(numbers: list[int]) -> list[str]:
    """
    Применяет лямбда-функцию классификации к каждому числу списка.

    :param numbers: Список целых чисел
    :type numbers: list[int]
    :return: Список строк с результатом для каждого числа
    """
    return list(map(lambda n: "zero" if n == 0 else "negative" if n < 0
                    else "positive even" if n % 2 == 0 else "positive odd",
                    numbers))


numbers = read_integers()
labels = classify_all(numbers)
for number, label in zip(numbers, labels):
    print(number, "-", label)
