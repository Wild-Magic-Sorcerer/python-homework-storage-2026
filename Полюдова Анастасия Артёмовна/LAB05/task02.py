#!/usr/bin/env python3


import argparse


CHOICES_MN = ('add', 'sub', 'mul', 'div')
PRECISION_MN = 1


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='task02',
                                    description='Программа с операциями над двумя числами.')
    parse.add_argument('x', type=float, help='Первое число')
    parse.add_argument('y', type=float, help='Второе число')
    parse.add_argument('-o', '--operation', choices=CHOICES_MN, help='Операции над числами')
    parse.add_argument('-p', '--precision', type=int, default=PRECISION_MN, help='Кол-во знаков после запятой')
    parse.add_argument('-f', '--file', type=str, help='Файл, куда сохраняем')

    args = parse.parse_args()

    x = args.x
    y = args.y
    operation = args.operation
    precision = args.precision
    file_name = args.file

    if operation:
        match operation:
            case 'add':
                result = x + y
            case 'sub':
                result = x - y
            case 'mul':
                result = x * y
            case 'div':
                if y == 0:
                    parse.error('Деление на ноль невозможно')
                result = x / y

        final_result = f'{result:.{precision}f}'
        print(f'Результат: {final_result}')

        if file_name:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(f'{x} {operation} {y} = {final_result}\n')

    else:
        print(f'x = {x}')
        print(f'y = {y}')
