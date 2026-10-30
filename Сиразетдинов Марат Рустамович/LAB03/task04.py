from functools import reduce


def main():
    user_input = input("Введите слова через пробл:")
    words = user_input.split()

    if not words:
        print("Вы ничего не ввели")
        return

    filtered_words = list(
        filter(lambda word:len(word) > 7, words)
    )
    print(f"Слова длинной не менее 7: {filtered_words}")

    pairs = list(
        map(lambda word: (word, len(word)),
            filtered_words)
    )
    print(f"Пары: {pairs}")

    londest_word = reduce(
        lambda a, b: a if a[1] > b[1] else b,
        pairs
    )
    print((f"Самое длинное слово: {londest_word}"))

    counter = reduce(
        lambda current_sum, element: current_sum + element[1],
        pairs,
        0
    )
    print(f"Число букв: {counter}")
if __name__ == "__main__":
    main()

