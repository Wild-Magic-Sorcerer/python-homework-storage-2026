def func(lst):
    new_lst = []
    average_length = sum(len(x) for x in lst) / len(lst)

    for x in lst:
        if len(x) > average_length:
            new_lst.append(x)

    return new_lst

if __name__ == '__main__':
    delimiter = ' '

    if delimiter == ' ':
        prompt_text = 'Введите несколько слов через пробел:\n'
    else:
        prompt_text = f'Введите несколько слов через "{delimiter}": '

    words_list = []

    while True:
        words = input(prompt_text)

        if not words.strip():
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        if delimiter not in words:
            if delimiter == ' ':
                print('Ошибка: вы ввели слова не через пробел! Попробуйте еще раз')
                continue
            else:
                print(f'Ошибка: вы ввели слова не через "{delimiter}"! Попробуйте еще раз')
                continue

        words_list = [word.strip() for word in words.split(delimiter)]

        words_list = [word for word in words_list if word]

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
