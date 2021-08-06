#Name      : Practical5Q3.py
#Purpose   : 
#Modules   : 
#Date      : 7th July 2021 
#Programmer: Gawr Gura

#Create a program to calculate how long takes for a student to get RM10,000 if the student
#deposited RM5,000 into a bank with yearly interest of 2%. The program should give the
#students a yearly report on his account.

import math
initialBalance = float(input("Please enter the deposited amount : "))
interest = 1.02

years = float(math.log(10000/initialBalance)/math.log(interest))

print(f"Initial balance is RM{initialBalance}")
print(f"The interest of the bank is {interest}")
print("The student will get RM10,000 after %.2f years"%years)