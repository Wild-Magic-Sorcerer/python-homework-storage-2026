#!/usr/bin/env python3

PRODUCTS = [
{"name": "Laptop", "price": 89990, "discount": 10},
{"name": "Mouse", "price": 2490, "discount": 15},
{"name": "Keyboard", "price": 5490, "discount": 0},
{"name": "Monitor", "price": 27990, "discount": 25},
]

def print_products(products):
    """
    Выводит список товаров в удобном формате.

    :param products: Список словарей с информацией о товарах.
    """
    for value in products:
        print(value["name"], "-", value["final_price"], "рублей")


if __name__ == '__main__':
    products_with_price = list(map(
        lambda value: {**value, "final_price": value["price"] * (1 - value["discount"] / 100)}, 
        PRODUCTS
    ))
    sort_products = sorted(products_with_price, key=lambda x: x["final_price"])

    print("Отсортированные по возрастанию товары final_price: ")
    print_products(sort_products)
