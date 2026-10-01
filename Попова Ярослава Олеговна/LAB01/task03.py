VOWELS = "аеёиоуыэюя"
CONSONANTS = "бвгджзйклмнпрстфхцчшщ"
PUNCTUATION = ".,!?;:-()"

def parse_text():
	text = input("Введите строку слов разделенных пробелами:")
	text_tuple = tuple(text.split())

	unique = len(set(text_tuple))
	print(f"Количество уникальных слов: {unique}")

	vowels = 0
	consonants = 0
	punctuation = 0

	for t in text.lower():
		if t in VOWELS:
			vowels += 1
		elif t in CONSONANTS:
			consonants += 1
		elif  t in PUNCTUATION:
			punctuation += 1

	print(f"Гласных букв: {vowels}")
	print(f"Согласных букв: {consonants}")
	print(f"Знаков препинания: {punctuation}")

if __name__ == '__main__':
    parse_text()
