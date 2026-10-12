VOWELS = "аеёиоуыэюяaeiouy"

def filter_vowels(**kwargs):
    result = {}
    
    for key, value in kwargs.items():
        if type(value) is str:
            vowels_count = len([char for char in value.lower() if char in VOWELS])

            if vowels_count >= 3:
                result[key] = value
    return result

if __name__ == '__main__':
    print("Тестирование. word1=\"яблоко\", word2=\"gross\", number=\"10\", is_active=\"True\", number2=\"23.5\"")

    final_result = filter_vowels(
        word1="яблокo",
        word2="gross",
        number=10,
        is_active=True,
        number2=23.5
    )
    print(f"Подходящие аргументы (3+ гласных): {final_result}")
