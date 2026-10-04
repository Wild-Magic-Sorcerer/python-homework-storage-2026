#!/usr/bin/env python3


def pif(value: str) -> float:
    all_is_fine: bool = False
    side: float = 0.0

    while not all_is_fine:
        text: str = input(f'Введи {value}: ').strip()

        if not text:
            print('Неправильно, попробуй еще раз')
        else:
            try:
                side = float(text)

                if side > 0:
                    all_is_fine = True
                else:
                    print('Сторона должна быть > 0')

            except ValueError:
                print('Введи число')

    return side


if __name__ == '__main__':
    choice: str = input(
        '1 - есть два катета, 2 - есть гипотенуза и катет: '
    ).strip()

    if choice == '1':
        a: float = pif('первый катет')
        b: float = pif('второй катет')

        c: float = (a ** 2 + b ** 2) ** 0.5

        print(f'Гипотенуза: {c:.2f}')

    elif choice == '2':
        c: float = pif('гипотенузу')
        a: float = pif('известный катет')

        if c > a:
            b: float = (c ** 2 - a ** 2) ** 0.5
            print(f'Второй катет: {b:.2f}')
        else:
            print('Гипотенуза должна быть больше катета')

    else:
        print('Неправильно, попробуй еще раз')
