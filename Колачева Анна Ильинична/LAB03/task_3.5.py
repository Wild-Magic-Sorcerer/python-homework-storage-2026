def repeat_n_times(n: int):
    """
    Декоратор для многократного вызова функции.
    
    :param n: Количество повторений
    :type n: int
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results: list = []
            for i in range(1, n + 1):
                print(f"Попытка №{i}: {func.__name__}...")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


@repeat_n_times(3)
def ask_for_extension(deadline: str) -> str:
    """
    Просит преподавателя продлить дедлайн.
    
    :param deadline: Дата дедлайна
    :type deadline: str
    :return: Ответ преподавателя
    """
    return f"Нет, сдавай до {deadline}!"


def main() -> None:
    """
    Основная функция.
    """
    answers: str = ask_for_extension("понедельника")
    
    print("\nРезультаты переговоров:")
    print("-" * 30)
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()