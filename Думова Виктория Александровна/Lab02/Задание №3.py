#!/usr/bin/env python3

def type_el(*arg):
    for i in arg:
        print(f' у этого элемента {i}, тип : {type(i)}\n')

def product_of_ints(*args):
    int_args = [x for x in args if type(x) is int]
    if not int_args:
        print("Целочисленных аргументов не найдено. Переданные значения и их типы:\n")
        type_el(*args)
        return None
    result = 1
    for num in int_args:
        result *= num
    return result

if __name__ == "__main__":
    print(product_of_ints(2, 3, 4))  # 24
    print(product_of_ints(2, "abc", 3.5, 5))  # 10
    print(product_of_ints("hello", 3.14, [1, 2]))  # None + вывод типов
    print(product_of_ints())  # None + пустой вывод
