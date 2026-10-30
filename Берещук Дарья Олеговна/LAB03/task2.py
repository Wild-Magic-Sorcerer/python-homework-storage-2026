
products = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]


if __name__ == "__main__":
    products_with_final = list(map(lambda p: {**p, "final_price": round(p["price"] * (1 - p["discount"] / 100), 2)}, products))
    """распаковываем словарь, получается равный предыдущему, но еще рассчитываю и добавляю туда финальную цену с учетом скидки"""

    sorted_products = sorted(products_with_final, key=lambda p: p["final_price"])
    """сортитовка по финальной цене"""

    print("Отсортировано по final_price:\n")
    for p in sorted_products:
        print(p)


