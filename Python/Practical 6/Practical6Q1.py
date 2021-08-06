#Name      : Practical6Q1.py
#Purpose   : 
#Modules   : 
#Date      : 6th August 2021 
#Programmer: Gawr Gura

# Write a program that accepts five integers from the user. Calculate the average and display
# the average to the user.

integers = []

loop = True
while loop:
    integers.append(int(input("Please enter an integer : ")))
    if len(integers) == 5:
        loop = False

print("The average of the five numbers are", sum(integers) / 5)