#!/usr/bin/env python3

def filter_string_args(**kwargs):
    vowels = set("аеёиоуыэюяaeiouy")
    filtered = {}
    for key, value in kwargs.items():
        if isinstance(value, str):
            vowel_count = sum(1 for ch in value.lower() if ch in vowels)
            if vowel_count >= 3:
                filtered[key] = value
    return filtered


if __name__ == "__main__":
    result = filter_string_args(
        name="Вика",
        city="Санкт-Петербург",
        country="Россия",
        number=18,
        greeting="Приветик",
        short="Ау"
    )
    print(result)
