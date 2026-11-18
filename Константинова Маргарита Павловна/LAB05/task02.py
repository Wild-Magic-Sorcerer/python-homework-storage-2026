#!/usr/bin/env python3

import argparse
from collections.abc import Callable
from pathlib import Path
from typing import Final

SLOZHENIE: Final[str] = "add"
VYCHITANIE: Final[str] = "sub"
UMNOZHENIE: Final[str] = "mul"
DELENIE: Final[str] = "div"
OPERATSII: Final[dict[str, Callable[[float, float], float]]] = {
    SLOZHENIE: lambda slagaemoe1, slagaemoe2: slagaemoe1 + slagaemoe2,
    VYCHITANIE: lambda umenshaemoe, vychitaemoe: umenshaemoe - vychitaemoe,
    UMNOZHENIE: lambda mnozhimoe, mnozhitel: mnozhimoe * mnozhitel,
    DELENIE: lambda delimoe, delitel: delimoe / delitel,
}
SIMVOLY_OPERATSII: Final[dict[str, str]] = {
    SLOZHENIE: "+",
    VYCHITANIE: "-",
    UMNOZHENIE: "*",
    DELENIE: "/",
}
MINIMALNAYA_TOCHNOST: Final[int] = 0
TOCHNOST_PO_UMOLCHANIYU: Final[int] = 2
KODIROVKA_FAILOV: Final[str] = "utf-8"
REZHIM_DOZAPISI: Final[str] = "a"
KONETS_STROKI: Final[str] = "\n"
OPISANIE_PROGRAMMY: Final[str] = (
    "Выполняет арифметическую операцию над двумя числами."
)
EPILOG_SPRAVKI: Final[str] = (
    "Делить на ноль нельзя: математика против, программа тоже."
)
SOOBSHCHENIE_DELENIE_NA_NOL: Final[str] = (
    "делить на ноль нельзя, математики такого не прощают, "
    "а программа тем более: укажите y не равным нулю"
)
STROKA_HODA_RABOTY: Final[str] = (
    "Считаю, не отвлекайте, у меня тут арифметика..."
)


class ArgumentyKalkulyatora(argparse.Namespace):
    """Типизированный набор аргументов командной строки."""

    x: float
    y: float
    operatsiya: str | None
    tochnost: int
    fail: Path | None


def proverit_tochnost(tekst_tochnosti: str) -> int:
    """Преобразует текст в количество знаков, не меньшее нуля."""
    try:
        chislo_znakov = int(tekst_tochnosti)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "точность должна быть целым числом, "
            f"а вы ввели: {tekst_tochnosti}, дробных знаков у знаков не бывает"
        ) from None
    if chislo_znakov < MINIMALNAYA_TOCHNOST:
        raise argparse.ArgumentTypeError(
            "точность не может быть отрицательной, "
            f"а вы ввели: {chislo_znakov}, знаков меньше нуля не бывает"
        )
    return chislo_znakov


def proverit_operatsiyu(tekst_operatsii: str) -> str:
    """Проверяет, что операция одна из допустимых: add, sub, mul или div."""
    if tekst_operatsii not in OPERATSII:
        raise argparse.ArgumentTypeError(
            f"операции '{tekst_operatsii}' не существует, выберите одну из: "
            f"{', '.join(OPERATSII)}, фантазия в арифметике не приветствуется"
        )
    return tekst_operatsii


def vypolnit_operatsiyu(
    nazvanie_operatsii: str,
    pervoe_chislo: float,
    vtoroe_chislo: float,
    znakov_posle_zapyatoi: int,
) -> str:
    """Возвращает строку с выражением и его результатом нужной точности."""
    rezultat = OPERATSII[nazvanie_operatsii](pervoe_chislo, vtoroe_chislo)
    simvol = SIMVOLY_OPERATSII[nazvanie_operatsii]
    return (
        f"{pervoe_chislo} {simvol} {vtoroe_chislo} = "
        f"{rezultat:.{znakov_posle_zapyatoi}f}"
    )


def dopisat_v_istoriyu(put_k_istorii: Path, stroka_zapisi: str) -> None:
    """Дописывает строку в конец файла истории, не трогая прежние записи."""
    with put_k_istorii.open(
        REZHIM_DOZAPISI, encoding=KODIROVKA_FAILOV
    ) as potok_istorii:
        potok_istorii.write(f"{stroka_zapisi}{KONETS_STROKI}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=OPISANIE_PROGRAMMY,
        epilog=EPILOG_SPRAVKI,
    )
    parser.add_argument("x", type=float, help="первое число")
    parser.add_argument("y", type=float, help="второе число")
    parser.add_argument(
        "--operatsiya",
        type=proverit_operatsiyu,
        metavar="{add,sub,mul,div}",
        help="операция: add, sub, mul или div",
    )
    parser.add_argument(
        "--tochnost",
        type=proverit_tochnost,
        default=TOCHNOST_PO_UMOLCHANIYU,
        help="количество знаков после запятой в результате",
    )
    parser.add_argument(
        "--fail",
        type=Path,
        help="файл, в конец которого дописывается результат операции",
    )
    argumenty = parser.parse_args(namespace=ArgumentyKalkulyatora())
    if argumenty.operatsiya is None and argumenty.fail is not None:
        parser.error(
            "сохранять в файл нечего, потому что операция не указана, "
            "добавьте --operatsiya, и результат обязательно найдется"
        )
    if argumenty.operatsiya is None:
        print(argumenty.x, argumenty.y)
    else:
        try:
            stroka_rezultata = vypolnit_operatsiyu(
                argumenty.operatsiya,
                argumenty.x,
                argumenty.y,
                argumenty.tochnost,
            )
        except ZeroDivisionError:
            parser.error(SOOBSHCHENIE_DELENIE_NA_NOL)
        print(STROKA_HODA_RABOTY)
        print(stroka_rezultata)
        if argumenty.fail is not None:
            dopisat_v_istoriyu(argumenty.fail, stroka_rezultata)
            print(
                f"Результат дописан в файл {argumenty.fail}, "
                "прежняя история цела и никуда не делась."
            )
