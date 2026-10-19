def filter_of_average(strings):
    if not strings:
        return "Вы ничего не ввели!"

    avg = sum(len(s) for s in strings) / len(strings)
    return list(filter(lambda s: len(s) > avg, strings))


if __name__ == "__main__":
    strings: list[str] = input("Ведите строки через пробел:\n").split()

    result = filter_of_average(strings)
    print(result)

