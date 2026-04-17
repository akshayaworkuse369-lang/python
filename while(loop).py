#1 Print numbers from 1 to 10.
i = 1
while i <= 10:
    print(i)
    i += 1

#2 Print all even numbers from 1 to 20.

num = 2
while num <= 20:
    print(num)
    num += 2

#3 Print all odd numbers from 1 to 20.

num = 1
while num <= 20:
    print(num)
    num += 2




#4 Print multiplication table of a number.
 
number = int(input("Enter a number: "))

i = 1

print(f"Multiplication table of {number}:")

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    
    i += 1


        
#5 Print numbers in reverse (10 to 1).

i = 10

while i >= 1:
    print(i)
    i -= 1



#6 Print sum of numbers from 1 to n.

n = int(input("Enter a number: "))  
sum_total = 0                       
i = 1                               

while i <= n:                       
    sum_total += i                  
    i += 1                         

print("The sum is:", sum_total)



#7 Print squares of numbers from 1 to 10.

i = 1

while i <= 10:
    print(f"The square of {i} is {i*i}")
    
    i += 1

