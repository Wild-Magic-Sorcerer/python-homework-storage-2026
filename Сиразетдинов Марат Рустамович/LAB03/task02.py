def main():
    """
    Создает список со словорями
    """
    products = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]

    updated_products = (list
            (map
            (lambda x: {
                **x,
                "final_price": round(x["price"] * (1-x["discount"]/100), 2)
            },
             products
             )
         )
     )
    sorter_by_benefits = sorted(updated_products, key=lambda x: x["final_price"])

    for item in sorter_by_benefits:
        print(
            f"{item["name"]} - Цена со скидкой: {item["final_price"]}"
            f" (Цена без скидки: {item["price"]}, Скидка: {item["discount"]}%)"
        )
if __name__ == "__main__":
    main()

