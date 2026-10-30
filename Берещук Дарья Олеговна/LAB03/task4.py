STANDARD_DELIMITER = " "
from functools import reduce

if __name__ == "__main__":
    raw = input(f"Введите строки через {STANDARD_DELIMITER}\n").split(STANDARD_DELIMITER)
    long_words = list(filter(lambda r: len(r) >= 7, raw))
    """оставляем только строки длиной 7 и более символов"""

    print(f"Слова строки из >=7 символов:\n{long_words}")

    pairs = list(map(lambda r: (r, len(r)), long_words))
    """делаю картежи пар строка и ее длина"""

    print(f"Пары строка-длина:\n{pairs}")

    longest = reduce(lambda a, b: a if a[1] >= b[1] else b, pairs)
    print(f"Максимальная длина - {longest[1]}")

    total_len = reduce(lambda total, lg: total + len(lg), long_words, 0)
    """суммирую все длины"""

    print(f"Суммарная длина = {total_len}")
