import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Поиск данных в файле по заданному режиму')
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('--output_file', default=None, help='Путь к выходному файлу (опционально)')
    parser.add_argument('target', choices=['digits', 'phones', 'domains', 'urls'], help='Режим поиска')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as in_f:
            text = in_f.read()
    except FileNotFoundError:
        print(f'Ошибка! Файл {args.input_file} не найден')
        exit(1)

    if args.target == 'digits':
        pattern = r'\d+'
    elif args.target == 'phones':
        pattern = r'\+7\d{10}|\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}|\d{2}-\d{2}-\d{2}|\d{6}'
    elif args.target == 'domains':
        pattern = r'[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    else:
        pattern = r'https?://\S+'

    coincidences = re.findall(pattern, text)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as out_f:
            for coincidence in coincidences:
                out_f.write(coincidence + '\n')
    else:
        for coincidence in coincidences:
            print(coincidence)

    print(f'Количество найденных совпадений: {len(coincidences)}')
