import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Работа со строками')
    parser.add_argument('strings', nargs='+', help='Одна строка или несколько')
    parser.add_argument('--count_str', action='store_true', help='Количество строк')
    parser.add_argument('--unique_str', action='store_true', help='Уникальные строки')
    parser.add_argument('--min_len', type=int, default=0, help='Минимальная длина')
    parser.add_argument('--sort_str', choices=['asc', 'desc', 'none'], default='none', help='Сортировка строк')

    args = parser.parse_args()

    result = args.strings
    if args.min_len > 0:
        result = [s for s in result if len(s) >= args.min_len]

    if args.unique_str:
        result = list(dict.fromkeys(result))

    if args.sort_str == 'asc':
        result = sorted(result)
    elif args.sort_str == 'desc':
        result = sorted(result, reverse=True)

    if args.count_str:
        print(len(result))
    else:
        for s in result:
            print(s)
