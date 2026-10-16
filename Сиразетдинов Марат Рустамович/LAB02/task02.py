def sort_numbers(numbers, reverse=False):
    sorted_list = list(numbers)
    sorted_list.sort(reverse=reverse)
    return sorted_list

if __name__ == "__main__":
    user_input = input("Введите числа через пробел:\n")
    numbers = [x for x in user_input.split()]

    choice = input("Выберите режим:1-По возврастанию, 2-По убыванию:")

    if choice == "1":
        result = sort_numbers(numbers, reverse=True)
        print(result)
    elif choice == "2":
        result = sort_numbers(numbers, reverse=False)
        print(result)
    else:
        print("Неверный ввод")

