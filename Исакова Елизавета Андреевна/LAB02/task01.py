def func(lst):
    new_lst = []
    average_length = sum(len(x) for x in lst) / len(lst)

    for x in lst:
        if len(x) >= average_length:
            new_lst.append(x)

    return new_lst

if __name__ == '__main__':
    while True:
        words = input('Введите несколько слов через пробел:\n')
        words_list = words.split()

        if not words.strip():
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        if ',' in words:
            print('Вы ввели слова через запятую, нужно через пробел! Попробуйте еще раз')
            continue

        valid_input = True
        for y in words_list:
            if not y.isalpha():
                print(f'"{y}" содержит не только буквы! Попробуйте еще раз')
                valid_input = False
                break

        if not valid_input:
            continue

        break

    print(f'Список строк, длина которых больше среднего значения длины строки в исходном списке: {func(words_list)}')
