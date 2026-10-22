#!/usr/bin/env python3

def apply_discounts(items: list[dict]) -> list[dict]:
    """
    Считает цену со скидкой для каждого товара.
    Возвращает новый список словарей, не меняя исходный.
    """

    calc_price = lambda p: {
        "name": p["name"],
        "price": p["price"],
        "discount": p["discount"],
        "final_price": p["price"] * (100 - p["discount"]) / 100
    }

    return list(map(calc_price, items))

if __name__ == '__main__':
    products = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]

    updated_products = apply_discounts(products)

    updated_products.sort(key=lambda item: item["final_price"])

    print("Товары с учетом скидки (по возрастанию цены):")
    for item in updated_products:
        print(item)
