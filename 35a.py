#Project Euler, Problem 1, sum of multiples of 3 and 5 below 100

string = input("Enter a number: ")
x = int(string)
for n in (1,x):
    sum = 0
    if n%3 == 0:
        sum = sum + n
    elif n%5 == 0:
        sum = sum + n
print(f"the sum of multiples of 3 and 5 below {x} is {sum}")
