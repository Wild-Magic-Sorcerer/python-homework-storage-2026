#!/usr/bin/env python3

import argparse

LENGTH_BARRIER = 15
ASCENDING_ORDER = "asc"
DESCENDING_ORDER = "desc"

def filter_strings(lst, unique, min_length):
    """
    Оставляет в списке строк только уникальные строки подходящей длины.
    :param lst: Исходный список строк.
    :param unique: Флаг, отбирающий только уникальные строки, если включён.
    :param min_length: Минимальная подходящая длина строки.
    :return: Отфильтрованный список строк.
    """
    long_strings = []
    for string in lst:
        if len(string) > min_length:
            long_strings.append(string)
    if unique == "yes":
        str_set = set(long_strings)
        return list(str_set)
    return long_strings

def sort_strings(lst, sort_choice):
    """
    Сортирует список заданным способом.
    :param lst: Исходный список строк.
    :param sort_choice: Способ сортировки списка (по возрастанию, по убыванию или никак).
    :return: Отсортированный список строк.
    """
    if sort_choice == ASCENDING_ORDER:
        lst.sort(key = str)
    elif sort_choice == DESCENDING_ORDER:
        lst.sort(key = str, reverse = True)
    return lst

if "__main__" == __name__:
    parser = argparse.ArgumentParser(prog = "strings_sort", description = "Скрипт, сортирующий и фильтрующий данный список строк", epilog = "Всё отфильтровано!")
    parser.add_argument("strings", nargs = "+", help = "Одна или несколько строк")
    parser.add_argument("-u", "--unique", type = str, choices = ("yes", "no"), default = "no", help = "Флаг уникальности строк")
    parser.add_argument("-m", "--min_len", type = int, default = LENGTH_BARRIER, help = "Минимальная длина строки")
    parser.add_argument("-s", "--sort", choices = (ASCENDING_ORDER, DESCENDING_ORDER, None), help = "Способ сортировки")
    args = parser.parse_args()
    if not args.strings:
        raise argparse.ArgumentError(args.strings, "Введите хоть какие-то строки!")
    else:
        filtered_strings = filter_strings(args.strings, args.unique, args.min_len)
        result = sort_strings(filtered_strings, args.sort)
        for some_str in result:
            print(some_str)
        print(f"Длина итогового списка строк: {len(result)}.")
