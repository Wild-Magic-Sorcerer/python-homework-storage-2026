#!/usr/bin/env python3


def enrich_products(products: list) -> list:
    """
    Добавляет поле final_price к каждому товару

    :param products
    :return: Новый список словарей с добавленным final_price
    """
    add_final = lambda p: {
        **p,
        "final_price": round(p["price"] * (100 - p["discount"]) / 100, 2)
    }
    return list(map(add_final, products))


def main() -> None:
    """
    Формирует список товаров, обогащает и сортирует его

    :return: None
    """
    products = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]

    enriched = enrich_products(products)
    sorted_items = sorted(enriched, key=lambda x: x["final_price"])

    for item in enriched:
        print(item)

    for item in sorted_items:
        print(item)


main()
