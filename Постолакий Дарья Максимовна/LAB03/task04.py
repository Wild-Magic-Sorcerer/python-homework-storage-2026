#!/usr/bin/env python3


from functools import reduce

def filter_words_only(words_list):
    """
    Оставляет только слова, состоящие из букв.
    :param words_list: Список слов.
    :return: Список слов, состоящих только из букв.
    :rtype: List
    """
    return list(filter(lambda word_1: word_1.isalpha(), words_list))

def filter_long_words(words_list):
    """
    Оставляет слова длиной не менее 7 символов.
    :param words_list: Список слов.
    :return: Список слов длиной >= 7.
    :rtype: List
    """
    return list(filter(lambda word_2: len(word_2) >= 7, words_list))

def words_to_pairs(words_list):
    """
    Превращает слова в пары (слово, длина).
    :param words_list: Список слов.
    :return: Список кортежей (слово, длина).
    :rtype: List
    """
    return list(map(lambda word_3: (word_3, len(word_3)), words_list))

def find_longest(pairs_list):
    """
    Находит все пары с максимальной длиной слова.
    :param pairs_list: Список кортежей (слово, длина).
    :return: Список кортежей с максимальной длиной слова.
    :rtype: List
    """
    max_length = max(pair[1] for pair in pairs_list)
    return [pair for pair in pairs_list if pair[1] == max_length]

def total_letters(pairs_list):
    """
    Считает суммарное количество букв во всех словах.
    :param pairs_list: Список кортежей (слово, длина).
    :return: Суммарное количество букв.
    :rtype: Int
    """
    return reduce(lambda acc, pair: acc + pair[1], pairs_list, 0)

if __name__ == '__main__':
    user_input = input("Введите слова через пробел: ")
    words = user_input.split()

    letter_words = filter_words_only(words)
    print(f"Все слова: {letter_words}")

    long_words = filter_long_words(letter_words)
    print(f"Слова длиной не менее 7 букв: {long_words}")

    word_pairs = words_to_pairs(long_words)

    if word_pairs:
        print(f"Пары (слово, длина): {word_pairs}")

        longest = find_longest(word_pairs)
        print("Самые длинные слова:")
        for word, length in longest:
            print(f"  {word} (длина: {length})")

        total = total_letters(word_pairs)
        print(f"Суммарное количество букв: {total}")
    else:
        print("Нет подходящих слов")
