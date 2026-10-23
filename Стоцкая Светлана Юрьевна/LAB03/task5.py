def decorator_with_n(arg):
    '''
    Декоратор, декорирующий функцию и вызывающий её n раз. Перед каждым вызовом выводит сообщение.
    :param arg: Количество раз, которое функция будет вызвана.
    :return: Список результатов всех вызовов функции.
    :returntype: list
    '''
    def decorator(func):
        def inner_func(*args, **kwargs):
            final_list = []
            print("Вызываем глупенькую функцию для преобразования чисел...")
            for i in range(arg):
                final_list.append(func(*args, **kwargs))
            return final_list
        return inner_func
    return decorator

def useless_func(value):
    '''
    Эта функция умножает полученное число на 3 и прибавляет к значению 1.
    :param value: Какое-то число.
    :return: None: Ничего не возвращает, выводит на экран итоговое значение.
    :raises: ValueError: При подаче значений, которые нельзя преобразовать в число.
    '''
    try:
        final_value = float(value)
        final_value = (final_value * 3) + 1
        return final_value
    except ValueError:
        return "Мне нужно число, а не другое значение!"

useless_func = decorator_with_n(5)(useless_func)

if __name__ == '__main__':
    print(useless_func(1))
