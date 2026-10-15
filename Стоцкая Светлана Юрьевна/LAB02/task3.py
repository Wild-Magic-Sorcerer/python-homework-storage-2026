def multiply(*args):
    result = 1
    for value in args:
        try:
            result *= int(value)
        except ValueError:
            print(value, type(value))
    print(result)

if __name__ == '__main__':
    numbers = input("Введите набор чисел через пробел ").split()
    multiply(*numbers)
