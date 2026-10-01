NUM_TO_TEXT = {
    "1": "а", "2": "б", "3": "в", "4": "г", "5": "д",
    "6": "е", "7": "ё", "8": "ж", "9": "з"}

TEXT_TO_NUM = {
    "а": "1", "б": "2", "в": "3", "г": "4", "д": "5",
    "е": "6", "ё": "7", "ж": "8", "з": "9"
}

def cipher():
	table_to_text = str.maketrans(NUM_TO_TEXT)
	table_to_num = str.maketrans(TEXT_TO_NUM)

	print("Шифр 1: а, 2: б, 3: в, 4: г, 5: д, 6: е, 7: ё, 8: ж, 9: з")

	while True:
		user_input = input("Что будем делать? 1 - шифровать числа в буквы, 2 - буквы в цифры, 3 - ничего не будем ")

		if user_input == "3":
			break
		elif user_input == "1":
			result = input("Введите последовательность чисел: ")
			result = result.translate(table_to_text)
			print(f"Расшифровка: {result}")
		elif user_input == "2":
			result = input("Введите последовательность букв: ")
			result = result.translate(table_to_num)
			print(f"Расшифровка: {result}")
		else:
			print("Ошибка! Введите 1, 2 или 3")

if __name__ == '__main__':
	cipher()
