a = int(input("Введите число: "))
max = a % 10

while a >= 1:
	a = a // 10
	if a % 10 > max:
		max = a % 10
	    if a == 9:
		    break
	else:
		print("Самая большая цифра в числе - ", max)
