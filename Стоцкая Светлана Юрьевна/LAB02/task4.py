ALL_VOWELS = ["a", "e", "i", "o", "u", "y",
              "а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

def many_vowels(**kwargs):
    vowel = 0
    new_dict = {}
    for key, value in kwargs.items():
        for symbol in value:
            if symbol.lower() in ALL_VOWELS:
                vowel += 1
        if vowel >= 3:
            new_dict[key] = value
            vowel = 0
    print(new_dict)


if __name__ == '__main__':
    condition = ""
    input_dict = {}
    while condition != "стоп":
        input_key = input("Введите ключ ")
        input_dict[input_key] = input("Введите значение аргумента ")
        condition = input("Если аргументы закончились, напишите 'стоп' ")
    many_vowels(**input_dict)
