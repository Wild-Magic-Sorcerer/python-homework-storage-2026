from pickle import TRUE

STANDARD_DELIMITER = ","
if __name__ == "__main__":
    while True:
        numbs = input(f"Введите числа для сортировки через {STANDARD_DELIMITER}\n").split(STANDARD_DELIMITER)
        scenario_selection = input("Сортировка по возрастанию или по убыванию?\n")
        if scenario_selection.lower() in ("по возрастанию", "повозрастанию", "возрастанию", "возрастание"):
            print(f"Ваши числа, отсортированные по возрастанию:\n{sorted(numbs)}")
            break
        elif scenario_selection.lower() in ("по убыванию", "поубыванию", "убыванию", "убывание"):
            print(f"Ваши числа, отсортированные по убыванию:\n{sorted(numbs, reverse = True)}")
            break
        else:
            print("Это плохой ответ на мой вопрос, попробуйте еще раз")




