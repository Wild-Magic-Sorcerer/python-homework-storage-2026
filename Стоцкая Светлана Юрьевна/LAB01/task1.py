def check_difference(sequence):
    numbers_list = sequence.split()
    each_number = len(numbers_list)
    numbers_set = set(numbers_list)
    unique_numbers = len(numbers_set)
    if each_number != unique_numbers:
        print("Не все числа различны, есть совпадения.")
    else:
        print("Все числа различны!")


if __name__ == '__main__':
    some_numbers = input("Введите какую-нибудь последовательность чисел ")
    check_difference(some_numbers)
