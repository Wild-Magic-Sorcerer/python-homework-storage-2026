#!/usr/bin/env python3


def hay(*args):
    integers = [a for a in args if isinstance(a, int)]
    if not integers:
        print('Целых нет, аргументы :\n')
        for a in args:
            TYPPE : str = type(a).__name__
            return -1

    res = 1
    for n in integers:
        res *= n
    return res

STANDARD_DELIMITED: str= ','
if __name__ == '__main__':
    while True:
        text = input(f'Введите значения через "{STANDARD_DELIMITED}"\n')
        parts = text.replace(',' , ' ').split()
        values = []
        for p in parts:
            try:
                values.append(int(p))
            except ValueError:
                try:
                    values.append(float(p))
                except ValueError:
                    values.append(p)
        print('Введенные значения:\n')
        for v in values:
            TYYPE : str= type(v).__name__
            print(f' {v} - {TYYPE}')

        print('Произведение:', hay(*values))
