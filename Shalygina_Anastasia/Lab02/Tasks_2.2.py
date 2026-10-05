#!/usr/bin/env python3

STANDARD_DELIMITED: str = ";"

def number():
    while True:
        user_number: str = input(f'Введите числа, используя "{STANDARD_DELIMITED}"\n')
        try:
            numbers = [float(num.strip().replace(',','.')) for num in user_number.split(STANDARD_DELIMITED) if num.strip()]

            if not numbers:
                print("Плохо! Вы ничего не ввели!")
                continue
            return numbers
        except ValueError:
            print('Плохо!! Введите числа, разделенными точкой с запятой!')

def sort_numbers(numberses, increasing = True):
    if increasing:
        return sorted(numberses)
    else:
        return sorted(numberses, reverse=True)

if __name__ == '__main__':
    numbers = number()
    print(f'Исходный список: {numbers}')
    while True:
        choice = input("Выберите тип сортировки: \n 1 - по возрастанию \n 2 - по убыванию \n")
        if choice == '1':
            result = sort_numbers(numbers, increasing=True)
            print(f'Поздравляю! Список чисел отсортирован по возрастанию: {result}')
            break
        elif choice == '2':
            result = sort_numbers(numbers, increasing=False)
            print(f'Поздравляю! Список чисел отсортирован по убыванию: {result}')
            break
        else:
            print("Плохо!! Выбор был ошибочным! Необходимо выбрать 1 или 2!")
