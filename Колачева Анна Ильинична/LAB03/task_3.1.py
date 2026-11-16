#!/usr/bin/env python3


def user_input():
    """
    Получение списка целых чисел от пользователя.

    :return: список введённых чисел
    """

    while True:
        try:
            numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
            break
        except ValueError:
            print("пожалуйста,вводите только целые числа.")
    return numbers

if __name__ == "__main__":

    lambda_number = lambda x: (
    "positive even" if x > 0 and x % 2 == 0 else
    "positive odd" if x > 0 and x % 2 != 0 else
    "negative" if x < 0 else
    "zero")

    num_list = user_input()

    for num in num_list:
        print(f'{num}: {lambda_number(num)}\n')
