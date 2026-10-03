def increase(data):
    inc_sort = sorted(data)
    return tuple(inc_sort)

def decrease(data):
    dec_sort = sorted(data, reverse=True)
    return tuple(dec_sort)

if __name__ == "__main__":
    while True:
        numbers = input('Введите последовательность чисел для сортировки через запятую:\n')
        numbers_lst = None

        if not numbers:
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        if ',' not in numbers:
            print('Вы ввели числа не через запятую! Попробуйте еще раз')
            continue

        numbers = numbers.split(',')
        valid = True
        for number in numbers:
            strip_number = number.strip()
            if not strip_number:
                valid = False
                print('Не пишите лишние запятые!')
                break
            if ' ' in strip_number:
                valid = False
                print(f'{strip_number} - это не одно число, их нужно разделять запятой!')
                break

        if not valid:
            continue

        try:
            numbers_lst = [float(number) for number in numbers]
        except ValueError:
            print('Вы ввели не число! Попробуйте еще раз')
            continue
        break

    while True:
        incr_or_decr = input('Если вы хотите отсортировать по возрастанию, введите: +\n'
                            'Если вы хотите отсортировать по убыванию, введите: -\n')

        if not incr_or_decr:
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        if incr_or_decr == '+':
            print(f'Ваша последовательность отсортирована по возрастанию: {increase(numbers_lst)}')
            break
        elif incr_or_decr == '-':
            print(f'Ваша последовательность отсортирована по убыванию: {decrease(numbers_lst)}')
            break
        else:
            print('Попробуйте еще раз, нужно ввести + или - !')
            continue
