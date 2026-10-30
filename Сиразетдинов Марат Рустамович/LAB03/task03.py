import random


def main():
    numbers = [random.randint(-100, 100) for i in range(20)]
    print(f"Исходный список чисел:\n{numbers}")
    divisible_3_not_9 = list(
        filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers)
    )

    more_than_20 = list(
        filter(lambda x: x > 20, numbers)
    )

    both = list(
        filter(lambda x: x < 20 and x % 3 == 0 and x % 9 != 0, numbers)
    )

    print(f"\nДелятся на 3, но не на 9 (длина {len(divisible_3_not_9)}):")
    print(divisible_3_not_9)

    print(f"\nАбсолютное значение > 20 (длина {len(more_than_20)}):")
    print(more_than_20)

    print(f"\nУдовлетворяют обоим условиям (длина {len(both)}):")
    print(both)


if __name__ == "__main__":
    main()

