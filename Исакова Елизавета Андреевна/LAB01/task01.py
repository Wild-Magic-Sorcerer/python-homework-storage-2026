def check_for_distinctness(entrance):
    lst_entrance = entrance.split(',')
    lst_entrance = [x.strip() for x in lst_entrance]
    set_lst_entrance = set(lst_entrance)
    if len(lst_entrance) != len(set_lst_entrance):
        return 'Не все числа в последовательности различны'
    else:
        return 'Все числа в последовательности различны'


if __name__ == "__main__":
    while True:
        sequence = input('Введите последовательность чисел через запятую:\n')

        if not sequence:
            print('Вы ничего не ввели, попробуйте еще раз!')
            continue

        if ',' not in sequence:
            print('Вы ввели числа не через запятую, попробуйте еще раз!')
            continue

        elements_sequence = sequence.split(',')
        for number in elements_sequence:
            try:
                the_correct_number = float(number)
            except ValueError:
                print('Вы ввели не число, попробуйте еще раз!')
                break

        else:
            print(check_for_distinctness(sequence))
            break