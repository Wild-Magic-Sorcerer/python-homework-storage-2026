from functools import reduce

def reform_list(strings_list):
    '''
    Эта функция фильтрует список строк, удаляя неподходящие и изменяя способ записи.
    :param strings_list: Список строк, полученный от пользователя.
    :return: None: Ничего не возвращает, выводит на экран промежуточные и итоговые
    '''
    cut = lambda x: len(x) >= 7
    cut_list = list(filter(cut, strings_list))
    pair = lambda x: (x, len(x))
    paired_list = list(map(pair, cut_list))
    lengths = lambda x: x[1]
    len_list = list(map(lengths, paired_list))
    maximum = reduce(lambda counter, x: x if counter < x else counter, len_list)
    for i in range(len(len_list)):
        if len_list[i] == maximum:
            max_word = paired_list[i][0]
    letter_result = reduce(lambda counter,x: counter + x[1], paired_list, 0)
    print(f"Список после убирания слов длиной менее 7 символов {cut_list}")
    print(f"Список после преобразований чисел в пары {paired_list}")
    print(f"Слово с максимальной длиной {max_word}")
    print(f"Суммарное количество символов во всех отфильтрованных словах {letter_result}")

if __name__ == '__main__':
    some_list = []
    while True:
        some_str = input("Введите строку ")
        if some_str == "":
            break
        some_list.append(some_str)
    reform_list(some_list)
