VOWELS = ("a", "e", "i", "o", "u", "а", "е", "ё", "и", "о", "у", "ы", "э",
          "ю", "я")
PUNCTUATION = (",", ".", "!", "?", "-", ":", ";", "'", '"', "(", ")")

def words(line):
    punctuation_count = 0
    for element in line:
        if element in PUNCTUATION:
            punctuation_count += 1
            line = line[:element] + line[element+1:]
    words_tuple = tuple(line.split())
    line_set = set(words_tuple)
    unique_words = len(line_set)
    print(f"Количество уникальных слов в строке {unique_words}")
    vowel_count = 0
    consonant_count = 0
    for letter in line:
        if letter in VOWELS:
            vowel_count += 1
        elif letter.isalpha():
            consonant_count += 1
    print(f"Количество гласных {vowel_count}", f"Количество согласных {consonant_count}",
          f"Количество знаков препинания {punctuation_count}")

if __name__ == '__main__':
    some_string = input("Введите какую-нибудь строку ")
    words(some_string)
