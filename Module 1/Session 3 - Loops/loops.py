#Use a while loop to print numbers from 1 to 10.

count=0
while count<10:
  count= count+1
  print(count)

#Take input from the user and keep asking until the user enters a password of at least 8 characters (input validation using while loop).
password= input("Enter Password(atleast 8 charters):")
while len(password)<8:
 print("Password is too shoort")
 password= input("Enter Password(atleast 8 charters):")

#Use a for loop to iterate through a list of 5 numbers and print their squares.
num=[3, 43, 34, 25, 598]
for i in num:
  print(i**2)

#Use the range() function to print even numbers from 1 to 20.
for i in range(1, 20):
  if i%2==0:
    print(i)

#Write a program using break to stop printing numbers when the number 7 is reached
for i in range(10):
  print(i)
  if i==7:
    break
  
#Write a program using continue to print only odd numbers from 1 to 10
for i in range(1,10):
  if i%2==0:
    continue
  else:
    print(i)
    
#Write a nested loop to print a 3×3 grid of *
for i in range(3):
  for j in range(3):
     print("*", end=" ")
  print()
   