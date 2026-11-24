import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Поиск строк, содержащих заданное слово')
    parser.add_argument('word', help='Заданное слово')
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('--output_file', default=None, help='Путь к выходному файлу (опционально)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as in_f:
            lines = in_f.readlines()
    except FileNotFoundError:
        print(f'Ошибка! Файл {args.input_file} не найден')
        exit(1)

    lines_with_word = []
    for line in lines:
        clean_line = line.rstrip('\n')
        if re.search(args.word, clean_line, re.IGNORECASE):
            lines_with_word.append(clean_line)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as out_f:
            for line in lines_with_word:
                out_f.write(line + '\n')
    else:
        for line in lines_with_word:
            print(line)

    print(f'Количество найденных строк: {len(lines_with_word)}')
