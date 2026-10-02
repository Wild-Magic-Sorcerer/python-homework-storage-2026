def third_side(a, b):
    answer = input("Если обе стороны катеты, введите '+', иначе введите '-' ")
    length = 0
    if answer == '+':
        length = (a ** 2 + b ** 2) ** 0.5
    elif answer == '-':
        if a > b:
            length = (a ** 2 - b ** 2) ** 0.5
        else:
            length = (b ** 2 - a ** 2) ** 0.5
    else:
        print("Ответьте на вопрос правильно!")
    if length == 0:
        print("Такого треугольника не существует")
    return length

if __name__ == '__main__':
    first_side = float(input("Введите длину первой стороны треугольника "))
    second_side = float(input("Введите длину второй стороны треугольника "))
    final_side = third_side(first_side, second_side)
    print(f'Длина третьей стороны треугольника {final_side}')
