#!/usr/bin/env python3

from functools import reduce


if __name__ == "__main__":

    words: list = input("Введите слова через пробел: ").split()
        
    print(f"Исходный список из ({len(words)} слов): {words}\n")
    print("-" * 40)

    long_words: list[str] = list(filter(lambda x: len(x) >= 7, words))
    print(f"После фильтрации (длина >= 7): {long_words}\n")

    if not long_words:
        print("Нет слов нужной длины.\n")
    else:
        word_pairs = list(map(lambda x:{"word": x, "leng": len(x)}, long_words))
        print(f"Пары (слово, длина): {word_pairs}\n")

        max_word = reduce(lambda x, y: x if len(x) >= len(y) else y, long_words)
        all_let_in_fil_list = reduce(lambda all_l, word: all_l + len(word), long_words, 0)
        print(f"Самое длинное слово: {max_word}, с длиной {len(max_word)} букв\n"
            f" Сумма всех букв в отфильтрованных словах: {all_let_in_fil_list}")

