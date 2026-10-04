#!/usr/bin/env python3


COURSES: tuple[str, ...] = (
    'Физика',
    'Вышмат',
    'Философия',
    'Ботаника',
    'Орг.химия',
)

DEFAULT_GRADES: tuple[int, ...] = (3, 4, 5)


if __name__ == '__main__':
    students: dict[str, list[int]] = {}
    score: list[int] = []
    all_is_fine: bool = True

    while all_is_fine:
        name: str = input(
            'Введи имя студента или нажми Enter для gg '
            '(чтобы выйти из цикла):').strip()

        if not name:
            all_is_fine = False
        elif name in students:
            print('Его уже записали!')
        else:
            their_grades: list[int] = []

            for course in COURSES:
                grade_is_fine: bool = False

                while not grade_is_fine:
                    try:
                        grade: int = int(
                            input(f'Введи оценку по курсу "{course}": ')
                        )

                        if grade in DEFAULT_GRADES:
                            their_grades.append(grade)
                            score.append(grade)
                            grade_is_fine = True
                        else:
                            print('Только тройбан, либо 4 или 5')

                    except ValueError:
                        print('Неправильно, введи только целое число')

            students[name] = their_grades

    if students:
        mid: float = sum(score) / len(score)

        print(f'Среднячок: {mid:.2f}')
        print('Минимальная оценка:', min(score))
        print('Максимальная оценка:', max(score))
    else:
        print('Нет информации')
