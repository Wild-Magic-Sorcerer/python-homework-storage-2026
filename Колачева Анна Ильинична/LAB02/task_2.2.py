#!/usr/bin/env python3

def user_input(text: str) -> list[str]:
    znach = input(text).replace(",", ".").split()
    return znach

def proverka_c() -> list[tuple[float, str]]:
    
    while True:
        num_list: list = user_input("Веедите последовательность чисел через пробел\n")
       
        if len(num_list) == 0:
            print('Вы ничего не ввели!\n')
            continue

        valid = True
        res_tuple: list[tuple[float, str]] = []

        for num in num_list:
            try:
                num_znach = float(num)
                res_tuple.append((num_znach, num))

            except ValueError:
                    print(f"В вашей последовательности встретилось {num}, а это не число, ещё попытка:\n")
                    valid = False
                    break

        if valid:
            return res_tuple


def quick_sort(arr: list[tuple[float, str]]) -> list[tuple[float, str]]:
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  
    
    left = [x for x in arr if x[0] < pivot[0]]      
    mid = [x for x in arr if x[0] == pivot[0]]    
    right = [x for x in arr if x[0] > pivot[0]]      
    
    return quick_sort(left) + mid + quick_sort(right)



if __name__ == "__main__":

    sort_tuples = quick_sort(proverka_c())

    while True:
        try:
           
            who_input = user_input(
                "Выберите порядок сортировки:\n"
                "1 - от меньшего к большему\n"
                "2 - от большего к меньшему\n"
                "Ваш выбор: "
            )
           
            if not who_input:
                print("Нужно ввести число 1 или 2.\n")
                continue
                 
            who = int(who_input[0])
           
            if who == 1:
                output = " ".join([x[1] for x in sort_tuples])
                print(f'Воть : {output}')
                break
            elif who == 2:
                rev_tuples = sort_tuples[::-1]
                output = " ".join([x[1] for x in rev_tuples])
                print(f'Воть : {output}')
                break
            else:
                print("Вы ввели  какое-то другое число, пробуем ещё раз:\n")
                continue
        except ValueError:
            print("Это вообще не число!")
