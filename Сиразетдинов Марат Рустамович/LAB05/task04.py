import argparse


def process_content(content, replace_pair, footer):
    """
    Обрабатывает содержимое файла, выполняет замену строк
    :param content:исходный текст из файла
    :param replace_pair: строка в формате OLD=NEW или none
    :param footer:строка для добавления в конец файла
    :return:кол-во выполненных замен, обработанный текст
    """
    result = content
    replacements_count = 0

    if replace_pair is not None:
        old, new = replace_pair.split('=', 1)
        replacements_count = result.count(old)
        result = result.replace(old, new)

    if footer is not None:
        if result and not result.endswith('\n'):
            result += '\n'
        result += footer

    return result, replacements_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт для копирования файла с заменой текста и футером')
    parser.add_argument('--input',required=True,help='путь к входному файлу')
    parser.add_argument('--output',required=True,help='путь к выходному файлу')
    parser.add_argument('--replace',help='замена текста в формате OLD=NEW')
    parser.add_argument('--append-footer',help='строка для добавления в конец выходного файла',)
    parser.add_argument('--overwrite',action='store_true',help='разрешить перезапись выходного файла',)
    args = parser.parse_args()

    if args.replace is not None and '=' not in args.replace:
        parser.error('Аргумент --replace должен быть в формате OLD=NEW')

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except FileNotFoundError:
        parser.error(f"Входной файл '{args.input}' не найден")

    processed_text, count = process_content(
        raw_content,
        args.replace,
        args.append_footer,
    )

    mode = 'w' if args.overwrite else 'x'
    try:
        with open(args.output, mode, encoding='utf-8') as f:
            f.write(processed_text)
    except FileExistsError:
        parser.error(
            f"Файл '{args.output}' уже существует. Используйте --overwrite"
        )

    print(f'Выполнено замен: {count}')
