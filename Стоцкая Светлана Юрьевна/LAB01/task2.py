COURSES = ("Иностранный язык", "Высшая математика", "Органическая химия",
           "Ботаника высших растений", "Физическая культура", "Философия")

def sort_marks(students_list, marks_list):
    max_mark = 3
    min_mark = 5
    avg_mark = 0
    for student in range(len(students_list)):
        if len(marks_list[student]) != len(COURSES):
            print("Вы ввели оценки студента не по всем предметам!")
            break
        for subject in range(len(COURSES)):
            try:
                temp_mark = int(marks_list[student][subject])
                if temp_mark > 5 or temp_mark < 3:
                    raise ValueError
                avg_mark += temp_mark
                if temp_mark > max_mark:
                    max_mark = temp_mark
                if temp_mark < min_mark:
                    min_mark = temp_mark
            except ValueError:
                print("Вы ввели не число или не оценку! ")
                break

        avg_mark /= len(COURSES)
        print(f"Студент {students_list[student]}", f"Максимальная оценка {max_mark}",
              f"Минимальная оценка {min_mark}", f"Средняя оценка {avg_mark}")
        avg_mark = 0
        max_mark = 3
        min_mark = 5

if __name__ == '__main__':
    students = []
    condition = ""
    all_marks = []
    while condition != "да":
        name = input("Введите ФИО студента ")
        your_marks = input("Введите оценки студента за все курсы через пробел ")
        if name in students:
            print("Вы уже вводили оценки этого студента ранее.")
            continue
        students.append(name)
        all_marks.append(tuple(your_marks.split()))
        condition = input("Если студенты закончились, напишите 'да', иначе напишите 'нет' ")
    print(all_marks)
    sort_marks(students, all_marks)
