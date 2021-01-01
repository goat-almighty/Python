a = input('Введите слова: ').split()
for i, word in enumerate(a, 1):
	print(f'{i}, {word[:10]}')