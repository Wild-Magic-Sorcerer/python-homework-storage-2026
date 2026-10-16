#!/usr/bin/env python3
VOWELS = "аеёиоуыэюяaeiou"


def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in VOWELS:
            count += 1
    return count


def strings_with_vowels(**kwargs):
    result = {}
    for name, value in kwargs.items():
        if isinstance(value, str) and count_vowels(value) >= 3:
            result[name] = value
    return result


def main():
    first = strings_with_vowels(word="привет", animal="крокодил",
                                city="ОкЕаН", number=5)
    second = strings_with_vowels(word="кот", number=10, flag=True)
    for selected in (first, second):
        if not selected:
            print("Подходящих аргументов нет")
        else:
            print("Подходящие аргументы:", selected)


if __name__ == "__main__":
    main()
