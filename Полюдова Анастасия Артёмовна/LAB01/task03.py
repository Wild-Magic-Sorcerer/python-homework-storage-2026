#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '
GL: str = 'уеыаоэяиюё'
ZNAKI: str = '.,!;:?-'


if __name__ == '__main__':
    text: str = input('Введи слова через пробел').strip()

    if not text:
        print('Неправильно, попробуй еще раз')
    else:
        words: tuple[str, ...] = tuple(text.split(STANDARD_DELIMITED))
        u_words: int = len(set(words))

        gl_2: int = 0
        sogl_2: int = 0
        znaki_2: int = 0

        for n in text:
            if n.casefold() in GL:
                gl_2 += 1
            elif n.isalpha():
                sogl_2 += 1
            elif n in ZNAKI:
                znaki_2 += 1

        print(f'Кол-во уникальных слов: {u_words}')
        print(f'Кол-во гласных: {gl_2}')
        print(f'Кол-во согласных: {sogl_2}')
        print(f'Кол-во знаков препинания: {znaki_2}')
