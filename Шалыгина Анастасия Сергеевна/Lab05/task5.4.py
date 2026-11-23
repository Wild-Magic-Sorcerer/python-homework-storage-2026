#!/usr/bin/env python3

import argparse
import os

def replace_arf(value):
    """
    Разбирает аргумент для замены в виде OLD=NEW

    :param value: Строка для замены
    :return: Кортеж(old, new) - что и на что поменять
    """
    if '=' not in value:
        raise argparse.ArgumentTypeError(
            f"Ошибка! Аргумент для заметы должен быть в формате old=new, а было получено: {value}"
        )
    parts = value.split('=', 1)
    old, new = parts[0], parts[1]
    return old, new

if __name__ == '__main__':
    def file_copy():
        """
        Главная функция копирования файлов
        Копирует содержимое входного файла в выходной с возможностью замены текста и добавления строки в конец файла
        :return: Ничего не возвращает, выполняет копирования и вывод статистики
        """
        parser = argparse.ArgumentParser(
            prog = 'Копировщик файлов',
            description = 'Копирует содержимое файла с возможностью замены текста и добавления изменений',
            epilog = 'Пример: python task5.4.py -i input.txt -o output.txt --replace "кот=собака, --append "Конец"'
        )
        parser.add_argument(
            '-i', '--input',
            type = str,
            required = True,
            help = 'Путь к входному файлу'
        )
        parser.add_argument(
            '-o', '--output',
            type = str,
            required = True,
            help = 'Путь к выходному файлу'
        )
        parser.add_argument(
            '-re', '--replace',
            type = str,
            default = None,
            help = 'Заменить все старые значения в формате "OLD=NEW'
        )
        parser.add_argument(
            '-a', '--append',
            type = str,
            default = None,
            help = 'Строка для добавления в конец выходного файла'
        )
        parser.add_argument(
            '-f', '--force',
            action = 'store_true',
            help = 'Разрешить перезапись существующего выходного файла'
        )
        args = parser.parse_args()

        if not os.path.exists(args.input):
            print(f"Ошибка!! Входной файл {args.input} не обнаружен")
            return

        if os.path.exists(args.output) and not args.force:
            print(f"Ошибка! {args.output} уже существует! Используйте --force для перезаписи.")
            return

        try:
            with open(args.input, 'r') as f:
                text = f.read()
        except Exception as e:
            print(f"Ошибка при чтении файла '{args.input}': {e}")
            return

        total_replace = 0

        if args.replace:
            old_str, new_str = args.replace
            total_replace = text.count(old_str)
            text = text.replace(old_str, new_str)

            if args.append:
                if text and not text.endswith('\n'):
                    text += '\n'
                text += args.append + '\n'

        try:
            with open (args.output, 'w') as f:
                f.write(text)
        except Exception as e:
            print(f"Ошибка при записи в файл '{args.output}': {e}")
            return

        print(f"Файл успешно записан: '{args.input}' -> '{args.output}'")

        if args.replace:
            print(f"Выполнена замена: {total_replace}")
        if args.append:
            print("Строка добавлена в конец файла")
