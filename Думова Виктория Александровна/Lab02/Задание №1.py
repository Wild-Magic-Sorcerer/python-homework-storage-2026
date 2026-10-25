#!/usr/bin/env python3

def filter_by_avg_length(strings):
    if not strings:
        return []
    avg_length = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > avg_length]

if __name__ == "__main__":
    test_list = ["малина", "программирование", "ром", "море", "мир"]
    result = filter_by_avg_length(test_list)
    print(f"Исходный список: {test_list}")
    print(f"Средняя длина: {sum(len(s) for s in test_list) / len(test_list):.2f}")
    print(f"Результат: {result}")
