#!/usr/bin/env python3

from functools import reduce

DELIMITER = None

def w_statistic(words: list[str]) -> tuple:
    """
    Фильтрует слова, преобразует их в кортежи и вычисляет статистику.
    Возвращает промежуточные и итоговые результаты.
    """
    filtered = list(filter(lambda w: len(w) >= 7, words))

    if not filtered:
        return [], [], None, 0

    mapped = list(map(lambda w: {"word": w, "length": len(w)}, filtered))

    max_word = reduce(lambda acc, x: acc if acc["length"] >= x["length"] else x, mapped)

    total_letters = reduce(lambda acc, x: acc + x["length"], mapped, 0)

    return filtered, mapped, max_word, total_letters

if __name__ == '__main__':

    while True:
        raw = input("Введите список слов: ")
        parts = raw.strip().split(DELIMITER)

        if not parts:
            print("Вы ничего не ввели! Попробуйте снова.")
            continue
        break

    res_filtered, res_mapped, res_max, res_total = w_statistic(parts)

    print(f"Отфильтрованные слова (>= 7 символов): {res_filtered}")
    print(f"Преобразованные в пары (слово, длина): {res_mapped}")

    if not res_filtered:
        print("Нет слов, удовлетворяющих условию (длина >= 7).")
    else:
        print(f"Слово с максимальной длиной: '{res_max['word']}' (длина {res_max['length']})")
        print(f"Суммарное количество букв: {res_total}")
