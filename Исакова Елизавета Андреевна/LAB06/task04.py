import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Поиск совпадений с регулярным выражением в файле')
    parser.add_argument('pattern', help='Паттерн')
    parser.add_argument('input_file', help='Путь к входному файлу')
    parser.add_argument('--output_file', default=None, help='Путь к выходному файлу (опционально)')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as in_f:
            text = in_f.read()
    except FileNotFoundError:
        print(f'Ошибка! Файл {args.input_file} не найден')
        exit(1)

    try:
        coincidences = re.findall(args.pattern, text)
    except re.error:
        print(f'Ошибка! Паттерн регулярного выражения некорректный: {args.pattern}')
        exit(1)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as out_f:
            for coincidence in coincidences:
                out_f.write(coincidence + '\n')
    else:
        for coincidence in coincidences:
            print(coincidence)

    print(f'Количество найденных совпадений: {len(coincidences)}')
