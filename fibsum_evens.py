#sum of EVEN numbers in fibinocci sequence below 4k

x= int(input(' Project Euler, Problem 2\n Sum of only even numbers of the fibonacci sequence\n Enter a number to fib-sum: ')) 


## create fibonacci sequence ##

fib_list = [0,1]

for num in range(x):
	fib_list.append(fib_list[-1]+fib_list[-2])


## Remove seed numbers ##

fib_list.pop(fib_list[0]) #remove seed numbers
fib_list.pop(fib_list[0]) #remove seed numbers


#### add the numbers ###
fib_sum = 0
x = 0
for num in fib_list:
	x = x-1 
	if num%2 == 0:
		fib_sum = fib_sum + num 

 
 ## for smaller sequences ##
print(f"The sum of the even numbers in the sequence {fib_list} is {fib_sum} \n")



## for larger numbers/ longer sequences ###
#print(f"The sum of your sequence is {fib_sum} \n")