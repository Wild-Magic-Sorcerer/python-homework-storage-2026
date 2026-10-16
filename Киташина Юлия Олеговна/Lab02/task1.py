#!/usr/bin/env python3
DELIMITER = " "


def average_length(strings):
    total = 0
    for s in strings:
        total += len(s)
    return total / len(strings)


def longer_than_average(strings):
    if not strings:
        return []
    average = average_length(strings)
    result = []
    for s in strings:
        if len(s) > average:
            result.append(s)
    return result


def read_strings():
    while True:
        text = input("Введите строки через пробел: ")
        words = []
        for word in text.split(DELIMITER):
            if word:
                words.append(word)
        if not words:
            print("Вы ничего не ввели, попробуйте ещё раз")
            continue
        return words


def main():
    strings = read_strings()
    print("Средняя длина:", round(average_length(strings), 2))
    longer = longer_than_average(strings)
    if not longer:
        print("Таких строк нет")
    else:
        print("Строки длиннее средней:", longer)


if __name__ == "__main__":
    main()
