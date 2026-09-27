if __name__ == '__main__':
    sentence = input('Введите предложение:\n')
    sentence_tpl = tuple(sentence.split())
    print(f"Кортеж слов: {sentence_tpl}")

    vowels = 0
    consonants = 0
    punctuation_marks = 0
    punctuation = '.,!?;:()-—«»"\'*/\\[]{}@#$%^&_+=<>|'

    for i in sentence.lower():
        if i in 'aeiouyаеёиоуыэюя':
            vowels += 1
        elif i in 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ':
            consonants += 1
        elif i in punctuation:
            punctuation_marks += 1

    print(f'Количество гласных в вашем предложении: {vowels},\n'
          f'Количество согласных в вашем предложении: {consonants},\n'
          f'Количество знаков препинания в вашем предложении: {punctuation_marks}')

    lst_clean_word = []
    for word in sentence_tpl:
        if word not in punctuation:
            clean_word = word.strip(punctuation)
            if clean_word:
                lst_clean_word.append(clean_word.lower())
    unique_clean_word = (set(lst_clean_word))
    print(f'Количество уникальных слов в вашем предложении:{len(unique_clean_word)}')