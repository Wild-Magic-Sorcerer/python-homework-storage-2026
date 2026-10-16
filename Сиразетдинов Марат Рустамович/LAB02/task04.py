VOWELS: str = "аеиоуыэюя"
MIN_VOWELS = 3


def triple_shafl(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            vowels_count = sum(1 for s in value.lower() if s in VOWELS)
            if vowels_count >= MIN_VOWELS:
                result[key] = value

    return result


if __name__ == "__main__":
    user_data = {}
    counter = 1

    print("Введите слова")

    while True:
        value = input(f"Введите слово №{counter}: ").strip()
        if not value:
            break

        key = f"slovechko №{counter}"
        user_data[key] = value
        counter += 1

    filtered_result = triple_shafl(**user_data)

    print("Результат:")
    print(filtered_result)