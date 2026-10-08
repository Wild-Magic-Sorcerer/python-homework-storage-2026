#!/usr/bin/env python3

CEMETERY: tuple[str, ...]=('math','bio','chemistry', 'hisrory', 'english')


sub = {subj: {} for subj in CEMETERY}
if __name__ == '__main__':
    students = {}
    print('Введите имя и 5 оценoк ученика через пробел, при окончании списка людей впишите слово "стоп" \n')
    while True:
        try:
            res_stringi :str = input().strip().lower()

            if res_stringi == 'стоп':
                break

            letters= any(c.isalpha() for c in res_stringi)
            digits= any(c.isdigit() for c in res_stringi)
            if letters and digits:
                print('Окей, смотрим дальше')
            elif letters and not digits:
                print('Оценочка пять из пяти типа?')
                continue
            elif digits and not letters:
                print('Буквы где')
                continue
            else:
                print('Ну и где все')
                continue

            ress_stringi = res_stringi.replace(',',' ' )
            marks = ress_stringi.split()
            if len(marks) != 6:
                print('А длина норм?')
                continue

            name = marks[0]
            values = marks[1:]


            if not all(g.isdigit() for g in values):
                print('Целые числа впиши')
                continue


            grades = [int(g) for g in values]

            if not all(3 <= v <=5 for v in grades) :
                raise ValueError()

            students[name] = tuple(grades)
            for i in range(5):
                subjects=CEMETERY[i]
                sub[subjects][name]= grades[i]

            print(f'Вааау: {name}= {students[name]}')
        except ValueError:
            print('Вне диапозона')
            continue

        print('По предметам:')
        for subjects in CEMETERY:
            print(f'    {subjects}: {sub[subjects]}')


for subjects in CEMETERY:
    marks = list(sub[subjects].values())

    if marks:
        med = sum(marks)/len(marks)
        print(f' {subjects}:')
        print(f'Средний балл: {round(med, 2)}')
        print(f'Минимум: {min(marks)}')
        print(f' максимум: {max(marks)}')

    else:
        print(f' {subjects}: нет данных')
