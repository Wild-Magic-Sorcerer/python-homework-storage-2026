#!/usr/bin/env python3

text = input("Введите строку: ")
words = tuple(text.split())
punctuation = ".,!?;:-–—…()[]{}«»„“”\"'‘’"

unique_words = set()
for word in words:
    clean_word = word.lower().strip(punctuation)
    if clean_word != "":
        unique_words.add(clean_word)

vowels = "аеёиоуыэюяaeiou"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
vowel_count = 0
consonant_count = 0
punctuation_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char in punctuation:
        punctuation_count += 1

print("Кортеж слов:", words)
print("Количество уникальных слов:", len(unique_words))
print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)
print("Количество знаков препинания:", punctuation_count)
