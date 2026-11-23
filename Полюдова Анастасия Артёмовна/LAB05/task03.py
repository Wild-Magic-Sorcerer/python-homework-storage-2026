#!/usr/bin/env python3


import argparse


CHOICES_MN = ('asc', 'desc', 'none')


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='task03',
                                    description='Скрипт, который химичит со строковыми аргументами.')

    parse.add_argument('strings', nargs='*', type=str, help='Строки')
    parse.add_argument('-c', '--count', action='store_true', help='Кол-во строк')
    parse.add_argument('-u', '--unique', action='store_true', help='Уникальные строки')
    parse.add_argument('-l', '--length', type=int, help='Минимальная длина строки')
    parse.add_argument('-s', '--sort', choices=CHOICES_MN, default='none', help='Сортировка строк')

    args = parse.parse_args()

    strings = args.strings
    count = args.count
    unique = args.unique
    min_length = args.length
    sorting = args.sort

    if not strings:
        parse.error('Неуважаемый пользователь, а список строк пуст')

    if unique:
        strings = list(dict.fromkeys(strings))

    if min_length:
        strings = [string for string in strings if len(string) >= min_length]

    match sorting:
        case 'asc':
            strings = sorted(strings)
        case 'desc':
            strings = sorted(strings, reverse=True)

    if count:
        length_of_strings = len(strings)
        print(length_of_strings)

    else:
        for string in strings:
            print(string)
