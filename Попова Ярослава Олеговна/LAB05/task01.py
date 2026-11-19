#!/usr/bin/env python3
import argparse

MIN_AGE = 0
MAX_AGE = 120
ERROR_EXIT_CODE = 2

def create_greeting(name: str, age: int = None, greet: bool = False) -> str:
    """
    Формирует строку приветствия на основе переданных данных.

    name: имя пользователя
    age: возраст пользователя
    greet: флаг для добавления официального приветствия
    return: готовая строка для вывода на экран
    """
    words = []

    if greet:
        words.append("Уважаемый(ая)")

    words.append(name)

    if age is not None:
        words.append(f"(возраст: {age})")

    return " ".join(words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Скрипт приветствия пользователя.")
    parser.add_argument("name", type=str, help="Имя пользователя")
    parser.add_argument("--age", type=int, default=None, help="Возраст пользователя")
    parser.add_argument("--greet", action="store_true", help="Флаг официального приветствия")

    args = parser.parse_args()

    if args.age is not None:
        if not (MIN_AGE <= args.age <= MAX_AGE):
            parser.error(f"Возраст должен быть целым числом от {MIN_AGE} до {MAX_AGE}.")

    result = create_greeting(args.name, args.age, args.greet)
    print(result)

