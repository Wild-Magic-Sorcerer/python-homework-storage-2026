def adding_price(products_list):
    '''
    Эта функция рассчитывает для каждого товара из списка финальную цену (с учётом скидок).
    :param products_list: Список словарей с информацией о товарах.
    :return: None: Ничего не возвращает, выводит на экран итоговый отсортированный список товаров.
    '''
    final_list = products_list
    add = lambda x: {"final_price": x["price"] * (100 - x["discount"])/100}
    new_list = list(map(add, products_list))
    numb = len(products_list)
    for item in range(numb):
        final_list[item].update(new_list[item])
    final_list.sort(key=lambda x: x["final_price"])
    print(f"Итоговый список товаров {final_list}")

if __name__ == '__main__':
    dicts_list = []
    condition = "fine"
    while condition:
        name = input("Введите наименование товара ")
        price = float(input("Введите стоимость товара "))
        discount = float(input("Введите скидку на товар "))
        dicts_list.append({"name": name, "price": price, "discount": discount})
        condition = input("Если словари закончились, нажмите Enter ")
    adding_price(dicts_list)
