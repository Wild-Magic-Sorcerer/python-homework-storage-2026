#!/usr/bin/env python3

import argparse
from typing import Final

MINIMALNYI_VOZRAST: Final[int] = 0
MAKSIMALNYI_VOZRAST: Final[int] = 120
PRIVETSTVIE: Final[str] = "Уважаемый(ая)"
OPISANIE_PROGRAMMY: Final[str] = (
    "Выводит имя пользователя, при желании с возрастом."
)
EPILOG_SPRAVKI: Final[str] = (
    "Возраст от 0 до 120: дальше программа вам не поверит."
)


class ArgumentyPolzovatelya(argparse.Namespace):
    """Типизированный набор аргументов командной строки."""

    imya: str
    vozrast: int | None
    privetstvie: bool


def proverit_vozrast(tekst_vozrasta: str) -> int:
    """Преобразует текст в возраст, допустимый диапазон от 0 до 120."""
    try:
        vozrast_chislo = int(tekst_vozrasta)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"возраст должен быть целым числом, а вы ввели: {tekst_vozrasta}, "
            "программа такого возраста не знает"
        ) from None
    if not MINIMALNYI_VOZRAST <= vozrast_chislo <= MAKSIMALNYI_VOZRAST:
        raise argparse.ArgumentTypeError(
            f"возраст должен быть от {MINIMALNYI_VOZRAST} "
            f"до {MAKSIMALNYI_VOZRAST}, а вы ввели: {vozrast_chislo}, "
            "программа в такое долголетие (или младенчество) не верит"
        )
    return vozrast_chislo


def sobrat_soobshchenie(
    imya_gostya: str,
    vozrast_gostya: int | None,
    nuzhno_privetstvie: bool,
) -> str:
    """Собирает строку с именем, возрастом при наличии и приветствием."""
    soobshchenie = imya_gostya
    if vozrast_gostya is not None:
        soobshchenie = f"{soobshchenie}, возраст: {vozrast_gostya}"
    if nuzhno_privetstvie:
        soobshchenie = f"{PRIVETSTVIE} {soobshchenie}"
    return soobshchenie


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=OPISANIE_PROGRAMMY,
        epilog=EPILOG_SPRAVKI,
    )
    parser.add_argument("imya", help="имя пользователя")
    parser.add_argument(
        "--vozrast",
        type=proverit_vozrast,
        help="возраст, целое число от 0 до 120",
    )
    parser.add_argument(
        "--privetstvie",
        action="store_true",
        help="начать вывод со слов «Уважаемый(ая)»",
    )
    argumenty = parser.parse_args(namespace=ArgumentyPolzovatelya())
    print(
        sobrat_soobshchenie(
            argumenty.imya, argumenty.vozrast, argumenty.privetstvie
        )
    )
