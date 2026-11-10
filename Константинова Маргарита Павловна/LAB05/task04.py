#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import Final

RAZDELITEL_ZAMENY: Final[str] = "="
KODIROVKA_FAILOV: Final[str] = "utf-8"
KONETS_STROKI: Final[str] = "\n"
OPISANIE_PROGRAMMY: Final[str] = "Копирует содержимое одного файла в другой."
EPILOG_SPRAVKI: Final[str] = (
    "Входной файл должен существовать, "
    "а выходной должен уметь сопротивляться перезаписи."
)
STROKA_ZAVERSHENIYA: Final[str] = (
    "Копирование завершено, все байты на месте, кроме замененных."
)


class ArgumentyKopirovaniya(argparse.Namespace):
    """Типизированный набор аргументов командной строки."""

    vkhodnoi_fail: Path
    vykhodnoi_fail: Path
    zamena: tuple[str, str] | None
    podval: str | None
    perezapis: bool


def razobrat_zamenu(tekst_zameny: str) -> tuple[str, str]:
    """Разбивает текст формата OLD=NEW на заменяемую и новую строки."""
    staraya_stroka, razdelitel, novaya_stroka = tekst_zameny.partition(
        RAZDELITEL_ZAMENY
    )
    if not razdelitel or not staraya_stroka:
        raise argparse.ArgumentTypeError(
            "замена должна быть в формате OLD=NEW, "
            f"а вы ввели: {tekst_zameny}, мысли программа читать не умеет"
        )
    return staraya_stroka, novaya_stroka


def skopirovat_fail(
    vkhodnoi_put: Path,
    vykhodnoi_put: Path,
    para_zameny: tuple[str, str] | None,
    tekst_podvala: str | None,
) -> int:
    """Копирует файл с заменой и подвалом, возвращает число замен."""
    soderzhimoe = vkhodnoi_put.read_text(encoding=KODIROVKA_FAILOV)
    chislo_zamen = 0
    if para_zameny is not None:
        zamenyaemoe, zamenitel = para_zameny
        chislo_zamen = soderzhimoe.count(zamenyaemoe)
        soderzhimoe = soderzhimoe.replace(zamenyaemoe, zamenitel)
    if tekst_podvala is not None:
        if soderzhimoe and not soderzhimoe.endswith(KONETS_STROKI):
            soderzhimoe += KONETS_STROKI
        soderzhimoe += f"{tekst_podvala}{KONETS_STROKI}"
    vykhodnoi_put.write_text(soderzhimoe, encoding=KODIROVKA_FAILOV)
    return chislo_zamen


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=OPISANIE_PROGRAMMY,
        epilog=EPILOG_SPRAVKI,
    )
    parser.add_argument(
        "--input",
        dest="vkhodnoi_fail",
        metavar="INPUT",
        type=Path,
        required=True,
        help="входной файл",
    )
    parser.add_argument(
        "--output",
        dest="vykhodnoi_fail",
        metavar="OUTPUT",
        type=Path,
        required=True,
        help="выходной файл",
    )
    parser.add_argument(
        "--replace",
        dest="zamena",
        type=razobrat_zamenu,
        metavar="OLD=NEW",
        help="заменить все вхождения строки OLD на строку NEW",
    )
    parser.add_argument(
        "--append-footer",
        dest="podval",
        metavar="FOOTER",
        help="строка, которая добавляется в конец выходного файла",
    )
    parser.add_argument(
        "--perezapis",
        action="store_true",
        help="разрешить перезапись существующего выходного файла",
    )
    argumenty = parser.parse_args(namespace=ArgumentyKopirovaniya())
    if not argumenty.vkhodnoi_fail.is_file():
        parser.error(
            f"входной файл не найден: {argumenty.vkhodnoi_fail}, "
            "копировать воздух программа пока не научилась"
        )
    if not argumenty.vykhodnoi_fail.parent.is_dir():
        parser.error(
            f"папки {argumenty.vykhodnoi_fail.parent} не существует, "
            "программа умеет копировать файлы, но не строить для них дома"
        )
    if argumenty.vykhodnoi_fail.exists() and not argumenty.perezapis:
        parser.error(
            f"выходной файл {argumenty.vykhodnoi_fail} уже существует, "
            "чтобы перезаписать его, добавьте флаг --perezapis, "
            "без него программа не станет затирать чужие труды"
        )
    print(
        f"Копирую файл {argumenty.vkhodnoi_fail} "
        f"в файл {argumenty.vykhodnoi_fail}, байты строятся в колонну..."
    )
    vypolneno_zamen = skopirovat_fail(
        argumenty.vkhodnoi_fail,
        argumenty.vykhodnoi_fail,
        argumenty.zamena,
        argumenty.podval,
    )
    print(f"Выполнено замен: {vypolneno_zamen}")
    print(STROKA_ZAVERSHENIYA)
