#!/usr/bin/env python3



if __name__ == '__main__':
    while True:
        side: str = input('Введите цифру "1", если нужно найти гипотенузу, "2", если катет\n ').strip()
        if side == "1":
            first = float(input('Введите первый катет\n'))
            second = float(input('Теперь второй\n'))
            ress = (first**2 + second**2) **0.5
            print(f"Получаем сторону\n {ress}")

        elif side == "2":
            first = float(input('Введите гипотенузу\n'))
            second = float(input('Теперь катет\n'))
            if first>second:
                ress = (first ** 2 - second ** 2) ** 0.5
                print(f"Получаем сторону\n {ress}")
            elif first<second:
                ress = (second ** 2 - first ** 2) ** 0.5

                print(f"Получаем сторону\n {ress}")
        else:
            print("Ввели не числа, видимо")
