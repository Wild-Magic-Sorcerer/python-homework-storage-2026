#!/usr/bin/env python3


def create_dict():
    """
    Функция, которая позволяет пользователю формировать
    список стандартизированных словарей с информацией о товарах.

    :return: Список словарей с информацией о товарах.
    """
    products_list: list[dict] = []
    count: int = int(input('Введите количество товаров: '))

    for _ in range(count):
        name: str = input('Введите название товара: ')
        price: float = float(input('Введите цену товара: '))
        discount: float = float(input('Введите скидку на товар: '))

        product: dict = {
            'name': name,
            'price': price,
            'discount': discount
        }
        products_list.append(product)

    return products_list


def w_final_price(products_list: list[dict]):
    """
    Функция, которая создает новый список словарей с информацией о товарах
    и добавляет для каждого товара final_price с учётом скидки.

    :param products: Список с информацией о товарах.

    :return: Новый список товаров с final_price.
    """
    final_price = lambda product: {
         **product, 'final_price': product['price'] * (100 - product['discount']) / 100}
    result: list[dict] = list(map(final_price, products_list))

    return result


def insertion_sort(spisok: list[dict]):
    """
    Функция, которая сортирует список товаров по возрастанию final_price.

    :param spisok: Список с информацией о товарах.

    :return: Отсортированный список товаров.
    """
    n: int = len(spisok)

    for i in range(1, n):
        j: int = i

        while j > 0 and spisok[j]['final_price'] < spisok[j - 1]['final_price']:
            spisok[j], spisok[j - 1] = spisok[j - 1], spisok[j]
            j -= 1

    return spisok


if __name__ == '__main__':
    products: list[dict] = create_dict()
    result_1: list[dict] = w_final_price(products)
    result_2: list[dict] = insertion_sort(result_1)

    print(result_2)
    
