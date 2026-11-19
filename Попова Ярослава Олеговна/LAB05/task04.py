#!/usr/bin/env python3
import argparse
import re

READ_MODE = 'r'
WRITE_OVERWRITE_MODE = 'w'
WRITE_SAFE_MODE = 'x'
ERROR_EXIT_CODE = 2

def process_file_content(text: str, replace_rule: str = None, footer: str = None) -> tuple[str, int]:
    """
    Обрабатывает текст: выполняет замену строк и добавляет подвал.

    text: исходный текст из файла
    replace_rule: правило замены в формате OLD=NEW
    footer: текст для добавления в конец файла
    return: кортеж из обработанного текста и количества выполненных замен
    """
    replacements_count = 0

    if replace_rule is not None and "=" in replace_rule:
        old_str, new_str = replace_rule.split("=", maxsplit=1)
        replacements_count = len(re.findall(old_str, text))
        text = re.sub(old_str, new_str, text)

    if footer is not None:
        text += f"\n{footer}"

    return text, replacements_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Утилита для копирования и изменения файлов.")

    parser.add_argument("--input", type=str, required=True, help="Путь к входному файлу")
    parser.add_argument("--output", type=str, required=True, help="Путь к выходному файлу")

    parser.add_argument("--replace", type=str, default=None, help="Замена в формате OLD=NEW")
    parser.add_argument("--append-footer", type=str, default=None, help="Текст для добавления в конец")
    parser.add_argument("--overwrite", action="store_true", help="Разрешить перезапись выходного файла")

    args = parser.parse_args()

    try:
        with open(args.input, READ_MODE, encoding='utf-8') as in_file:
            content = in_file.read()
    except FileNotFoundError:
        parser.error(f"Входной файл '{args.input}' не найден.")

    processed_content, count = process_file_content(content, args.replace, args.append_footer)

    out_mode = WRITE_OVERWRITE_MODE if args.overwrite else WRITE_SAFE_MODE

    try:
        with open(args.output, out_mode, encoding='utf-8') as out_file:
            out_file.write(processed_content)
    except FileExistsError:
        parser.error(f"Выходной файл '{args.output}' уже существует. Используйте --overwrite.")

    print(f"Файл успешно скопирован в '{args.output}'.")
    print(f"Количество выполненных замен: {count}")

