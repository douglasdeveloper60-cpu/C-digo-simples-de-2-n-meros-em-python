n = float(input("numero 1: "))
m = float(input("numero2: "))

if n >= m:
	print("maior ou igual")
	if n % 2 == 0 and m % 2 == 0:
		print("numero 1 e 2 é par")
	elif n % 2 == 0 and m % 2 == 1:
		print("numero 1 é par e numero 2 é impar")
	elif n % 2 == 1 and m % 2 == 0:
		print("numero 1 é impar e numero 2 é par")
	else:
		print("numero 1 e 2 é impar")
elif m >= n:
	print("menor ou igual")
	if n % 2 == 0 and m % 2 == 0:
		print("numero 1 e 2 é par")
	elif n % 2 == 0 and m % 2 == 1:
		print("numero 1 é par e numero 2 é impar")
	elif n % 2 == 1 and m % 2 == 0:
		print("numero 1 é impar e numero 2 é par")
	else:
		print("numero 1 e 2 é impar")
