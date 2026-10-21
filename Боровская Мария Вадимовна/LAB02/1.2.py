#!/usr/bin/env python3


def uporyadochit(chisla, obratno):
    return sorted(chisla, reverse=obratno)


def zapusk_sortirovki():
    while True:
        chisla = []

        while True:
            vvod = input("Введите числа через пробел: ").strip()
            if not vvod:
                print("Ошибка: пустой ввод. Попробуйте еще раз.")
                continue

            chisla = []
            oshibka = False
            for slovo in vvod.split():
                try:
                    chisla.append(float(slovo))
                except ValueError:
                    print(
                        f"Ошибка: '{slovo}' не число. "
                        f"Попробуйте еще раз."
                    )
                    oshibka = True
                    break

            if not oshibka:
                break

        while True:
            vibor = input(
                "1 - по возрастанию, 2 - по убыванию: "
            ).strip()
            if vibor == "1" or vibor == "2":
                break
            print("Ошибка: нужно ввести 1 или 2.")

        print("Результат:", uporyadochit(chisla, vibor == "2"))

        prodolzhit = input(
            "Продолжить -enter, стоп - выход"
        ).strip().lower()
        if prodolzhit == "стоп":
            break


if __name__ == "__main__":
    zapusk_sortirovki()
