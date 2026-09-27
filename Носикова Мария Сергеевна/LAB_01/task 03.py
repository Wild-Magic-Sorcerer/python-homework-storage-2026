# task 03
def count_signs(text):
    vowels = 0
    consonants = 0
    punctuation = 0
    list_vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    list_consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    list_punctuation = ",./?:;-_!"
    for letter in text:
        if letter in list_vowels:
            vowels += 1
        elif letter in list_consonants:
            consonants += 1
        elif letter in list_punctuation:
            punctuation += 1
    return vowels, consonants, punctuation
def uniqueness(text):
    words = tuple(text.split())
    unique_words = set(words) # для удаления дубликатов
    unique_count = len(unique_words)
    vowels, consonants, punctuation = count_signs(text)
    print(f'Исходная строка:{text}')
    print(f'Кортеж слов:{words}')
    print(f'Количество уникальных слов: {unique_count}')
    print(f'Гласные буквы: {vowels}')
    print(f'Согласные буквы: {consonants}')
    print(f'Знаки препинания: {punctuation}')
if __name__ == '__main__':
    result = input('Введите строку слов, разделенную пробелами:')
    result_str = result.strip()
    uniqueness(result_str)
