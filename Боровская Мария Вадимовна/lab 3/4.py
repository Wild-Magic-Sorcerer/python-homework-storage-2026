#!/usr/bin/env python3

from functools import reduce


def process_words(words: list) -> None:
    """
    Обрабатывает список слов с помощью filter, map и reduce

    :param words
    :return: None
    """
    filtered = list(filter(lambda w: len(w) >= 7, words))
    print(f"После filter: {filtered}")

    if not filtered:
        print("Нет слов, подходящих под условие.")
        return

    pairs = list(map(lambda w: (w, len(w)), filtered))
    print(f"После map: {pairs}")

    longest = reduce(
        lambda a, b: a if a[1] >= b[1] else b,
        pairs,
    )
    print(f"Самое длинное слово: '{longest[0]}' ({longest[1]} букв)")

    total_letters = reduce(lambda acc, w: acc + len(w), filtered, 0)
    print(f"Суммарное количество букв: {total_letters}")


def main() -> None:
    """
    Запрашивает слова у пользователя и вызывает обработчик

    :return: None
    """
    raw_str = input("Введите слова через пробел: ").strip()

    if not raw_str:
        print("Пусто. Не получилось((")
        return

    words = raw_str.split()
    print(f"Исходный список: {words}")
    process_words(words)


main()
