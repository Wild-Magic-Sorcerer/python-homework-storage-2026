

STANDARD_DELIMITER = ","

def str_or_not(smth):
    smth = smth.strip()

    if smth == "None":
        return None
    if smth == "True":
        return True
    if smth == "False":
        return False
    try:
        return int(smth)
    except ValueError:
        pass
    try:
        return float(smth)
    except ValueError:
        return smth

if __name__ == "__main__":
    args = input(f"Введите произвольное количество аргументов любых типов через {STANDARD_DELIMITER}\n").split(STANDARD_DELIMITER)
    args_with_int = [ str_or_not(a) for a in args]
    ints = [awi for awi in args_with_int if type(awi) is int]
    if ints:
        result = 1
        for awi in ints:
            result *= int(awi)
        print(f"Произведение целочисленных аргементов:\n{result}")
    else:
        types_of_args = {}
        for awi in args_with_int:
            types_of_args[awi] = type(awi).__name__
        print(f"В выших аргументах нет целочисленных аргументов, вот:\n{types_of_args}")

