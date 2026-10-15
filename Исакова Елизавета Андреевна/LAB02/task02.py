def increase(data):
    inc_sort = sorted(data)
    return tuple(inc_sort)

def decrease(data):
    dec_sort = sorted(data, reverse=True)
    return tuple(dec_sort)

if __name__ == "__main__":
    delimiter = ','

    if delimiter == ' ':
        prompt_text = 'Введите последовательность чисел для сортировки через пробел:\n'
    else:
        prompt_text = f'Введите последовательность чисел для сортировки через "{delimiter}":\n'

    numbers_lst = []
    
    while True:
        numbers = input(prompt_text)

        if not numbers.strip():
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        if delimiter not in numbers:
            if delimiter == ' ':
                print('Вы ввели числа не через пробел! Попробуйте еще раз')
            else:
                print(f'Вы ввели числа не через "{delimiter}"! Попробуйте еще раз')
            continue

        numbers = numbers.split(delimiter)
        valid = True
        for number in numbers:
            strip_number = number.strip()
            if not strip_number:
                valid = False
                print(f'Не пишите лишние "{delimiter}"!')
                break
            if delimiter in strip_number:
                valid = False
                print(f'{strip_number} - это не одно число, их нужно разделять "{delimiter}"!')
                break

        if not valid:
            continue

        try:
            numbers_lst = [float(number.strip()) for number in numbers]
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
