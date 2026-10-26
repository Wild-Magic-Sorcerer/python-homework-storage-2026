#!/usr/bin/env python3

from functools import reduce

def user_input(text: str) -> list:
    """
    Запрашивает у пользователя данные в виде строки, преобразуя в список разделяя по пробелу 

    :param text: текст, который выводится пользователю
    :return: список из строки
    """
    znach: list = input(text).split()
    return znach

def main() -> None:
    """
    Основная программа.
    """
    
    words: list = user_input("Введите слова через пробел: ")
    
    print(f"Исходный список из ({len(words)} слов): {words}\n")
    print("-" * 40)

    long_words: list[str] = list(filter(lambda x: len(x) >= 7, words))
    print(f"После фильтрации (длина >= 7): {long_words}\n")

    if not long_words:
        print("Нет слов нужной длины.\n")
        return

    word_pairs: list[tuple[str, int]] = list(map(lambda x: (x, len(x)), long_words))
    print(f"Пары (слово, длина): {word_pairs}\n")

    max_pair: tuple[str, int] = reduce( lambda accum, list_el: list_el if list_el[1] > accum[1] else accum, word_pairs)
    print(f"Слово с максимальной длиной: '{max_pair[0]}' ({max_pair[1]} букв)\n")

    total_letters: int = reduce(lambda accum, list_el: accum + list_el[1], word_pairs, 0 )
    print(f"Суммарное количество букв во всех отфильтрованных словах: {total_letters}")


if __name__ == "__main__":
    main()
