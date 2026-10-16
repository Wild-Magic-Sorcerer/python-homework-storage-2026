STANDARD_DELIMITER = " "


if __name__ == "__main__":
    users_tuple = tuple(input(f"Введите строку слов, разделенных {STANDARD_DELIMITER} \n").split())
    unique_el = len(set(users_tuple))
    VOWELS = set("аеёиоуыэюя")
    CONSONANTS = set("бвгджзйклмнпрстфхцчшщ")
    PUNCTUATION_MARKS = set(".,;:?\"!-'")
    vowels_count = 0
    consonants_count = 0
    punct_count = 0
    for word in users_tuple:
        for letter in word:
            if letter.lower() in VOWELS:
                vowels_count += 1
            elif letter.lower() in CONSONANTS:
                consonants_count += 1
            elif letter.lower() in PUNCTUATION_MARKS:
                punct_count += 1
            else:
                continue
    print(f"Уникаальных слов {unique_el}\n"
          f"Всего {vowels_count} гласных, {consonants_count} согласных, {punct_count} знаков пунктуации")


