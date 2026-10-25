#!/usr/bin/env python3


PRODUCTS: list[dict] = [
    {'name': 'Laptop', 'price': 89990, 'discount': 10},
    {'name': 'Mouse', 'price': 2490, 'discount': 15},
    {'name': 'Keyboard', 'price': 5490, 'discount': 0},
    {'name': 'Monitor', 'price': 27990, 'discount': 25}
]


def w_final_price(products: list[dict]):
    """
    Функция, которая создает новый список словарей с информацией о товарах
    и добавляет для каждого товара final_price с учётом скидки.

    :param products: Список с информацией о товарах.

    :return: Новый список товаров с final_price.
    """
    final_price = lambda product: {
         **product, 'final_price': product['price'] * (100 - product['discount']) / 100}
    result: list[dict] = list(map(final_price, products))

    return result


def insertion_sort(spisok: list[dict]):
    """
    Функция, которая сортирует список товаров по возрастанию final_price.

    :param spisok: Список с информацией о товарах.

    :return: Отсортированный список товаров.
    """
    n: int = len(spisok)

    for i in range(1, n):
        j: int = i

        while j > 0 and spisok[j]['final_price'] < spisok[j - 1]['final_price']:
            spisok[j], spisok[j - 1] = spisok[j - 1], spisok[j]
            j -= 1

    return spisok


if __name__ == '__main__':
    result_1: list[dict] = w_final_price(PRODUCTS)
    result_2: list[dict] = insertion_sort(result_1)

    print(result_2)
