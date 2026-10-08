#!/usr/bin/env python3


if __name__ == '__main__':
    while True:
        text = input('Введите числа через запятую:\n').strip()
        parts = text.replace(',', ' ').split()


        try:
            nums = [float(p) for p in parts]
            break
        except ValueError:
            print('Введите именно числа!!\n')

    numbers = [float(p) for p in parts]

    while True:
        print('1 — по возрастанию, ')
        print('2 — по убыванию\n')
        choice = input('Выбери:\n')
        n = len(numbers)
        if choice == '1':
            for i in range(n):
                for j in range(n - 1):
                    if numbers[j] > numbers[j + 1]:
                        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            break
        elif choice == '2' :
            for i in range(n):
                for j in range(n - 1):
                    if numbers[j] < numbers[j + 1]:
                         numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            break
        else:
            print('Впишите числа 1 или 2!\n')

    print('Результат:\n', numbers)
