def fact_rec(value):
    try:
        value = int(value)
        if value == 0:
            return 1
        elif value == 1:
            return 1
        elif value < 0:
            raise ValueError
        else:
            return (fact_rec(value - 1)) * value
    except ValueError:
        return "Вы ввели неподходящее значение, подсчёт невозможен"

def fact_iter(value):
    fact = 1
    try:
        value = int(value)
        if value == 0:
            return 1
        elif value < 0:
            raise ValueError
        for i in range(1, value+1):
            fact *= i
        return fact
    except ValueError:
        return "Вы ввели неподходящее значение, подсчёт невозможен"

if __name__ == '__main__':
    number = input("Введите целое неотрицательное число ")
    print(fact_rec(number))
#    print(fact_iter(number))
