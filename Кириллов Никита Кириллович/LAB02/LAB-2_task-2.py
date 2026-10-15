'''
Задание №2 Напишите программу, которая принимает на вход числа от пользователя
и сортирует их в порядке возрастания или убывания (выбор зависит от пользователя).
'''

DELIMITER = ' '

def sort_ascending(numbers):
    return sorted(numbers)


def sort_descending(numbers):
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    while True:
        user_answer = input("Введите через пробел последовательность чисел: ").split()
        if not user_answer:
            print("Вы ничего не ввели!")
            continue

        nums = []
        try:
            for num in user_answer:
                nums.append(int(num))
            break
        except ValueError:
            print("Ошибка! вы должны ввести последовательность чисел")

    print("Если хотите сделать сортировку по возрастанию, нажмите 1. Если по убыванию - нажмите 2")
    us_input = input("Что Вы желаете сделать? ")

    if us_input == "1":
        result = sort_ascending(nums)
    elif us_input == "2":
        result = sort_descending(nums)
    else:
        print("Ошибка! Выберите 1 или 2")

    print(f"Ваш отсортированный список: {result}")
