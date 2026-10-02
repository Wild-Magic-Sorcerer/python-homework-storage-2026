#!/usr/bin/env python3

import math

mode = input("1 — известны два катета, 2 — гипотенуза и катет: ")

if mode == "1":
    first = float(input("Введите первый катет: "))
    second = float(input("Введите второй катет: "))
    result = math.sqrt(first ** 2 + second ** 2)
    print("Длина неизвестной стороны:", round(result, 3))
elif mode == "2":
    hypotenuse = float(input("Введите гипотенузу: "))
    leg = float(input("Введите известный катет: "))
    if hypotenuse > leg:
        result = math.sqrt(hypotenuse ** 2 - leg ** 2)
        print("Длина неизвестной стороны:", round(result, 3))
    else:
        print("Ошибка: гипотенуза должна быть больше катета.")
else:
    print("Ошибка: нужно выбрать 1 или 2.")
