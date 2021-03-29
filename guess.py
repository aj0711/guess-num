import random #載入random
start = input('Start Number? ')
end = input('End Number? ')
start = int(start)
end = int(end)

r = random.randint(start, end) #random的random int隨機整數(從1到100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('Guess? ')
	num = int(num)
	if num == r: 
		print('U R Right')
		print('This is', count, '次')
		break
	elif num > r:
		print('Ans is smaller ')
	else:
		print('Ans is bigger')
	print('This is', count, '次')