#!/usr/bin/env python3

def user_input(text: str):
    znach = input(text).strip()
    return znach

def filter_v(**kwargs):
    vowels = 'aeiouаеёиоуыэюя'
    res = {}

    for key, znach in kwargs.items():
        if isinstance(znach, str):
            count = 0
            lower_znach = znach.lower()
            
            for x in lower_znach:
                if x in vowels:
                    count += 1
            
            if count >= 3:
                res[key] = znach
                
    return res


if __name__ == "__main__":
    
    user_kwargs = {}
    
    print("Вводите аргументы по очереди.")
    print("Для завершения введите пустую строку вместо имени аргумента.\n")
    
    while True:

        key = user_input("Имя аргумента (или Enter для завершения): \n")
        
        if not key:
            break
            
        znach = input(f"Значение для '{key}': ")
        
        user_kwargs[key] = znach
    
    if user_kwargs:
        res = filter_v(**user_kwargs)
        print("\nРезультат:", res)
    else:
        print("\nВы не ввели ни одного аргумента.")