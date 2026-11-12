#!/usr/bin/env python3


if __name__ == "__main__":
    
    numbers: list[int] = [
        45, -12, 89, 3, -67, 102, -5, 24, 0, -99, 
        18, 76, -33, 50, -8, 15, -42, 61, 9, -100
    ]

    print(f"Исходный список из ({len(numbers)} чисел):\n")
    print(numbers)
    print("*" * 40)

    print("Делятся на 3, но не на 9:\n")
    result_1: list[int] = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))
    print(f"Список: {result_1}")
    print(f'Длинна данного списка: {len(result_1)}\n')

    print("Строго > 20:\n")
    result_2: list[int] = list(filter(lambda x: abs(x) > 20, numbers))
    print(f"Список: {result_2}")
    print(f'Длинна данного списка: {len(result_2)}\n')

    print("Оба условия одновременно:\n")
    result_3: list[int] = list(filter(lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20, numbers))
    print(f"Список: {result_3}")
    print(f'Длинна данного списка: {len(result_3)}\n')
