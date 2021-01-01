my_list = input('Введите числа через пробел: ').split()
print(f'Список: {my_list}')
i = 0
while i + 1 < len(my_list):
	if i % 2 == 0:
		my_list.insert(i, my_list.pop(i + 1))
	i += 1
print(f'Получилось: {my_list}')