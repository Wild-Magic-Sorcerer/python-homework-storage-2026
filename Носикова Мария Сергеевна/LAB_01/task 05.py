# task 05
def find_hypotenuse(a,b):
    return (a ** 2 + b ** 2) ** 0.5
def find_cathetus(a,c):
    return (c ** 2 - a ** 2) ** 0.5
if __name__ == '__main__':
    print("1 - Найти гипотенузу (известны два катета)")
    print("2 - Найти катет (известны гипотенуза и катет)")
    choice = input('Ваш выбор:')
    if choice == '1':
        a = float(input('Введите первый катет:'))
        b = float(input('Введите второй катет:'))
        result = find_hypotenuse(a, b)
        print(f'Гипотенуза трегольника равна = {result}')
    elif choice == '2':
        a = float(input('Введите известный катет:'))
        c = float(input('Введите гипотенузу:'))
        result = find_cathetus(a, c)
        print(f'Второй катет трегольника равен = {result}')
    else: 
        print('При вводе выбора произошла ошибка. Попробуйте еще раз')
