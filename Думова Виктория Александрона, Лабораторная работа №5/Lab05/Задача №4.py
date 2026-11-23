#!/usr/bin/env python3

import argparse
import sys

EXIT_INVALID = 2
MODE_OVERWRITE = "w"
MODE_EXCLUSIVE = "x"
REPLACE_SEPARATOR = "="
FOOTER_SEPARATOR = "\n"

def main() -> None:
    """Копирует входной файл в выходной с заменами и футером.

    Args:
        Нет.

    Returns:
        None.

    Raises:
        SystemExit: Если входной файл отсутствует, --replace имеет неверный формат
            или выходной файл существует без --force.
    """
    parser = argparse.ArgumentParser(description="Копирование файла с заменами")
    parser.add_argument("--input", required=True, help="Входной файл")
    parser.add_argument("--output", required=True, help="Выходной файл")
    parser.add_argument("--replace", default=None, metavar="OLD=NEW", help="Заменить все вхождения OLD на NEW")
    parser.add_argument("--append-footer", default=None, help="Текст, добавляемый в конец выходного файла")
    parser.add_argument("--force", action="store_true", help="Разрешить перезапись существующего выходного файла")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: входной файл '{args.input}' не найден.", file=sys.stderr)
        sys.exit(EXIT_INVALID)

    replace_count = 0
    if args.replace:
        if REPLACE_SEPARATOR not in args.replace:
            print("Ошибка: --replace должен быть в формате OLD=NEW.", file=sys.stderr)
            sys.exit(EXIT_INVALID)
        old, new = args.replace.split(REPLACE_SEPARATOR, 1)
        replace_count = text.count(old)
        text = text.replace(old, new)

    if args.append_footer is not None:
        if text and not text.endswith(FOOTER_SEPARATOR):
            text += FOOTER_SEPARATOR
        text += args.append_footer
        if not text.endswith(FOOTER_SEPARATOR):
            text += FOOTER_SEPARATOR

    mode = MODE_OVERWRITE if args.force else MODE_EXCLUSIVE
    try:
        with open(args.output, mode, encoding="utf-8") as file:
            file.write(text)
    except FileExistsError:
        print(f"Ошибка: файл '{args.output}' уже существует. Используйте флаг перезаписи.", file=sys.stderr)
        sys.exit(EXIT_INVALID)

    print(f"Выполнено замен: {replace_count}")

if __name__ == "__main__":
    TEST_ARGS = ["--input", "input.txt", "--output", "output.txt", "--replace", "old=new", "--force"]
    if len(sys.argv) == 1:
        print("--- Тест, что оно работает ---")
        with open("input.txt", "w", encoding="utf-8") as f:
            f.write("Это old текст для проверки old замен.")
        sys.argv.extend(TEST_ARGS)
    main()
