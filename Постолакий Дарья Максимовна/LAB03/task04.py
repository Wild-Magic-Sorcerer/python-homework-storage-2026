#!/usr/bin/env python3


from functools import reduce

def filter_words_only(words_list):
    """
    Оставляет только слова, состоящие из букв.
    :param words_list: Список слов.
    :return: Список слов, состоящих только из букв.
    :rtype: list
    """
    return list(filter(lambda word_1: word_1.isalpha(), words_list))

def filter_long_words(words_list):
    """
    Оставляет слова длиной не менее 7 символов.
    :param words_list: Список слов.
    :return: Список слов длиной >= 7.
    :rtype: list
    """
    return list(filter(lambda word_2: len(word_2) >= 7, words_list))

def words_to_dict(words_list):
    """
    Превращает список слов в словарь: ключ — слово, значение — длина.
    :param words_list: Список слов.
    :return: Словарь {слово: длина}.
    :rtype: dict
    """
    return {w: len(w) for w in words_list}

def find_longest(words_dict):
    """
    Находит все слова с максимальной длиной.
    :param words_dict: Словарь {слово: длина}.
    :return: Словарь с самыми длинными словами.
    :rtype: dict
    """
    max_length = max(words_dict.values())
    return {w: long for w, long in words_dict.items() if long == max_length}

def total_letters(words_dict):
    """
    Считает суммарное количество букв во всех словах.
    :param words_dict: Словарь {слово: длина}.
    :return: Суммарное количество букв.
    :rtype: int
    """
    return reduce(lambda acc, l: acc + l, words_dict.values(), 0)

if __name__ == '__main__':
    user_input = input("Введите слова через пробел: ")
    words = user_input.split()

    letter_words = filter_words_only(words)
    print(f"Все слова: {letter_words}")

    long_words = filter_long_words(letter_words)
    print(f"Слова длиной не менее 7 букв: {long_words}")

    word_pairs = words_to_dict(long_words)

    if word_pairs:
        print(f"Пары (слово, длина): {word_pairs}")

        longest = find_longest(word_pairs)
        print("Самые длинные слова:")
        for word, length in longest.items():
            print(f"  {word} (длина: {length})")

        total = total_letters(word_pairs)
        print(f"Суммарное количество букв: {total}")
    else:
        print("Нет подходящих слов")
