#!/usr/bin/env python3
import argparse


def read_order(text: str) -> str:
    """Проверяет значение аргумента сортировки.

    :param text: Направление сортировки
    :return: Одно из значений asc, desc или none
    """
    if text not in ("asc", "desc", "none"):
        raise argparse.ArgumentTypeError(
            "Для --sort выберите asc, desc или none"
        )
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Фильтрация списка строк.")
    parser.add_argument("strings", nargs="*", help="строки через пробел")
    parser.add_argument("--unique", action="store_true", help="убрать повторы")
    parser.add_argument("--count", action="store_true", help="число строк")
    parser.add_argument("--min-length", type=int, default=0, help="мин. длина")
    parser.add_argument("--sort", type=read_order, default="none")
    args = parser.parse_intermixed_args()

    if not args.strings:
        parser.error("Передайте хотя бы одну строку")
    if args.min_length < 0:
        parser.error("Минимальная длина должна быть неотрицательной")
    words = [word for word in args.strings if len(word) >= args.min_length]
    if args.unique:
        words = list(dict.fromkeys(words))
    if args.count:
        print(len(words))
    else:
        if args.sort != "none":
            words.sort(reverse=args.sort == "desc")
        for word in words:
            print(word)
