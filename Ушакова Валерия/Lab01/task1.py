#!/usr/bin/env python3


def uniq(numb):
    return len(numb) == len(set(numb))

if __name__ == '__main__':
    print('Введите последовательность чисел через пробел или запятую\n')
    while True:
        res_stringi: str= input().strip()
        if res_stringi.lower() == 'стоп':
            break
        res_stringi = res_stringi.replace(',',' ' )
        parts= res_stringi.split()
        if all(c.isdigit() for c in parts):
            numbs = tuple(float(i) for i in parts)
            if uniq(numbs):
                print(numbs)
                print('All is different,continue!')
            else:
                print('Впишите РАЗЛИЧНЫЕ числа через запятую или пробел!!')
