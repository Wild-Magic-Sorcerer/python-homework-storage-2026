STANDARD_DELIMITER = ","

if __name__ == "__main__":
    users_input = input(f"Введите вашу последовательность через {STANDARD_DELIMITER} \n")
    users_list = users_input.split(STANDARD_DELIMITER)
    users_set = set(users_list)

    seen = []
    duplicates = []
    for i in users_list:
        if i in seen:
            duplicates.append(i)
        else:
            seen.append(i)

    if len(users_list) == len(users_set):
        print("Элементы различны")
    else:
        print(f"Элементы не уникальны, вот повторы: {duplicates}, вот оригинальные значения: {users_set}")
