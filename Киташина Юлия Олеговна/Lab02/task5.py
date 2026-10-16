#!/usr/bin/env python3


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def read_number():
    while True:
        text = input("Введите целое число: ")
        try:
            number = int(text)
        except ValueError:
            print("Ошибка:", text, "- это не целое число, попробуйте ещё раз")
            continue
        if number < 0:
            print("Ошибка: факториал отрицательного числа не определён")
            continue
        return number


def main():
    number = read_number()
    recursive = factorial_recursive(number)
    iterative = factorial_iterative(number)
    print("Рекурсивно:", recursive)
    print("Итеративно:", iterative)
    if recursive == iterative:
        print("Результаты совпадают")
    else:
        print("Результаты не совпадают")


if __name__ == "__main__":
    main()
