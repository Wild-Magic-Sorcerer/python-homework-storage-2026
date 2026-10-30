STANDARD_DELIMITER = " "


def get_user_input():
    """
    Запрашивает у пользователя строку с числами
    :return: Введенная пользователем строка
    """
    return input("Введите целые числа через пробел:\n")


def parse_and_validate(user_input):
    """
    Преобразует строку в список чисел, пропуская некорректные элементы
    :param user_input: Исходная строка с числами через пробел
    :return: Кортеж из списка валидных чисел и списка пропущенных элементов
    """
    raw_elements = user_input.split(STANDARD_DELIMITER)
    valid_numbers = []
    skipped_elements = []

    for element in raw_elements:
        if not element:
            continue
        try:
            number = int(element)
            valid_numbers.append(number)
        except ValueError:
            skipped_elements.append(element)

    return valid_numbers, skipped_elements


def process_and_print_results(numbers):
    """
    Применяет лямбда-функцию к числам и выводит результаты
    :param numbers: Список проверенных целых чисел
    :return:
    """
    categorize = lambda x: (
        "zero" if x == 0 else (
        "negative" if x < 0 else (
        "positive even" if x % 2 == 0 else "positive odd")
        )
    )

    for number in numbers:
        print(f"{number}: {categorize(number)}")


def print_skipped_elements(skipped):
    """
    Выводит информацию о пропущенных элементах, если они есть
    :param skipped: Список строк, которые не удалось преобразовать в числа
    :return:
    """
    if skipped:
        print("\nСледующие элементы были пропущены (не являются целыми числами):")
        for element in skipped:
            print(f"- {element}")


def main():
    """
    Основная управляющая функция программы
    :return:
    """
    user_input = get_user_input()
    valid_numbers, skipped_elements = parse_and_validate(user_input)

    if not valid_numbers and not skipped_elements:
        print("Вы ничего не ввели.")
        return

    if valid_numbers:
        process_and_print_results(valid_numbers)
    else:
        print("Нет корректных чисел для обработки.")

    print_skipped_elements(skipped_elements)


if __name__ == "__main__":
    main()


