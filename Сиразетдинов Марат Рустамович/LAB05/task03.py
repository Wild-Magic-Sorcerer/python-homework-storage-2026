import argparse

SORT_CHOICES = ('asc', 'desc', 'none')


def process_strings(strings, min_length, unique_only, sort_order):
    """
    фильтрует строки
    :param strings: список строк
    :param min_length: минимальная длина или none
    :param unique_only: уникальные строки
    :param sort_order: порядок сортировки
    :return:
    """
    result = strings

    if min_length is not None:
        result = [item for item in result if len(item) >= min_length]

    if unique_only:
        result = list(dict.fromkeys(result))

    if sort_order == 'asc':
        result = sorted(result)
    elif sort_order == 'desc':
        result = sorted(result, reverse=True)

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт для подсчета и фильтрации строк')
    parser.add_argument('strings',nargs='+',help='список строк для обработки')
    parser.add_argument('--count', action='store_true',help='вывести только итоговое количество строк')
    parser.add_argument('--unique', action='store_true',help='оставить только уникальные строки')
    parser.add_argument('--min-length', type=int, help='минимальная длина строки')
    parser.add_argument('--sort',choices=SORT_CHOICES, default='none',help='тип сортировки - asc, desc, none')
    args = parser.parse_args()

    if args.min_length is not None and args.min_length < 0:
        parser.error('Минимальная длина строки не может быть отрицательной')

    processed = process_strings(args.strings, args.min_length, args.unique, args.sort,)

    if args.count:
        length_of_processed = len(processed)
        print(length_of_processed)
    else:
        for line in processed:
            print(line)
