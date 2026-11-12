LETTERS_TO_NUM = {"а": "01", "б": "02", "в": "03", "г": "04", "д": "05",
    "е": "06", "ё": "07", "ж": "08", "з": "09", "и": "10",
    "й": "11", "к": "12", "л": "13", "м": "14", "н": "15",
    "о": "16", "п": "17", "р": "18", "с": "19", "т": "20",
    "у": "21", "ф": "22", "х": "23", "ц": "24", "ч": "25",
    "ш": "26", "щ": "27", "ъ": "28", "ы": "29", "ь": "30",
    "э": "31", "ю": "32", "я": "33", ".":"34", ",":"35", "!":"36", "?":"37", ":":"38", "-":"39", " ":"40"}

NUM_TO_LETTERS = {"01": "а", "02": "б", "03": "в", "04": "г", "05": "д",
    "06": "е", "07": "ё", "08": "ж", "09": "з", "10": "и",
    "11": "й", "12": "к", "13": "л", "14": "м", "15": "н",
    "16": "о", "17": "п", "18": "р", "19": "с", "20": "т",
    "21": "у", "22": "ф", "23": "х", "24": "ц", "25": "ч",
    "26": "ш", "27": "щ", "28": "ъ", "29": "ы", "30": "ь",
    "31": "э", "32": "ю", "33": "я","34": ".","35": ",","36": "!","37": "?","38": ":","39": "-","40": " "}

PUNCTUATION = set(".,!?:- ")

def encode(users_input):
    text = users_input.lower()
    result = []
    for el in text:
        if el in LETTERS_TO_NUM:
            new_el = LETTERS_TO_NUM[el]
            result.append(new_el)
        else:
            continue
    filal_result=str("".join(result))
    print(f"{filal_result}")

def decode(users_input):
    text = users_input.lower()
    result = []
    for i in range(0, len(text), 2):
        couple_el = text[i:i+2]
        if couple_el in NUM_TO_LETTERS:
            result.append(NUM_TO_LETTERS[couple_el])
        else:
            continue
    filal_result = str("".join(result))
    print(f"{filal_result}")

if __name__ == "__main__":
    users_input = input("Введите свой текст\n")
    if users_input.isdigit():
        decode(users_input)
    else:
        digit_inside_text= any(el.isdigit() for el in users_input)
        smth_unknown_inside_text = any(el.lower() not in LETTERS_TO_NUM and el.lower() not in PUNCTUATION for el in users_input)
        if digit_inside_text:
            print("Буквы и цифры мешать нельзя")
        elif smth_unknown_inside_text:
            print("Неивестные символы в вашем тексте")
        else:
            encode(users_input)