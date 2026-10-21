#!/usr/bin/env python3


def dlinnye_stroki(stroki):
    if not stroki:
        return []
    srednyaya = sum(len(s) for s in stroki) / len(stroki)
    return [s for s in stroki if len(s) > srednyaya]


def obrabotka_strok():
    while True:
        spisok = []

        while True:
            vvod = input("Введите строки через пробел: ").strip()
            if not vvod:
                print("Ошибка: пустой ввод. Попробуйте еще раз.")
                continue
            spisok = vvod.split()
            if len(spisok) == 0:
                print("Ошибка: нужно хотя бы одно слово.")
                continue
            break

        print("Результат:", dlinnye_stroki(spisok))

        prodolzhit = input(
            "Продолжить -enter, стоп - выход : "
        ).strip().lower()
        if prodolzhit == "стоп":
            break


if __name__ == "__main__":
    obrabotka_strok()
