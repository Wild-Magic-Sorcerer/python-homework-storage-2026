#!/usr/bin/env python3


import argparse
import sys


def parse_replace_arg(replace_str: str) -> tuple[str, str]:
    """
    Парсит аргумент замены формата 'OLD=NEW'.

    :param replace_str: Строка формата 'OLD=NEW'.
    :return: Кортеж из двух строк (old_text, new_text).
    :raises ValueError: Если в аргументе нет знака '='.
    """
    if "=" not in replace_str:
        raise ValueError(f"Неверный формат замены: '{replace_str}'. Ожидается OLD=NEW")

    old_text, new_text = replace_str.split("=", 1)
    return old_text, new_text


def main() -> None:
    """
    Главная функция для запуска утилиты.

    :raises SystemExit: Если файлы не найдены или произошла ошибка чтения/записи (код 2).
    """
    parser = argparse.ArgumentParser(
        description="Утилита для копирования и замены текста",
        epilog="Всего хорошего!"
    )

    parser.add_argument("--input", required=True, help="Исходный файл")
    parser.add_argument("--output", required=True, help="Файл для сохранения")

    parser.add_argument("--replace", help="Замена текста в формате OLD=NEW")
    parser.add_argument("--append-footer", help="Текст для добавления в конец")
    parser.add_argument("-f", "--force", action="store_true", help="Принудительная перезапись")

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input}' не найден.", file=sys.stderr)
        sys.exit(2)
    except IOError as e:
        print(f"Ошибка чтения файла: {e}", file=sys.stderr)
        sys.exit(2)

    if args.replace:
        try:
            old, new = parse_replace_arg(args.replace)
            content = content.replace(old, new)
            print(f"Выполнена замена: '{old}' на '{new}'")
        except ValueError as e:
            print(f"Ошибка: {e}", file=sys.stderr)
            sys.exit(2)

    if args.append_footer:
        content += "\n" + args.append_footer

    mode = 'w' if args.force else 'x'

    try:
        with open(args.output, mode, encoding='utf-8') as f_out:
            f_out.write(content)
        print(f"Копирование успешно завершено в файл '{args.output}'.")
    except FileExistsError:
        print(f"Ошибка: Файл '{args.output}' уже существует. Используйте -f/--force для перезаписи.", file=sys.stderr)
        sys.exit(2)
    except IOError as e:
        print(f"Ошибка записи в файл: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
