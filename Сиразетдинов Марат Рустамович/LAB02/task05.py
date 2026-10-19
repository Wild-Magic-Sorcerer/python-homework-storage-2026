def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n - 1)


def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == "__main__":

    while True:
        str = input("Введите целое неотрицательное число: ").strip()

        try:
            n = int(str)
            if n >= 0:
                break
            else:
                print("Число должно быть неотрицательным!")
        except ValueError:
            print("Для кого написанно? ЦЕЛОЕ ЧИСЛО")

    result_rec = fact_rec(n)
    result_iter = fact_iter(n)

    print(f"Рекурсивный метод: {result_rec}")
    print(f"Итеративным метод: {result_iter}")
