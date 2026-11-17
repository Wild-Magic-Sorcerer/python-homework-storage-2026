#!/usr/bin/env python3


if __name__ == '__main__':
    check = lambda x: (
        "positive even" if x > 0 and x % 2 == 0
        else "positive odd" if x > 0
        else "negative" if x < 0
        else "zero"
    )

    user_input = input("Введите целые числа через пробел:\n")
    for token in user_input.split():
        try:
            number = int(token)
        except ValueError:
            continue
        print(f"{number}: {check(number)}")
