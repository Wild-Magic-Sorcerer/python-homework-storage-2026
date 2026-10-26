#!/usr/bin/env python3
from functools import reduce

DELIMITER = ","
MIN_LENGTH = 7


def read_strings() -> list[str]:
    """
    Запрашивает у пользователя строки через разделитель.

    :return: Список непустых строк без пробелов по краям
    """
    while True:
        text = input("Введите слова через '" + DELIMITER + "': ")
        words = []
        for word in text.split(DELIMITER):
            word = word.strip()
            if word:
                words.append(word)
        if not words:
            print("Вы ничего не ввели, попробуйте ещё раз")
            continue
        return words


def select_long(words: list[str]) -> list[str]:
    """
    Оставляет только слова длиной не менее MIN_LENGTH символов.

    :param words: Список слов
    :type words: list[str]
    :return: Список длинных слов в исходном порядке
    """
    return list(filter(lambda word: len(word) >= MIN_LENGTH, words))


def with_lengths(words: list[str]) -> list[tuple[str, int]]:
    """
    Превращает каждое слово в пару (слово, длина).

    :param words: Список слов
    :type words: list[str]
    :return: Список пар
    """
    return list(map(lambda word: (word, len(word)), words))


def longest(pairs: list[tuple[str, int]]) -> tuple[str, int]:
    """
    Находит пару с наибольшей длиной слова.

    :param pairs: Непустой список пар (слово, длина)
    :type pairs: list[tuple[str, int]]
    :return: Пара с самым длинным словом, при равенстве первая из них
    """
    return reduce(lambda best, pair: pair if pair[1] > best[1] else best,
                  pairs)


def total_length(pairs: list[tuple[str, int]]) -> int:
    """
    Считает суммарное количество букв во всех словах.

    :param pairs: Список пар (слово, длина)
    :type pairs: list[tuple[str, int]]
    :return: Сумма длин всех слов
    """
    return reduce(lambda total, pair: total + pair[1], pairs, 0)


words = read_strings()
print("Введённые слова:", words)
long_words = select_long(words)
print("Слова длиной не менее " + str(MIN_LENGTH) + " символов:", long_words)
if not long_words:
    print("Таких слов нет, считать больше нечего")
else:
    pairs = with_lengths(long_words)
    print("Пары (слово, длина):", pairs)
    best = longest(pairs)
    print("Самое длинное слово:", best[0], "длина", best[1])
    print("Суммарное количество букв:", total_length(pairs))

