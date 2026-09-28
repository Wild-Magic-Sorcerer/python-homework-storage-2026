

def v_gip(a,b):
    gip = (a**2 + b**2)**0.5
    return round(gip, 2)

def v_kat(a,c):
    sec_kat = (c**2 - a**2)**0.5
    return round(sec_kat, 2)

if __name__ == "__main__":
    a = 0
    b = 0
    c = 0
    while True:
        
        try:
            a_str = input('Введите известный катет:\n').replace(',','.')
            a = float(a_str)
            break

        except ValueError:
            print(f'Это не число, пробуй ещё раз!\n')

    what_n =int(input('Если хотите провести расчет по двум катетам введите - 1, если же по катету и гипотенузе - 2:\n'))

          
    if what_n == 1:
        while True:
            try:
                b_str = input('Введите второй катет:\n').replace(',','.')
                b = float(b_str)
                break

            except ValueError:
                print('Это не число, пробуй ещё раз!\n')

    if what_n == 2:
        while True:
                try:
                    c_str = input('Введите гипотенузу:\n').replace(',','.')
                    c = float(c_str)
                    if round(c , 3) <= round(a , 3):
                        print("Гипотенуза должнв быть меньше изввестного катета, пробуем снова!\n")
                        continue

                    else:
                        break
    
                except ValueError:
                    print('Это не число, пробуй ещё раз!\n')

    if (a and b) > 0:
        print(f' Гипотенуза в таком треугольнике ровна {v_gip(a,b)}')

    if (a and c) > 0:
        print(f' Второй катет в таком треугольнике ровна {v_kat(a,c)}')
