import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Поиск email-адресов в файле')
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('--output_file', default=None, help='Путь к выходному файлу (опционально)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as in_f:
            text = in_f.read()
    except FileNotFoundError:
        print(f'Ошибка! Файл {args.input_file} не найден')
        exit(1)

    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(pattern, text)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as out_f:
            for email in emails:
                out_f.write(email + '\n')
    else:
        for email in emails:
            print(email)

    print(f'Количество найденных email-адресов: {len(emails)}')
