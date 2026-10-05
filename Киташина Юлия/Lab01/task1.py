#!/usr/bin/env python3

def all_different(numbers):
    seen = []
    for number in numbers:
        if number in seen:
            return False
        seen.append(number)
    return True


text = input("Введите числа через пробел: ")

try:
    numbers = []
    for item in text.split():
        numbers.append(float(item))

    if len(numbers) == 0:
        print("Вы не ввели числа.")
    elif all_different(numbers):
        print("Все числа различны.")
    else:
        print("Есть одинаковые числа.")
except ValueError:
    print("Ошибка: нужно вводить только числа.")
