
#1,6 Check if a number is positive or negative.
    
# a= int(input("enter first number:"))
# if (a>0):
#     print (a," is positive:")
# elif(a<0):
#     print(a," is negative:")
# else:
#     print("number is zero:")

#2 Check whether a number is even or odd.

# a = int(input("enter your age:"))
# if (a%2==0) :
#      print (a,"the number is even:")
# else :
#      print(a,"the number is odd:") 

#3 Check if a person is eligible to vote (age ≥ 18).

# age = 20
# if age >= 18 :
#     print("eligible for vote.")


#4 Check whether a number is divisible by 5.

# num = int(input("Enter a number: "))
# if num % 5 == 0 :
#      print(num,"is divisible by 5.")
# else:
#     print(f"{num} is not divisible by 5.")

#5 Check if a character is a vowel or consonant.

# a = (input("enter a character:"))
# a = a. lower ()
# if a in "aeiou":
#     print(a,"Vowel")
# else:
#     print("Consonant")

#7 Check whether a number is a multiple of 3 and 7.

# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 7 == 0:
#     print(f"{num} is a multiple of both 3 and 7.")
# else:
#     print(f"{num} is not a multiple of both 3 and 7.")

#8 Take a password input and check if it matches a predefined password.

# correct_password = "jack"
# user_input = input("Enter your password: ")
# if user_input == correct_password:
#     print("Access granted!")
# else:
#     print("Access denied.")

#9 Check whether a year is a leap year or not.

# year = 2025
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
#     print(year, "is a leap year.")
# else:
#     print(year,"is not a leap year.")

#10 Simple calculator using if-elif (add, subtract, multiply, divide).

# a = float(input("enter first number:"))
# b = float(input("a second number:"))
# c = input("Choose operation (+, -, *, /): ")
# if c == '+' :
#     print ("result:" , a + b)
# elif c == '-':
#     print("result:" , a-b)
# elif c == '*':
#    print("result:" , a*b)
# elif c == '/':
#  if b != 0:
#     print("Result:", a / b)
#  else:
#     print("Error: Cannot divide by zero")
# else:
#     print("Invalid operation selected.")


#11 Check if a number is divisible by both 2 and 5.

# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 5 == 0:
#      print(f"{num} is a multiple of both 2 and 5.")
# else:
#      print(f"{num} is not a multiple of both 2 and 5.")

# Check whether a number lies between 1 and 100.

# num=int(input("enter a number:" ))
# if(num >=1 and num <=100):
#         print("The number is between 1 and 100.")
# else:
#         print("the numbe is not between 1 an 100.")

#12 Find the smallest among three numbers.

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))
# if(a<b) and(a<c):
#     print (a,"a is smallest:")
# elif (b<c):
#     print(b,"b is smallest:")
# else:
#    print(c,"c is smallest:")

#13 ATM withdrawal (check balance before withdrawal).

# balance = 1000.00
# print("your current balance is :" ,  balance)
# withdraw_amount = float(input("enter amount to withdraw:"))
# if withdraw_amount <= 0:
#     print("error:please enter a positive amount.")
# elif withdraw_amount <= balance:
#     balance -= withdraw_amount
#     print("withdrawal successful! remaining balance:", balance)
# else:
#     print("transaction failes: insufficient balance.")

# Movie ticket pricing: Child (<12) → ₹100 Adult → ₹200 Senior (>60) → ₹150

age=int(input("enter your age"))
if age <12:
    price=100
    print("category:child")
elif age <60:
    price=200
    print("category:adult")
else:
    price=150
    print("category:senior citizen")
print("ticket price:", price)


