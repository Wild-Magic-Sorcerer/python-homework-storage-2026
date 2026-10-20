def func(lst):
    new_lst = []
    average_length = sum(len(x) for x in lst) / len(lst)

    for x in lst:
        if len(x) >= average_length:
            new_lst.append(x)

    return new_lst

if __name__ == '__main__':
    delimiter = None

    if delimiter is None:
        prompt_text = 'Введите несколько слов через пробел:\n'
    else:
        prompt_text = f'Введите несколько слов через "{delimiter}": '

    words_list = []

    while True:
        words = input(prompt_text)

        if not words.strip():
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue
            
        words_list = words.split()

        valid_input = True
        for y in words_list:
            if not y.isalpha():
                print(f'"{y}" содержит не только буквы! Попробуйте еще раз')
                valid_input = False
                break

        if not valid_input:
            continue

        break

    print(f'Список строк, длина которых больше или равна среднему значению: {func(words_list)}')
    
