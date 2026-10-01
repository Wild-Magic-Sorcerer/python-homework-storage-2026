def count():
	while True:
		user_answer = input("Введите последовательность чисел: ")
		user_answer = user_answer.replace(",", " ")

		user_answer = user_answer.split()

		numbers  = []

		try:
			for num in user_answer:
				numbers.append(int(num))
			break

		except ValueError:
			print("Ошибка! Введите только целые числа.")

	if len(numbers) == len(set(numbers)):
		print("Повторяющихся элементов в последовательности нет!")
	else:
		print("Повторяющиеся элементы в последовательности присутствуют!")

if __name__ == '__main__':
	count()
