#!/usr/bin/env python3
DELIMITER = " "


def to_number(text):
    try:
        return int(text)
    except ValueError:
        return float(text)


def merge_sort(numbers, descending):
    if len(numbers) <= 1:
        return numbers
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle], descending)
    right = merge_sort(numbers[middle:], descending)
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if descending:
            take_left = left[i] >= right[j]
        else:
            take_left = left[i] <= right[j]
        if take_left:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


def read_numbers():
    while True:
        text = input("Введите числа через пробел: ")
        words = []
        for word in text.split(DELIMITER):
            if word:
                words.append(word)
        if not words:
            print("Вы ничего не ввели, попробуйте ещё раз")
            continue
        numbers = []
        try:
            for word in words:
                numbers.append(to_number(word))
        except ValueError:
            print("Ошибка:", word, "- это не число, попробуйте ещё раз")
            continue
        return numbers


def read_order():
    while True:
        order = input("1 - по возрастанию, 2 - по убыванию. Ваш выбор: ")
        if order == "1" or order == "2":
            return order
        print("Ошибка: введите 1 или 2")


def main():
    numbers = read_numbers()
    order = read_order()
    ordered = merge_sort(numbers, order == "2")
    line = ""
    for number in ordered:
        line += str(number) + DELIMITER
    print("Результат:", line.strip())


if __name__ == "__main__":
    main()
