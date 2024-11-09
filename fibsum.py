#sum of numbers in the fibinocci sequence below 4k

x= int(input(' Project Euler, Problem 2\n Enter a large number to fib-sum: ')) 


## create fibonacci sequence ##

fib_list = [0,1]

for num in range(x):
	fib_list.append(fib_list[-1]+fib_list[-2])


## Remove seed numbers ##

fib_list.pop(fib_list[0]) #remove seed numbers
fib_list.pop(fib_list[0]) #remove seed numbers


#### add the numbers ###

# method 1, 1 line
fib_sum = sum(fib_list)

# method 2, five lines 
#fib_sum = 0
#x = 0
#for num in fib_list:
#	x = x-1 
#for evens#		if num%2 == 0:
#for evens#			fib_sum = fib_sum + num 

## method 3, 4 lines, distroys the list 
##but by using "for i in range x" instead of "for num in fib_list" it does go through the entire list instead of stopping because the list shrinks
#fib_sum=0
#for i in range(x):
#	fib_sum = fib_sum + fib_list[0]
#	fib_list.pop(0)


## for smaller sequences ##
print(f"The sum of the even numbers in the sequence {fib_list} is {fib_sum} \n")



### for larger numbers/ longer sequences ###
#print(f"The sum of your sequence is {fib_sum} \n")