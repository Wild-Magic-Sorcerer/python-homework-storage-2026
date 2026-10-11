#!/usr/bin/env python3

def user_input(text: str):
    znach = input(text)
    return znach

def recurs_factor(num):
    if num == 0 or num == 1:
        return 1
    return num * recurs_factor(num - 1)

def iterativ_factor(num):
    res = 1
    for x in range(1, (num+1)):
        res *= x
    return res

if __name__ == "__main__":
    while True:
        U_I = user_input("Введите целое число, факториал которого вы хотите найти:\n")
         
        try:
            number = int(U_I)
            
            if number >= 0:
                break  
            else:
                print("Число должно быть неотрицательным. Попробуем ещё раз.\n")
                
        except ValueError:
            has_let = any(char.isalpha() for char in U_I)
            
            if has_let:
                print("Вы ввели буквы. Написано же, только ЦИФРЫ.\n")
            else:
                print("Это не целое число. Попробуем ещё раз.\n")

    
    print(f'А вот и результат\n от рекурсивной функции :{recurs_factor(number)}\n  от итеративной: {iterativ_factor(number)} ')
            

    
    