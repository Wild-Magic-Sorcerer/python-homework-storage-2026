#!/usr/bin/env python3


import argparse


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='task04.py',
                                    description='Копирование содержимого одного файла в другой.')
    parse.add_argument('-i', '--input', required=True, help='Входной файл')
    parse.add_argument('-o', '--output', required=True, help='Выходной файл')
    parse.add_argument('-r', '--replace', help='Замена строки в формате OLD=NEW')
    parse.add_argument('-a', '--append-footer', help='Добавление строки в конец файла')
    parse.add_argument('--rewrite', action='store_true', help='Перезапись выходного файла')

    args = parse.parse_args()

    input_file = args.input
    output_file = args.output
    replace = args.replace
    footer = args.append_footer
    rewriting = args.rewrite

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

    except FileNotFoundError:
        parse.error('Входного файла нет')

    replace_count = 0
    if replace:
        if '=' in replace:
            old, new = replace.split('=', 1)
            replace_count = text.count(old)
            text = text.replace(old, new)
        else:
            parse.error('Неверный формат замены')

    if footer:
        text += '\n' + footer

    if rewriting:
        mode = 'w'
    else:
        mode = 'x'

    try:
        with open(output_file, mode, encoding='utf-8') as file:
            file.write(text)

    except FileExistsError:
        parse.error('Выходной файл уже существует.')

    print(f'Кол-во выполненных замен: {replace_count}')
