#!/usr/bin/env python3

KURSY: list[str] = [
    "Программирование",
    "Математический анализ",
    "Физика",
    "История России",
    "Иностранный язык",
]


def schitat_otsenku(kurs: str) -> int:
    while True:
        otsenka = input(f"Оценка по курсу {kurs}: ")
        if otsenka.isdigit() and 3 <= int(otsenka) <= 5:
            return int(otsenka)
        print("Оценка должна быть целым числом от 3 до 5.")


def statistika_po_kursam() -> None:
    otsenki_po_kursam: dict[str, list[int]] = {kurs: [] for kurs in KURSY}

    while True:
        imya = input("Имя студента (Enter для завершения):\n")
        if not imya:
            break
        for kurs in KURSY:
            otsenki_po_kursam[kurs].append(schitat_otsenku(kurs))

    if not otsenki_po_kursam[KURSY[0]]:
        print("Студенты не введены.")
        return

    for kurs, otsenki in otsenki_po_kursam.items():
        sredniy = sum(otsenki) / len(otsenki)
        print(f"{kurs}: средний балл {sredniy:.2f}, минимальная {min(otsenki)}, максимальная {max(otsenki)}")


if __name__ == "__main__":
    statistika_po_kursam()
