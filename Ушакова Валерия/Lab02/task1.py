#!/usr/bin/env python3


def longer(words: list) -> list:
    if not words:
        return []

    lengths = [len(word) for word in words]
    average = sum(lengths) / len(lengths)

    return [word for word in words if len(word) > average]
STANDARD_DELIMITED: str= ','

if __name__ == '__main__':
    print(f'Введите слова,используя "{STANDARD_DELIMITED}" как делимитр:\n')

    while True:
        text = input().strip()

        if text.lower() == 'stop':
            break

        texts= text.replace(',', ' ')
        words = texts.split()

        if not words:
            print('Пусто пусто')
            continue

        result = longer(words)
        average = sum(len(w) for w in words) / len(words)

        print(f'Слова: {words}')
        print(f'Средняя длина: {average:}')
        print(f'Слова длиннее среднего: {result}')
