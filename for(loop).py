#1 Print numbers from 1 to 10.

for i in range(11):
    print(i)

#2 Print all even numbers from 1 to 20.

for i in range(21):
    if i%2==0:
        print(i)

#3 Print all odd numbers from 1 to 20.

for i in range(21):
    if i%2!=0:
        print(i)


#4 Print multiplication table of a number.       

number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(number,'x', i , '=' ,number * i)
    # print(f"{number} x {i} = {number * i}")


#5 Print numbers in reverse (10 to 1).

for i in range(10 , 0 ,-1):
    print(i)


#6 Print sum of numbers from 1 to n.

total = 0
for i in range(1, 11):
    total += i
    print(total)

#7 Print squares of numbers from 1 to 10. 


for i in range(1, 11):
    square = i*i  
    print(square)
