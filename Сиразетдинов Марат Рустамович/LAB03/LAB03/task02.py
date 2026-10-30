PRODUCTS = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]


def calculate_final_prices(products):
    """
    Рассчитывает финальную цену для каждого товара без изменения исходного списка
    :param products: Исходный список словарей товаров
    :return: Новый список словарей с добавленным полем final_price
    """
    return list(map(lambda x: {**x, "final_price": round(x["price"] * (1 - x["discount"] / 100), 2)}, products))


def sort_ruchkami(products):
    """
    Сортирует список товаров по возрастанию финальной цены ручным пузырьковым методом
    :param products: Список товаров с рассчитанными ценами
    :return:
    """
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j]["final_price"] > products[j + 1]["final_price"]:
                products[j], products[j + 1] = products[j + 1], products[j]


def main():
    """
    Основная управляющая функция программы
    :return:
    """
    updated_products = calculate_final_prices(PRODUCTS)

    sort_ruchkami(updated_products)

    for item in updated_products:
        print(item)


if __name__ == "__main__":
    main()
