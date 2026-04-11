#Create a list of 5 numbers and print the first and last element using indexing.
lst = [5, 10, 15, 20, 35]
    
print(lst[0], lst[4])
    
#create a list using range() from 1 to 10 and print only even numbers using slicing.
nums= list(range(1, 11))
print(nums[1::2])

#Given a list ['apple', 'banana', 'cherry', 'date'], print the last two elements using negative slicing.
fruits=['apple', 'banana', 'cherry', 'date']
print(fruits[-2:])

#Use a for loop to iterate through a list of numbers and calculate their sum.
num =[2, 3, 4, 5]
sum = 0
for i in num:
    sum= sum + i
print(sum)

#Use a while loop to iterate through a list and print all elements.
a = 0
while a < len(fruits):
    print(fruits[a])
    a= a+1

#Write a function greet(name) that takes a name as a parameter and prints a greeting message.
def greet(name):
    print("Hello", name)
name=input("Enter Your Name:")
greet(name)

#Write a function add(a, b) that returns the sum of two numbers and print the result.
def add(a, b):
    return a + b
result = add(3474, 5379)
print(result)

#Write a function with a default parameter power(base, exponent=2) to calculate exponentiation.
def exponentiation(base, exponent=2):
    return base**exponent
value = exponentiation(3)
print(value)
