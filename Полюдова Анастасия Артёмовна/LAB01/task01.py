#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '


def function(value: list[int]):
    return len(value) == len(set(value))


def same(value: list[int]):
    return [number for number in set(value) if value.count(number) > 1]

if __name__ == '__main__':
    all_is_fine: bool = True

    while all_is_fine:
        try:
            pishite: str = input('Введи числа через пробел:').strip()

            if not pishite:
                print('Неправильно, попробуй еще раз')
            else:
                chisla: list[int] = [int(number) for number in pishite.split(STANDARD_DELIMITED)]
                all_is_fine = False

        except ValueError:
            print('Неправильно, введи только целые числа')

    if function(chisla):
        print('Все числа различны')
    else:
        double: list[int] = same(chisla)
        print('Есть повторы:', double)
