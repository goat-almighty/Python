profit = input("Введите выручку: ")
costs = input("Введите издержки: ")
if profit > costs:
	print(f"Фирма работает с прибылью. Рентабельность составляет {profit / costs}")
	workers = input("Введите количество сотрудников: ")
	print(f"Прибыль на одного сотрудника составила {profit / workers}")
elif profit == costs:
	print("Фирма работает в ноль")
else:
	print("Фирма работает в убыток")