#!/usr/bin/env python3
def umnozhit_tselye(*args):
    tselye = [z for z in args if type(z) is int]
    if not tselye:
        print("Ошибка: циферки пиши (инты)!")
        for z in args:
            print(f"  Значение: {z}, Тип: {type(z).__name__}")
        return None

    itog = 1
    for chislo in tselye:
        itog = itog * chislo
    return itog


def zapusk_umnozheniya():
    while True:
        while True:
            vvod = input("Введите значения через пробел: ").strip()
            if not vvod:
                print("Ошибка: пустой ввод. Попробуйте еще раз.")
                continue
            break

        argumenty = []
        for slovo in vvod.split():
            if slovo.lstrip("-").isdigit():
                argumenty.append(int(slovo))
            else:
                try:
                    argumenty.append(float(slovo))
                except ValueError:
                    argumenty.append(slovo)

        rezultat = umnozhit_tselye(*argumenty)
        if rezultat is not None:
            print("Результат:", rezultat)

        prodolzhit = input(
            "Продолжить -enter, стоп - выход"
        ).strip().lower()
        if prodolzhit == "стоп":
            break


if __name__ == "__main__":
    zapusk_umnozheniya()
