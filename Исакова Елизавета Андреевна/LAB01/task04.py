alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_count = 0
numbers_for_letters = []
for letter in alphabet:
    alphabet_count += 1
    numbers_for_letters.append(alphabet_count)
dict_letter_number = dict(zip(alphabet, numbers_for_letters))
dict_number_letter = dict(zip(numbers_for_letters, alphabet))


def translate_letters(sentence):
    sentence = sentence.lower()
    result_numbers = []
    for x in sentence:
        if x in dict_letter_number:
            result_numbers.append(str(dict_letter_number[x]))
        elif x == ' ':
            result_numbers.append('0')
        else:
            result_numbers.append(x)
    return ' '.join(result_numbers)


def translate_numbers(sentence):
    sentence_num = sentence.split()
    result_letters = []
    for y in sentence_num:
        if int(y) in dict_number_letter:
            result_letters.append(dict_number_letter[int(y)])
        elif int(y) == 0:
            result_letters.append(' ')
        else:
            result_letters.append(y)
    return ' '.join(result_letters)


if __name__ == '__main__':
    while True:
        data = input('Введите предложение на русском языке '
                     'или последовательность чисел через пробел от 0 до 33 включительно'
                     '(или просто Enter для выхода из программы)\n')
        if data == '':
            print('Программа завершена')
            break

        symbols = data.split()
        all_numbers = True
        valid_range = True

        for symbol in symbols:
            if symbol.isnumeric():
                if not (0 <= int(symbol) <= 33):
                    valid_range = False
                    print('Число должно быть от 0 до 33 включительно! Попробуйте еще раз')
                    break
            else:
                all_numbers = False

        if all_numbers and valid_range:
            print(f'В виде буквенного текста: {translate_numbers(data)}')
        elif not all_numbers:
            print(f'В виде числовой последовательности: {translate_letters(data)}')