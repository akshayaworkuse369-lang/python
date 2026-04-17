#1 function call
def name():
    print("hello world")
name()

#2 enter a num

def name(num):
    print(num)
name(34)

#3 enter 2 nums and print the sum

def name(a,b):
    print(a+b)
name(3,4)

#4 check the number is positive or negative

def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_sign(1))   
print(check_sign(-5))   
print(check_sign(0)) 


#5 Student Name List . Create a list of at least 5 student names.
#  Use a loop to print each name with a friendly greeting.

student=['ash','shh','sdhh','efc','hyf']
for student in student:
   print(f"hai {student}, where are you going?")