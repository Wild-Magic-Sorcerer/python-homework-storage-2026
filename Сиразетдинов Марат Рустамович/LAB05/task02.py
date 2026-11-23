import argparse

OPERATIONS = ("add", "sub", "mul", "div")
DEFAULT_PRECISION = 2


def calculate(x, y, operation):
    """
    Выполняет математическую операцию над двумя числами
    :param x:первый позиционный аргумент
    :param y:второй позиционный аргумент
    :param operation:тип математической операции: add, sub, mul, div
    :return:строка с вычислением или ошибка
    """
    if operation == "add":
        return x + y
    elif operation == "sub":
        return x - y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        if y == 0:
            raise ValueError("Ошибка: деление на ноль невозможно")
        return x / y
    else:
        raise ValueError(f"Неизвестная операция: {operation}")


def save_to_file(filename, text):
    """
    записывает результат в файл
    :param filename:путь к файлу
    :param text:текст
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        file.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Калькулятор для выполнения операций над двумя числами")
    parser.add_argument("x", type=float, help="первое число")
    parser.add_argument("y", type=float, help="второе число")
    parser.add_argument("--operation", choices=OPERATIONS, help="операции: add, sub, mul, div")
    parser.add_argument("--precision",type=int, default=DEFAULT_PRECISION, help=f"количество знаков после запятой по умолчанию - {DEFAULT_PRECISION}")
    parser.add_argument("--file", help="имя файла для сохранения результата")
    args = parser.parse_args()

    if args.precision < 0:
        parser.error("Точность не может быть меньше 0")

    if not args.operation:
        output = f"Числа: {args.x}, {args.y}"
    else:
        try:
            raw_result = calculate(args.x, args.y, args.operation)
            formatted_result = f"{raw_result:.{args.precision}f}"
            output = (
                f"{args.x} ({args.operation}) {args.y} = {formatted_result}"
            )
        except ValueError as error:
            parser.error(str(error))

    print(output)

    if args.file:
        save_to_file(args.file, output)
