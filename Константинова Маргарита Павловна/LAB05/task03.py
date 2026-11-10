#!/usr/bin/env python3

import argparse
from typing import Final

PORYADOK_PO_VOZRASTANIYU: Final[str] = "asc"
PORYADOK_PO_UBYVANIYU: Final[str] = "desc"
PORYADOK_BEZ_SORTIROVKI: Final[str] = "none"
DOPUSTIMYE_PORYADKI: Final[tuple[str, str, str]] = (
    PORYADOK_PO_VOZRASTANIYU,
    PORYADOK_PO_UBYVANIYU,
    PORYADOK_BEZ_SORTIROVKI,
)
MINIMALNAYA_DOPUSTIMAYA_DLINA: Final[int] = 0
MINIMALNAYA_DLINA_PO_UMOLCHANIYU: Final[int] = 0
OPISANIE_PROGRAMMY: Final[str] = (
    "Выводит переданные строки с фильтрами и сортировкой."
)
EPILOG_SPRAVKI: Final[str] = "Пустой ввод считается неуважением к программе."
SOOBSHCHENIE_PUSTOGO_SPISKA: Final[str] = (
    "вы не передали ни одной строки, а придумывать их за вас "
    "программа не умеет, напишите их после названия скрипта, "
    "например: task03.py яблоко груша"
)


class ArgumentyStrok(argparse.Namespace):
    """Типизированный набор аргументов командной строки."""

    stroki: list[str]
    kolichestvo: bool
    unikalnye: bool
    min_dlina: int
    sort: str


def proverit_minimalnuyu_dlinu(tekst_dliny: str) -> int:
    """Преобразует текст в минимальную длину строки, не меньшую нуля."""
    try:
        dlina_filtra = int(tekst_dliny)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"длина должна быть целым числом, а вы ввели: {tekst_dliny}, "
            "буквы мерить дробями пока не научились"
        ) from None
    if dlina_filtra < MINIMALNAYA_DOPUSTIMAYA_DLINA:
        raise argparse.ArgumentTypeError(
            f"длина не может быть отрицательной, а вы ввели: {tekst_dliny}, "
            "строки с минус одной буквой в природе не встречаются"
        )
    return dlina_filtra


def proverit_poryadok(tekst_poryadka: str) -> str:
    """Проверяет, что порядок сортировки один из допустимых."""
    if tekst_poryadka not in DOPUSTIMYE_PORYADKI:
        raise argparse.ArgumentTypeError(
            f"порядок сортировки '{tekst_poryadka}' не существует, "
            f"выберите один из: {', '.join(DOPUSTIMYE_PORYADKI)}, "
            "творческий подход к сортировке тут не оценят"
        )
    return tekst_poryadka


def otobrat_stroki(
    ishodnye_stroki: list[str],
    tolko_unikalnye: bool,
    minimalnaya_dlina: int,
    poryadok_sortirovki: str,
) -> list[str]:
    """Применяет фильтры по уникальности и длине, затем сортирует строки."""
    otobrannye = (
        list(dict.fromkeys(ishodnye_stroki))
        if tolko_unikalnye
        else ishodnye_stroki
    )
    otobrannye = [
        element for element in otobrannye if len(element) >= minimalnaya_dlina
    ]
    if poryadok_sortirovki == PORYADOK_BEZ_SORTIROVKI:
        return otobrannye
    return sorted(
        otobrannye, reverse=poryadok_sortirovki == PORYADOK_PO_UBYVANIYU
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=OPISANIE_PROGRAMMY,
        epilog=EPILOG_SPRAVKI,
    )
    parser.add_argument("stroki", nargs="*", help="строки для обработки")
    parser.add_argument(
        "--kolichestvo",
        action="store_true",
        help="вывести только количество строк после применения фильтров",
    )
    parser.add_argument(
        "--unikalnye",
        action="store_true",
        help="оставить только уникальные строки",
    )
    parser.add_argument(
        "--min-dlina",
        type=proverit_minimalnuyu_dlinu,
        default=MINIMALNAYA_DLINA_PO_UMOLCHANIYU,
        help="оставить строки длиной не меньше указанного значения",
    )
    parser.add_argument(
        "--sort",
        type=proverit_poryadok,
        default=PORYADOK_BEZ_SORTIROVKI,
        metavar="{asc,desc,none}",
        help="порядок сортировки: asc, desc или none",
    )
    argumenty = parser.parse_args(namespace=ArgumentyStrok())
    if not argumenty.stroki:
        parser.error(SOOBSHCHENIE_PUSTOGO_SPISKA)
    otobrannye_stroki = otobrat_stroki(
        argumenty.stroki,
        argumenty.unikalnye,
        argumenty.min_dlina,
        argumenty.sort,
    )
    if argumenty.kolichestvo:
        print(len(otobrannye_stroki))
    else:
        for stroka_vyvoda in otobrannye_stroki:
            print(stroka_vyvoda)
