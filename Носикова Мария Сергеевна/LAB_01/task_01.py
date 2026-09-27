# task01
def counter(var):
    var_split = var.split()
    list_var = []
    for number in var_split:
        list_var.append(int(number))
    if len(list_var) == len(set(list_var)):
        print("условие соблюдено")
    else: 
        print("условие не соблюдено, замените")

if __name__ == '__main__':
     var = input('Введите числа через пробел:')
     counter(var)
     