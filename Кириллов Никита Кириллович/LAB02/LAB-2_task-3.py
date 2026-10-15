'''
Задание №3 Создайте функцию, которая принимает произвольное количество аргументов любых типов и возвращает их
произведение (только целочисленных аргументов). Если целочисленные аргументы не были поданы, программа должна
выдать эти значения и указать их тип.
'''

from functools import reduce


def multi_ints(*args):
    only_ints = [x for x in args if type(x) is int]

    if not only_ints:
        return {arg: type(arg) for arg in args}

    product = reduce(lambda acc, x: acc * x, only_ints, 1)
    return product


if __name__ == '__main__':
    user_answer = input("Введите числа и слова через пробел: ").split()

    for item in user_answer:
        try:
            number = int(item)
            user_data.append(number)
        except ValueError:
            try:
                float_number = float(item)
                user_data.append(float_number)
            except ValueError:
                user_data.append(item)

        result = multi_ints(*user_data)

        print(f"Результат: {result}")
