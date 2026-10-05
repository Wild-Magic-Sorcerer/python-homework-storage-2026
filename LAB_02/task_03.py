#!/usr/bin/env python3

def different_arguments(numbers):
    integer = []
    not_integer = []

    for argument in numbers:
        if type(argument) == int:
            integer.append(argument)
        else:
            not_integer.append(argument)

    if integer:
        result = 1
        for num in integer:
            result *= num
        return result
    else:
        return not_integer


def print_result(result):
    if type(result) == int:
        print(f"Произведение целых чисел равно {result}")
    elif len(result) == 0:
        print("Спсиок пуст.")
    else: 
        print("В списке отсутсвуют целые числа. Нецелые аргументы: ")
        for item in result:
            print(f"{item} - тип: {type(item)}")


def analise_str(user_input):
    user_input = user_input.replace(",", " ")
    string_list = user_input.split()

    if len(string_list) == 0:
        return []

    result = []
    for item in string_list:
        try: 
            result.append(int(item))
        except ValueError:
            result.append(item)
    return result 

if __name__ == '__main__':
    print("Напишите значения. Например: 2 привет 56.0473 True пупупу")
    user_input = input("Введите данные: ")
    numbers = analise_str(user_input)
    print(f"Распознанные числа: {numbers}")
    result = different_arguments(numbers)
    print_result(result)
