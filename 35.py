#Project Euler, Problem 1, sum of multiples of 3 and 5 below 1000
sum = 0
for n in (1,1000):
	if n%3 == 0:
		sum = sum + n
	elif n%5 == 0:
	    sum = sum + n
print(sum)

