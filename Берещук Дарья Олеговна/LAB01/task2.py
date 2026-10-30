if __name__ == "__main__":
    CLASSES = ("физика","структуры данных","вышмат","ботаника","физхим")
    grades_by_classes = {c: [] for c in CLASSES}
    while True:
        name = input("Введите фамилию студента \n").strip()
        if name == "":
            break
        for c in CLASSES:
            while True:
                try:
                    g = int(input(f"Оценка по курсу {c} студента {name}: \n"))

                except ValueError:
                    print("Введите целое число")
                    continue
                if 3 <= g <= 5:
                    grades_by_classes[c].append(g)
                    break
                else:
                    print("Оценки от 3 до 5")
    for c, g in grades_by_classes.items():
        avg = sum(g) / len(g)
        print(f'Для курса "{c}"":\n '
              f'среднее значение {avg}\n '
              f'минимальное значение {min(g)}\n '
              f'максимальное значение {max(g)}')
