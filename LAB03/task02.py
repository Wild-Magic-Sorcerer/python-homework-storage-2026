new_dict = lambda old_dict: {**old_dict,
                             "final_price":old_dict['price'] * (1 - old_dict["discount"] / 100)}

if __name__ == '__main__':

    products = []
    while True:
        data_name = input('Введите название товара (или Enter для завершения):\n')
        if not data_name.strip():
            break

        price = None
        discount = None

        while True:
            data_price = input('Введите цену на этот товар:\n')
            data_discount = input('Введите скидку на этот товар:\n')

            try:
                price = int(data_price)
                discount = int(data_discount)
            except ValueError:
                print('Цена и скидка должны быть целыми числами!')
                continue

            if price < 0:
                print('Цена не может быть отрицательной!')
                continue
            if discount < 0 or discount > 100:
                print('Скидка должна быть от 0 до 100!')
                continue

            break

        product = {
            "name": data_name.strip(),
            "price": price,
            "discount": discount
        }
        products.append(product)

    result = list(map(new_dict, products))
    result_sorted = sorted(result, key=lambda x: x["final_price"])

    print('Список товаров, отсортированный по финальной цене:')
    for item in result_sorted:
        print(item)
