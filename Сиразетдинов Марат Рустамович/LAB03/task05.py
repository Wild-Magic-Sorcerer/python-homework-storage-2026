import functools
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(1, n + 1):
                res = func(*args, **kwargs)
                results.append(res)

            return results
        return wrapper
    return decorator

@repeat(n=3)
def greetings(name):
    return (f"Добрый день, {name}!")

def main():
    greet = greetings("Сергей")
    print(f"Список возвращенный значений{greet}!")


if __name__ == "__main__":
    main()