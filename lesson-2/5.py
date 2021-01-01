rating = [8, 7, 6, 6, 6, 5, 5, 4, 3, 2, 2, 1]
a = int(input('Введите новый элемент рейтинга: '))
b = 0
for i in rating:
	if a <= i:
		b += 1
rating.insert(b, a)
print(rating)