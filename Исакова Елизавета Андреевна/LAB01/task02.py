courses = ['Высшая математика', 'Ботаника', 'Физика', 'Английский язык', 'Структуры данных']

def valid_grade(s_name, course_name):
    while True:
        try:
            data = input(f'Введите оценку {s_name} по предмету {course_name}:\n')
            grade_value = int(data)
            if 3 <= grade_value <= 5:
                return grade_value
            else:
                print('Ошибка, оценка должна быть от 3 до 5 включительно!')
        except ValueError:
            print('Ошибка, вы ввели не целое число!')

if __name__ == "__main__":
    all_students_grade = []

    while True:
        student_name = input('Введите имя студента (или Enter для завершения):\n')

        if student_name == '':
            print('Список студентов завершен')
            break

        one_student_grade = []
        for course in courses:
            grade = valid_grade(student_name, course)
            one_student_grade.append(grade)

        all_students_grade.append(one_student_grade)
        print(f'Оценки студента {student_name} сохранены')

    if all_students_grade:
        for i, subject_grade in enumerate(zip(*all_students_grade)):
            average_score = sum(subject_grade) / len(subject_grade)
            max_grade = max(subject_grade)
            min_grade = min(subject_grade)
            print(f'За предмет {courses[i]} средний балл - {average_score}, '
                  f'максимальная оценка - {max_grade}, '
                  f'минимальная оценка - {min_grade}')