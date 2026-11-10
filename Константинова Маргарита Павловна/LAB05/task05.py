#!/usr/bin/env python3

import argparse
import secrets
import string
from pathlib import Path
from typing import Final

MINIMALNAYA_DLINA_PAROLYA: Final[int] = 8
MAKSIMALNAYA_DLINA_PAROLYA: Final[int] = 64
DLINA_PO_UMOLCHANIYU: Final[int] = 12
KOLICHESTVO_PO_UMOLCHANIYU: Final[int] = 1
MINIMALNOE_KOLICHESTVO_PAROLEI: Final[int] = 1
KODIROVKA_FAILOV: Final[str] = "utf-8"
REZHIM_DOZAPISI: Final[str] = "a"
KONETS_STROKI: Final[str] = "\n"
OPISANIE_PROGRAMMY: Final[str] = "Генерирует случайные пароли заданной длины."
EPILOG_SPRAVKI: Final[str] = (
    "Пароль никому не сообщайте, даже программе, что его придумала."
)
SOOBSHCHENIE_PUSTOGO_ALFAVITA: Final[str] = (
    "после исключения символов не осталось ни одного символа, "
    "из пустоты пароль не вырастить"
)
STROKA_HODA_RABOTY: Final[str] = (
    "Придумываю пароли, всем отвернуться и не подглядывать..."
)


class GeneratsiyaNevozmozhnaError(Exception):
    """Исключение: после исключения символов паролю не из чего собраться."""


class ArgumentyGeneratora(argparse.Namespace):
    """Типизированный набор аргументов командной строки."""

    dlina: int
    kolichestvo: int
    bez_tsifr: bool
    bez_spetssimvolov: bool
    fail: Path | None


def proverit_dlinu(tekst_dliny: str) -> int:
    """Преобразует текст в длину пароля, допустимо от 8 до 64."""
    try:
        dlina_chislo = int(tekst_dliny)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"длина должна быть целым числом, а вы ввели: {tekst_dliny}, "
            "пароли дробной длины пока никто не придумал"
        ) from None
    if not (
        MINIMALNAYA_DLINA_PAROLYA <= dlina_chislo <= MAKSIMALNAYA_DLINA_PAROLYA
    ):
        raise argparse.ArgumentTypeError(
            f"длина пароля должна быть от {MINIMALNAYA_DLINA_PAROLYA} "
            f"до {MAKSIMALNAYA_DLINA_PAROLYA}, а вы ввели: {dlina_chislo}, "
            "короткий пароль взломают, а длинный вы сами не запомните"
        )
    return dlina_chislo


def proverit_kolichestvo(tekst_kolichestva: str) -> int:
    """Преобразует текст в количество паролей, не меньшее единицы."""
    try:
        kolichestvo_chislo = int(tekst_kolichestva)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "количество должно быть целым числом, "
            f"а вы ввели: {tekst_kolichestva}, паролей по половинке не бывает"
        ) from None
    if kolichestvo_chislo < MINIMALNOE_KOLICHESTVO_PAROLEI:
        raise argparse.ArgumentTypeError(
            "количество паролей должно быть не меньше "
            f"{MINIMALNOE_KOLICHESTVO_PAROLEI}, а вы ввели: "
            f"{kolichestvo_chislo}, ноль паролей это не генерация, "
            "а медитация"
        )
    return kolichestvo_chislo


def sobrat_gruppy_simvolov(
    isklyuchit_tsifry: bool, isklyuchit_spetssimvoly: bool
) -> list[str]:
    """Собирает группы символов, оставшиеся после исключений."""
    ostavshiesya_gruppy = [string.ascii_lowercase, string.ascii_uppercase]
    if not isklyuchit_tsifry:
        ostavshiesya_gruppy.append(string.digits)
    if not isklyuchit_spetssimvoly:
        ostavshiesya_gruppy.append(string.punctuation)
    if not ostavshiesya_gruppy:
        raise GeneratsiyaNevozmozhnaError(SOOBSHCHENIE_PUSTOGO_ALFAVITA)
    return ostavshiesya_gruppy


def sgenerirovat_parol(dlina_parolya: int, dostupnye_gruppy: list[str]) -> str:
    """Генерирует пароль, в котором есть символ из каждой группы."""
    vse_simvoly = "".join(dostupnye_gruppy)
    simvoly_parolya = [secrets.choice(gruppa) for gruppa in dostupnye_gruppy]
    simvoly_parolya += [
        secrets.choice(vse_simvoly)
        for _ in range(dlina_parolya - len(simvoly_parolya))
    ]
    secrets.SystemRandom().shuffle(simvoly_parolya)
    return "".join(simvoly_parolya)


def dopisat_paroli(put_k_failu: Path, spisok_paroley: list[str]) -> None:
    """Дописывает пароли в конец файла по одному в строке."""
    with put_k_failu.open(
        REZHIM_DOZAPISI, encoding=KODIROVKA_FAILOV
    ) as potok_paroley:
        for parol_dlya_zapisi in spisok_paroley:
            potok_paroley.write(f"{parol_dlya_zapisi}{KONETS_STROKI}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=OPISANIE_PROGRAMMY,
        epilog=EPILOG_SPRAVKI,
    )
    parser.add_argument(
        "--dlina",
        type=proverit_dlinu,
        default=DLINA_PO_UMOLCHANIYU,
        help="длина пароля, от 8 до 64",
    )
    parser.add_argument(
        "--kolichestvo",
        type=proverit_kolichestvo,
        default=KOLICHESTVO_PO_UMOLCHANIYU,
        help="сколько паролей сгенерировать",
    )
    parser.add_argument(
        "--bez-tsifr",
        action="store_true",
        help="не использовать цифры",
    )
    parser.add_argument(
        "--bez-spetssimvolov",
        action="store_true",
        help="не использовать специальные символы",
    )
    parser.add_argument(
        "--fail",
        type=Path,
        help="файл, в конец которого дописываются пароли",
    )
    argumenty = parser.parse_args(namespace=ArgumentyGeneratora())
    try:
        gruppy = sobrat_gruppy_simvolov(
            argumenty.bez_tsifr, argumenty.bez_spetssimvolov
        )
    except GeneratsiyaNevozmozhnaError as oshibka:
        parser.error(str(oshibka))
    print(STROKA_HODA_RABOTY)
    paroli = [
        sgenerirovat_parol(argumenty.dlina, gruppy)
        for _ in range(argumenty.kolichestvo)
    ]
    for parol_vyvoda in paroli:
        print(parol_vyvoda)
    if argumenty.fail is not None:
        dopisat_paroli(argumenty.fail, paroli)
        print(
            f"Пароли дописаны в файл {argumenty.fail}, "
            "берегите его как зеницу ока."
        )
