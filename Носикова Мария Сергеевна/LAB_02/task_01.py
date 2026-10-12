### задание №1
STRING_OF_FRUITS = ["яблоко", "апельсин", "помидор", "инжир", "слива", "груша", "маракуйя"]

def filter_length_strings(strings):

    if not strings:
        return print('список пуст')
    
    total_length = 0
    for word in strings:
        total_length += len(word)

    average_length = total_length/ len(strings)

    result = []
    for word in strings:
        if len(word) > average_length:
            result.append(word)
    return result, average_length


if __name__ == '__main__':
    filtered_str, average_length = filter_length_strings(STRING_OF_FRUITS)

    print(f"средняя длина строки: {average_length:.2f}")
    print(f"длинее среднего: {filtered_str}")
