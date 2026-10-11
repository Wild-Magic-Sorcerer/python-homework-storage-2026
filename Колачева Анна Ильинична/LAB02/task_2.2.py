#!/usr/bin/env python3

def user_input(text: str):
    znach = input(text)
    return znach

def proverka_c() -> list:
    
    while True:
        num_list = user_input("Веедите последовательность чисел через пробел\n").replace("," , ".").split()
       
        if len(num_list) == 0:
            print('Вы ничего не ввели!\n')
            continue

        valid = True
        for num in num_list:
            try:
                float(num)
            except ValueError:
                    print(f"В вашей последовательности встретилось {num}, а это не число, ещё попытка:\n")
                    valid = False
                    break

        if valid:
            return [float(x) for x in num_list]


def quick_sort(arr: list) -> list:
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  
    
    left = [x for x in arr if x < pivot]      
    mid = [x for x in arr if x == pivot]    
    right = [x for x in arr if x > pivot]      
    
    return quick_sort(left) + mid + quick_sort(right)



if __name__ == "__main__":
    num_list = proverka_c()
    
    while True:

        try:
            who = int(user_input("Если хотите отсортировать от меньшего к большему, пишите - 1, в обратном порядке - 2\n"))
            if who == 1:
                print(f'Воть : {quick_sort(num_list)}')
                break
            elif who == 2:
                rev_s_list = quick_sort(num_list)[::-1]
                print(f'Воть : {rev_s_list}')
                break
            else:
                print("Вы ввели  какое-то другое число, пробуем ещё раз:\n")
                continue
        except ValueError:
            print("Это вообще не число!")
