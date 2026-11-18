#!/usr/bin/env python3

import argparse

ENCODING = "utf-8"


def process_file(input_path, output_path, replace_arg, footer, force):
    """
    копирует файл с правками

    :param input_path: входной файл
    :param output_path: выходной файл
    :param replace_arg: строка OLD=NEW или None
    :param footer: строка в конец
    :param force: перезапись
    :return: количество замен
    :raises FileNotFoundError: нет входного файла
    :raises FileExistsError: выходной есть, а force=False
    :raises ValueError: неверный формат --replace
    """
    old_str = None
    new_str = None
    if replace_arg:
        if "=" not in replace_arg:
            raise ValueError("--replace должен быть в формате OLD=NEW.")
        old_str, new_str = replace_arg.split("=", 1)

    with open(input_path, "r", encoding=ENCODING) as file:
        content = file.read()

    replace_count = 0
    if old_str is not None:
        replace_count = content.count(old_str)
        content = content.replace(old_str, new_str)

    if footer:
        if not content.endswith("\n"):
            content += "\n"
        content += footer + "\n"

    mode = "w" if force else "x"
    with open(output_path, mode, encoding=ENCODING) as file:
        file.write(content)

    return replace_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="file_copier",
        description="копирование файла с заменой и футером.",
        epilog="все готово",
    )
    parser.add_argument("-i", "--input", required=True,
                        help="входной файл")
    parser.add_argument("-o", "--output", required=True,
                        help="выходной файл")
    parser.add_argument("-r", "--replace", help="замена OLD=NEW")
    parser.add_argument("-a", "--append-footer", help="строка в конец")
    parser.add_argument("-f", "--force", action="store_true",
                        help="разрешить перезаписать")
    args = parser.parse_args()

    try:
        count = process_file(args.input, args.output, args.replace,
                             args.append_footer, args.force)
        print("все супер файл обработан")
        if args.replace:
            print(f"количество замен: {count}")
    except FileNotFoundError:
        print("не вижу входного файла((")
    except FileExistsError:
        print("выходной файл уже есть")
    except ValueError as error:
        print(error)
