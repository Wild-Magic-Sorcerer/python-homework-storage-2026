#!/usr/bin/env python3


from random import choice


TARO_CARDS: list[str] = [
    'Звезда',
    'Дьявол',
    'Смерть',
    'Колесо фортуны',
    'Отшельник',
    'Сила',
    'Влюбленные',
    'Император',
    'Верховная жрица',
    'Маг',
    'Шут',
    'Сова на скакалке'
]


def reveal_fortune(n):
    """
    Декоратор, который вызывает функцию n раз
    и возвращает список результатов всех вызовов.

    :param n: Количество вызовов функции.

    :return: Декоратор для повторного вызова функции.
    """
    def decorator(func):
        def inner_func(*args, **kwargs):
            results: list[str] = []

            for i in range(n):
                result: str = func(*args, **kwargs)

                print(f'Получить пророчество №{i + 1}: {result}')
                results.append(result)

            return results

        return inner_func

    return decorator


@reveal_fortune(3)
def draw_card():
    """
    Моя личная функция, которая случайно выбирает карту Таро.

    :return: Название случайно выбранной карты.
    """
    return choice(TARO_CARDS)


if __name__ == '__main__':
    result_1 = draw_card()
