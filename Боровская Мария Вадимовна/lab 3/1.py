#!/usr/bin/env python3


def classify_number(number: int) -> str:
    """
    Классифицирует число с помощью лямбда-функции

    :param number
    :return: Строка с описанием числа
    """
    classify = lambda n: (
        "zero" if n == 0
        else "positive even" if n > 0 and n % 2 == 0
        else "positive odd" if n > 0
        else "negative"
    )
    return classify(number)


def main() -> None:
    """
    Запрашивает числа у пользователя и выводит результат

    :return: None
    """
    raw_str = input("Введите целые числа через пробел: ").strip()

    if not raw_str:
        print("Пусто. Не получилось((")
        return

    numbers = []
    for token in raw_str.split():
        try:
            numbers.append(int(token))
        except ValueError:
            pass

    if not numbers:
        print("Нет ни одного корректного числа. Не получилось((")
        return

    for num in numbers:
        print(f"  {num:>4} — {classify_number(num)}")


main()
