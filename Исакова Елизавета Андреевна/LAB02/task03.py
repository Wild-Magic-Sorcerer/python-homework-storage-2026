def multiplication(*args):
    result = 1
    integers = False
    no_integers = []

    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            result *= arg
            integers = True
        else:
            no_integers.append(arg)

    if integers:
        return f'Произведение целых чисел из вашей последовательности - {result}'
    else:
        for arg in no_integers:
            print(arg, type(arg))
        return 'Целых чисел в последовательности нет!'

if __name__ == '__main__':
    while True:
        data = input('Введите любые значения через запятую:\n')

        if not data:
            print('Вы ничего не ввели!')
            continue

        if ',' not in data:
            print('Значения должны быть разделены запятыми!')
            continue

        data_lst = data.split(',')
        valid = True
        for x in data_lst:
            strip_x = x.strip()
            if not strip_x:
                valid = False
                print('Не пишите лишние запятые!')
                break
            if ' ' in strip_x:
                valid = False
                print(f'"{strip_x}" — это не одно значение, разделяйте запятыми!')
                break

        if not valid:
            continue

        arguments = []
        for y in data_lst:
            y = y.strip()
            try:
                value = int(y)
            except ValueError:
                try:
                    value = float(y)
                except ValueError:
                    value = y
            arguments.append(value)

        print(multiplication(*arguments))
        break
