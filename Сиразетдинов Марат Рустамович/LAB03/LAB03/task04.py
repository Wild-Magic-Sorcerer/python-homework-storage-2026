import functools

def repeat(n=3):
    """
    Декоратор верхнего уровня для повторения вызова функции
    :param n: Количество раз, которое нужно запустить декорируемую функцию.
    :return: Сам декоратор, принимающий целевую функцию
    """
    def decorator(func):
        """
        Принимает целевую функцию и возвращает её обертку
        :param func: Декорируемая функция
        :return: Обернутая функция (wrapper)
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Вызывает исходную функцию n раз и собирает результаты в список
            :param args: Позиционные аргументы для исходной функции
            :param kwargs: Именованные аргументы для исходной функции
            :return: Список, содержащий результаты всех выполнений функции
            """
            results = []
            for i in range(1, n + 1):
                res = func(*args, **kwargs)
                results.append(res)
            return results
        return wrapper
    return decorator

@repeat()
def greetings(name):
    """
    Формирует приветственное сообщение для указанного имени
    :param name: Имя пользователя для приветствия
    :return: Строка с приветствием
    """
    return f"Добрый день, {name}!"

def main():
    """
    Основная управляющая функция программы
    :return:
    """
    greet = greetings("Сергей")
    print(f"Список возвращенных значений: {greet}")


if __name__ == "__main__":
    main()
