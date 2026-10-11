#!/usr/bin/env python3

def user_input(text: str):
    znach = input(text)
    return znach

def sr_znach(list_ish: list):
    len_str = 0 

    for i in list_ish:
        len_str += len(i)

    return len_str//len(list_ish)

def new_list(list_ish: list, sr_zn: int):
    n_list = []

    for st in list_ish:
        if len(st) > sr_zn:
            n_list.append(st)

    return n_list

if __name__ == "__main__":

    ish_list = []

    var: str = user_input('По очереди ввесдите строки из своего списка:\n')
    ish_list.append(var)

    while True:

        var_more: str = user_input('Ещё одну? (если строки закончились, пиши "стоп")\n')

        if var_more != "стоп":
            ish_list.append(var_more)
        else:
            break

    print(f'Вот что получилось (средняя длинна строки {sr_znach(ish_list)})')
    print(*(new_list(ish_list, sr_znach(ish_list))), sep='\n')
