#!/usr/bin/env python3
import argparse
from pathlib import Path


def read_replacement(text: str) -> tuple[str, str]:
    """Разделяет аргумент замены по первому знаку равенства.

    :param text: Запись OLD=NEW
    :return: Искомая строка и строка замены
    """
    old, separator, new = text.partition("=")
    if not separator or not old:
        raise argparse.ArgumentTypeError("Нужен формат OLD=NEW с непустым OLD")
    return old, new


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копирование с заменой.")
    parser.add_argument("--input", required=True, type=Path, help="источник")
    parser.add_argument("--output", required=True, type=Path, help="копия")
    parser.add_argument("--replace", type=read_replacement, metavar="OLD=NEW")
    parser.add_argument("--append-footer", metavar="TEXT", help="подпись")
    parser.add_argument("--overwrite", action="store_true", help="перезапись")
    args = parser.parse_args()

    try:
        content = args.input.read_bytes()
    except FileNotFoundError:
        parser.error(f"Входной файл не найден: {args.input}")
    except OSError as error:
        parser.error(f"Не удалось прочитать входной файл: {error}")

    replacements = 0
    if args.replace is not None:
        old, new = args.replace
        needle = old.encode("utf-8")
        replacements = content.count(needle)
        content = content.replace(needle, new.encode("utf-8"))
    if args.append_footer is not None:
        newline = b"\r\n" if b"\r\n" in content else b"\n"
        if content and not content.endswith((b"\n", b"\r")):
            content += newline
        content += args.append_footer.encode("utf-8") + newline

    mode = "wb" if args.overwrite else "xb"
    try:
        with args.output.open(mode) as target:
            target.write(content)
    except FileExistsError:
        parser.error("Файл уже существует. Для перезаписи укажите --overwrite")
    except OSError as error:
        parser.error(f"Не удалось записать выходной файл: {error}")
    print(f"Количество замен: {replacements}")
