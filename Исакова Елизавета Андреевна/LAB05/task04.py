import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Утилита для копирования и обработки файлов')
    parser.add_argument('--input', required=True, help='Входной файл')
    parser.add_argument('--output', required=True, help='Выходной файл')
    parser.add_argument('--replace', help='Замена в формате OLD=NEW')
    parser.add_argument('--append-footer', help='Строка для добавления в конец')
    parser.add_argument('--rewrite', action='store_true', help='Разрешить перезапись выходного файла')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        parser.error(f'Входной файл "{args.input}" не найден!')
    if os.path.exists(args.output) and not args.rewrite:
        parser.error(f'Файл "{args.output}" уже существует!')

    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
        
    count_replace = 0
    if args.replace:
        old, new = args.replace.split('=', 1)
        count_replace = content.count(old)
        content = content.replace(old, new)

    if args.append_footer:
        content += '\n' + args.append_footer

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Выполнено замен: {count_replace}')
    print(f'Результат сохранён в "{args.output}"')
