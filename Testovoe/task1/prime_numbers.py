#Написать функцию, возвращающую все простые числа до N

def prime_numbers():
	n = int(input('n='))
	lst=[]
	for i in range(2, n+1):
		for j in lst:
			if i % j == 0:
				break
		else:
			lst.append(i)
	print(lst)

prime_numbers()