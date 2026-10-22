#!/usr/bin/env python3

import random

def repeat_n_times(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []

            for i in range(n):
                print(f"попытка {i + 1} из {n})")
                res = func(*args, **kwargs)
                results.append(res)
            return results

        return wrapper

    return decorator

@repeat_n_times(n=3)
def magic_ball(question: str) -> str:
    """Выдает случайное предсказание на заданный вопрос."""
    answers = ["Да, точно!", "Спроси позже", "Шансы невелики", "Абсолютно!"]
    chosen = random.choice(answers)
    return f"Вопрос: {question} | Ответ: {chosen}"


if __name__ == '__main__':
    print("Магический шар:\n")
    final_results = magic_ball("я придумала 3 вопроса. Смогу ли я....")

    print("\nИтоговый список:")
    for item in final_results:
        print(item)