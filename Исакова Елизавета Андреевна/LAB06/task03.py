import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Поиск строк в лог-файле по дате.')
    parser.add_argument('date', help='Искомая дата')
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('--output_file', default=None, help='Путь к выходному файлу (опционально)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as in_f:
            lines = in_f.readlines()
    except FileNotFoundError:
        print(f'Ошибка! Файл {args.input_file} не найден')
        exit(1)

    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.search(pattern, args.date):
        print('Ошибка! Дата должна быть указана в формате: YYYY-MM-DD')
        exit(1)

    lines_with_date = []
    for line in lines:
        clean_line = line.rstrip('\n')
        if re.search(args.date, clean_line):
            lines_with_date.append(clean_line)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as out_f:
            for line in lines_with_date:
                out_f.write(line + '\n')
    else:
        for line in lines_with_date:
            print(line)

    print(f'Количество найденных строк: {len(lines_with_date)}')
