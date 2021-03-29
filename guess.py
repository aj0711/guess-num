import random #載入random

r = random.randint(1, 10) #random的random int隨機整數(從1到100)
while True:
	num = input('Guess? ')
	num = int(num)
	if num == r: 
		print('U R Right')
		break
	elif num < r:
		print('Ans is smaller ')
	else:
		print('Ans is bigger')
