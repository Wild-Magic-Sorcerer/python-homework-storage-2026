STANDARD_DELIMITER = ","

def filtr(dict):
    vowels = set("аеёиоуыэюяaeiou")
    result = {}
    for key, value in dict.items():
        if not isinstance(value, str):
            continue
        count_v = 0
        for letter in value.lower():
            if letter in vowels:
                count_v += 1
        if count_v >= 3:
            result[key] = value
    return result

if __name__ == "__main__":
    raw = input(f"Введите именованные аргументы в формате ключ=значение, разделяя их {STANDARD_DELIMITER}\nПример:name=Александра,city=Рязань,age=20\n").split(STANDARD_DELIMITER)
    dict_from_raw = {}
    for r in raw:
        r=r.strip()
        if not r:
            continue
        if "=" not in r:
            print("Вы ввели значения не по примеру")
            break
        key, value = r.split("=")
        key = key.strip()
        value = value.strip()
        dict_from_raw[key] = value


    print(f"Пары где значениие это строка с 3 и более гласными: {filtr(dict_from_raw)}")

