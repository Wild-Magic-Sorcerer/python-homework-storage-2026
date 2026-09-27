def side_search(c1, c2, h):
    if c1 == '':
        result = (h**2 - c2**2) ** 0.5
        return f'Первый катет - {result}'
    elif c2 == '':
        result = (h**2 - c1**2) ** 0.5
        return f'Второй катет - {result}'
    elif h == '':
        result = (c1**2 + c2**2) ** 0.5
        return f'Гипотенуза - {result}'
    else:
        return 'Все стороны известны'

if __name__ == '__main__':
    cathetus_1_str = input('Введите значение одного катета (или Enter если неизвестно)\n')
    cathetus_2_str = input('Введите значение второго катета (или Enter если неизвестно)\n')
    hypotenuse_str = input('Введите значение гипотенузы (или Enter если неизвестно)\n')

    cathetus_1 = ''
    cathetus_2 = ''
    hypotenuse = ''

    try:
        if cathetus_1_str:
            cathetus_1 = float(cathetus_1_str)
        if cathetus_2_str:
            cathetus_2 = float(cathetus_2_str)
        if hypotenuse_str:
            hypotenuse = float(hypotenuse_str)
    except ValueError:
        print('Ошибка! Введите число или просто Enter')

    print(side_search(cathetus_1, cathetus_2, hypotenuse))

