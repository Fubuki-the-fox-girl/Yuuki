#Name      : Practical5Q3.py
#Purpose   : 
#Modules   : 
#Date      : 7th July 2021 
#Programmer: Gawr Gura

#Create a program to calculate how long takes for a student to get RM10,000 if the student
#deposited RM5,000 into a bank with yearly interest of 2%. The program should give the
#students a yearly report on his account.


#       5000 ( 1.02 ) ** ( target - 1 ) > 10000
#            ( 1.02 ) ** ( target - 1 ) > 2000
#        ( target - 1 )math.log( 1.02 ) > math.log(2000)
#                        ( target - 1 ) > (math.log(2000))/(math.log( 1.02 ))
#                                target > 383.83303113564267 + 1
#                                target = 385

import math
initialBalance = 5000
interest = 0.02

print(f"Initial balance is RM{initialBalance}")
print(f"The interest of the bank is {interest}")
print("The student will get RM10,000 after",)