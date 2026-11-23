#!/usr/bin/env python3

import argparse

def bubble_sort(str_list, reverse = False):
    """
    Сортировка методом пузырька

    :param str_list: Список строк для сортировки
    :param reverse: Параметр сортировки по убыванию (desc) или по возрастанию (asc)
    :return: Новый отсортированный список слов
    """
    arr = str_list.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if reverse:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':

    def str_process():
        """
        Разделение аргументов, применение фильтров, сортировки

        :return: Ничего не возвращает, выводит результат на экран
        """
        parser = argparse.ArgumentParser(
            prog = 'Обработчик строк',
            description = 'Обработка строк с фильтрацией и сортировкой',
            epilog = 'Пример: python task5.3.py Привет Мир --unique --sort asc --min-length 4'
        )
        parser.add_argument(
            'strings',
            nargs = '*',
            type = str,
            help = 'Одна или несколько строк обработок'
        )

        parser.add_argument(
            '-c', '--count',
            action = 'store_true',
            help = 'Вывести только количество строк после фильтрации'
        )

        parser.add_argument(
            '-u', '--unique',
            action = 'store_true',
            help = 'Оставить только уникальные строки'
        )

        parser.add_argument(
            '-m', '--min-length',
            type = int,
            default = 0,
            help = 'Минимальная длина строки для фильтрации'
        )

        parser.add_argument(
            '-s', '--sort',
            type = str,
            default = 'none',
            help = 'Сортировка asc (по возрастанию), desc (по убыванию), none (без сортировки)'
        )

        args = parser.parse_args()

        if not args.strings:
            print("Ошибка! Введите, пожалуйста, хоть что-то")
            return

        if args.sort not in ['asc', 'desc', 'none']:
            print(f"Ошибка: Неизвестное значение сортировки '{args.sort}'"
                  f"Выберите asc, desc, none!")
            return

        result = args.strings

        if args.min_length > 0:
            result = [s for s in result if len(s) >= args.min_length]

        if args.unique:
            result = list(set(result))

        if args.sort == 'asc':
            result = bubble_sort(result, reverse = False)
        elif args.sort == 'desc':
            result = bubble_sort(result, reverse = True)

        if args.count:
            print(f"Количество строк: {len(result)}")
        else:
            for line in result:
                print(line)
