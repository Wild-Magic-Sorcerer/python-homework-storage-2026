#!/usr/bin/env python3
GLASNYE_BUKVY = "аеёиоуыэюя"
POROG = 3


def otobrat_stroki(**kwargs):
    itog = {}
    for imya, znachenie in kwargs.items():
        if type(znachenie) is str:
            glasnyh = 0
            for s in znachenie.lower():
                if s in GLASNYE_BUKVY:
                    glasnyh = glasnyh + 1
            if glasnyh >= POROG:
                itog[imya] = znachenie
    return itog


def zapusk_filtratsii():
    while True:
        parametry = {}

        while True:
            vvod = input(
                "Введите пары ключ=значение через пробел: "
            ).strip()
            if not vvod:
                print("Ошибка: пустой ввод.")
                continue

            parametry = {}
            oshibka = False
            for para in vvod.split():
                if "=" not in para:
                    print(
                        f"Ошибка: '{para}' без знака '='. "
                    )
                    oshibka = True
                    break
                klyuch, znachenie = para.split("=", 1)
                if not klyuch or not znachenie:
                    print(
                        f"Ошибка: '{para}' пустой ключ "
                    )
                    oshibka = True
                    break
                parametry[klyuch] = znachenie

            if not oshibka:
                break

        rezultat = otobrat_stroki(**parametry)
        if rezultat:
            print("Результат:", rezultat)
        else:
            print("Нет слов с 3+ гласными.")

        prodolzhit = input(
            "Продолжить -enter, стоп - выход "
        ).strip().lower()
        if prodolzhit == "стоп":
            break


if __name__ == "__main__":
    zapusk_filtratsii()
