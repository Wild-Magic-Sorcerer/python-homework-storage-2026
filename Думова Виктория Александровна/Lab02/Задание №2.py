#!/usr/bin/env python3

def get_numbers_from_user():
    result = []
    print("Введите числа (для завершения введите пустую строку):")
    while True:
        user_input = input("> ").strip()
        if user_input == "":
            break
        try:
            result.append(float(user_input))
        except ValueError:
            print(f"'{user_input}' не является числом, попробуйте снова.")
    return result

if __name__ == "__main__":
    numbers = get_numbers_from_user()
    if not numbers:
        print("Список чисел пуст.")
    while True:
        choice = input("Сортировать по возрастанию (1) или по убыванию (2)? ").strip()
        if choice == "1":
            numbers.sort()
            break
        elif choice == "2":
            numbers.sort(reverse=True)
            break
        else:
            print("Введите 1 или 2.")
    print(f"Отсортированный список: {numbers}")
