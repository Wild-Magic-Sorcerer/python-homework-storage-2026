#!/usr/bin/env python3

PRODUCTS: list[dict] = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]


def main() -> None:
    """
    Обработка списка товаров и расчёт финальных цен.
    """

    updated_products: list[dict] = list( map( lambda item: {**item, "final_price": item["price"] * (1 - item["discount"] / 100)}, PRODUCTS))

    sorted_products: list[dict] = sorted(updated_products, key=lambda x: x["final_price"])

    print("Итоговый список товаров (отсортирован по цене):")
    print("*" * 39)
    for product in sorted_products:
        print(
            f"{product['name']:<12} | "
            f"Цена: {product['price']:>7} | "
            f"Скидка: {product['discount']:>2}% | "
            f"Итого: {product['final_price']:>8.2f}"
        )


if __name__ == "__main__":
    main()
