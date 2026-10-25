#!/usr/bin/env python3

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    user_input = input("Введите целое неотрицательное число: ").strip()
    try:
        n = int(user_input)
    except ValueError:
        print(f"Ошибка: '{user_input}' не является целым числом.")

    if n < 0:
        print("Ошибка: число должно быть неотрицательным.")

    print(f"Рекурсивно: {n}! = {factorial_recursive(n)}")
    print(f"Итеративно: {n}! = {factorial_iterative(n)}")
