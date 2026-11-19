#!/usr/bin/env python3
DELIMITER = ","


def read_integers() -> list[int]:
    """
    Запрашивает у пользователя целые числа через разделитель.

    Слова, которые не являются целыми числами, пропускаются с сообщением.

    :return: Список целых чисел, введённых пользователем
    """
    while True:
        text = input("Введите целые числа через '" + DELIMITER + "': ")
        numbers = []
        for word in text.split(DELIMITER):
            word = word.strip()
            if not word:
                continue
            try:
                numbers.append(int(word))
            except ValueError:
                print("Пропущено:", word, "- это не целое число")
        if not numbers:
            print("Ни одного целого числа не введено, попробуйте ещё раз")
            continue
        return numbers


def classify_all(numbers: list[int]) -> list[str]:
    """
    Применяет лямбда-функцию классификации к каждому числу списка.

    :param numbers: Список целых чисел
    :return: Список строк с результатом для каждого числа
    """
    return list(map(lambda n: "zero" if n == 0 else "negative" if n < 0
                    else "positive even" if n % 2 == 0 else "positive odd",
                    numbers))


def main() -> None:
    """
    Читает числа, классифицирует каждое и печатает результат.
    """
    numbers = read_integers()
    labels = classify_all(numbers)
    for number, label in zip(numbers, labels):
        print(number, "-", label)


main()
