# task_04
VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
MIN_VOWELS = 3

def count_vowels(arguments):
    count = 0
    for letter in arguments:
        if letter in VOWELS:
            count += 1
    return count


def filtered_words(data):
    result = {}

    for i, value in data.items():
        if type(value) == str:
            vowels_count = count_vowels(value)
            if vowels_count >= MIN_VOWELS:
                result[i] = value
    return result


def parse_input(user_input):
    result = {}
    for pair in user_input.split(","):
        if "=" in pair:
            key, value = pair.split("=", 1)
            result[key.strip()] = value.strip()
    return result


if __name__ == '__main__':
    print("Введите аргументы через запятую в формате: ключ=значение")
    user_input = input("Введите данные: ")
    lala = parse_input(user_input)
    print(f"Распознанные аргументы: {lala}")
    result = filtered_words(lala)

    if result:
        print(f"Аргументы с 3+ гласными: {result}")
    else: 
        print("подходящих аргументов не найдено.")
