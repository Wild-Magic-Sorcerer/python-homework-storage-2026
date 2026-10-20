#!/usr/bin/env python3


products = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]

def process_products(products_list):
    """
    Добавляет final_price к каждому товару и сортирует по возрастанию final_price.
    Исходные словари не изменяются.
    :param products_list: Список словарей товаров.
    :return: Новый список словарей с полем final_price, отсортированный по final_price.
    :rtype: list
    """
    result_list = list(map(
        lambda product: {
            **product,
            "final_price": product["price"] * (1 - product["discount"] / 100),
        },
        products_list,
    ))
    result_list.sort(key=lambda product: product["final_price"])
    return result_list

if __name__ == '__main__':
    result = process_products(products)
    for thing in result:
        print(thing)
