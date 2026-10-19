def main():
    user_input = input("Введите целые чисоа через пробел:\n")

    raw_elements = user_input.split(" ")
    valid_numbers = []

    for element in raw_elements:
        try:
            number = int(element)
            valid_numbers.append(number)
        except ValueError:
            print("Вы ввели не целое число!")
            return

    lambda_function = lambda x: (
        "zero" if x == 0 else (
            "negative" if x < 0 else (
                "positive even" if x % 2 == 0 else "positive odd"
            )
        )
    )

    if not valid_numbers:
        print("Вы ничего не ввели.")
        return

    for number in valid_numbers:
        print(f"{number}: {lambda_function(number)}")


if __name__ == "__main__":
    main()
