#!/usr/bin/env python3
from typing import Callable

PRODUCTS = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]


def add_final_price(products: list[dict]) -> list[dict]:
    """
    Добавляет к каждому товару поле final_price, цену со скидкой.

    :param products: Список словарей с полями name, price и discount
    :type products: list[dict]
    :return: Новый список новых словарей с полем final_price
    """
    return list(map(
        lambda product: {
            **product,
            "final_price": product["price"] * (100 - product["discount"]) / 100
        },
        products))


def merge_sort(items: list[dict], key: Callable[[dict], float]) -> list[dict]:
    """
    Сортирует список по возрастанию значения key(item) слиянием.

    :param items: Исходный список, он не меняется
    :type items: list[dict]
    :param key: Функция, которая по элементу даёт значение для сравнения
    :type key: Callable[[dict], float]
    :return: Новый отсортированный список
    """
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = merge_sort(items[:middle], key)
    right = merge_sort(items[middle:], key)
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


with_prices = add_final_price(PRODUCTS)
print("Товары с итоговой ценой:")
for product in with_prices:
    print(product)
ordered = merge_sort(with_prices, lambda product: product["final_price"])
print("По возрастанию final_price:")
for product in ordered:
    print(product)
print("Исходные товары без изменений:")
for product in PRODUCTS:
    print(product)
