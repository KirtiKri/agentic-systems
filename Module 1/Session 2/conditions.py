#Take a number as input from the user and check whether it is positive, negative, or zero using if / elif / else.

num = int(input("Enter Number:"))
if num > 0:
    print("Positive Number")
elif num< 0:
    print("Negative Number")
else:
    print("Zero")
    
#Take a number and check whether it is even or odd.

num_1 = int(input("Enter Number:"))
if num_1 % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Write a program using nested if to check:
#If a number is greater than 10
#If yes, check whether it is even or odd

check = int(input("Enter Number:"))
if check > 10:
    print("Number Greater that 10")
    if check % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Number smaller than 10")

#Take two boolean inputs and print the result using logical operators (and, or)

boolean1= (input("Enter 1st boolean (True/False):")) =="True"
boolean2= (input("Enter 2nd boolean (True/False):")) =="True"

print(boolean1 and boolean2)
print(boolean1 or boolean2)

#Write a program to take marks as input and print grade:

marks = int(input("Enter your Marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
