#!/usr/bin/env python3
WITH_INTEGERS = (2, "abc", 3.5, 4, True)
WITHOUT_INTEGERS = ("abc", 1.5, None)


def product_of_integers(*args):
    product = 1
    count = 0
    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            product *= arg
            count += 1
    if count == 0:
        print("Целых чисел нет, вот что было передано:")
        for arg in args:
            print(arg, type(arg))
        return None
    return product


for values in (WITH_INTEGERS, WITHOUT_INTEGERS):
    print("Аргументы:", values)
    answer = product_of_integers(*values)
    if answer is not None:
        print("Произведение целых чисел:", answer)
