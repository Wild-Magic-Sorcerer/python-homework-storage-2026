#!/usr/bin/env python3
vowels = 'уеыаоэяиюeyuoa'
consonants = 'йцкншщзхъфвпрлджчсмтбqwrtpsdfghkjlzxcvbnm'
prob = ' '
if __name__ == '__main__':
        print('Введите строку слов')
        while True:
                text = input().strip()
                if text.lower() =='стоп':
                    break
                texts = tuple(text.split())
                text_un = set(texts)

                v = 0
                c = 0
                p = 0
                diff = 0


                for t in text.lower():
                    if t in vowels:
                        v += 1
                    elif t in consonants:
                        c += 1
                    elif t in prob:
                        p += 1
                    else:
                        diff += 1

                print(f'Уникальные слова: {text_un}')
                print(f'Гласных:{v}')
                print(f'Согласных:{c}')
                print(f'Пробелов: {p}')
                print(f'Знаков препинания:{diff}')
