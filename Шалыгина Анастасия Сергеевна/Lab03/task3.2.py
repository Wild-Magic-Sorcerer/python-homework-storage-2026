#!/usr/bin/env python3


def main():
    """
Вычисляет итоговую цену товаров с учётом скидки и сортирует их по возрастанию
    """
    products: list =  [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]
    final_price = lambda product:{**product, "final_price": product["price"] * (1-product["discount"]/100)}
    products_with_final_price = list(map(final_price, products))
    sorted_products = sorted(products_with_final_price, key=lambda x: x["price"])
    print("Исходный список товаров:")
    for product in products:
        print(f' {product}')
    print('\n Отсортированный список продуктов:')
    for product in sorted_products:
        print(
            f"{product['name']},"
            f"цена = {product['price']}",
            f"скидка = {product['discount']}",
            f"итоговая цена = {product['final_price']}"
        )


if __name__ == '__main__':
    main()
