#Practical Q4
#Q2.

#Write a program that calculates how far a satellite travels in one rotation about the Earth. 
#The user is required to enter the satellite’s altitude in kilometres.
#(Use 12,730 km as the Earth’s diameter. )

#Hint:  Use IPO chart in step 1, 
#a flow chart drawn using draw.io in step 2, 
#a table with sample test data and expected output in step 3, 
#use IDLE PYTHON to write a program in step 4, 
#run the program in step 5 to check if you have the following sample output and accuracy level in step 5 
#and provide the needed internal documentation in step 6.

#Step 1: Define the problem 
#Distance = 2*pi*((Diameter_of_Earth/2)+Altitude)

#IPO Chart
#________|INPUT|________|PROCESS|___________|OUTPUT|________
#    altitude_km    |INPUT altitude_km  |   orbit_km     |
#                   |CALCULATE orbit_km |                |
#                   |PRINT orbit_km     |                |
#                   |END                |                |

#Step 2: Develop the algorithm
#Elaborate your flow in details
#(open in L1PRAC2Q4-Q2.drawio)

#Step 3: Test the algorithm -> need to provide test data
#Desk checking (identify logic errors only because there is no program yet)

#TEST NUMBER_____ALTITUDE_KM______ORBIT_KM_________PASS/FAIL________REMARK______
#___1____________100.0____________40620.7930_______PASS_____________
#___2____________1500.235_________49418.7290_______PASS_____________

#Step 4: Code the program

#import math

#PI=math.pi
#DIAMETER_EARTH=12730
#ALTITUDE=float(input("Enter your altitude from ground to the sky at your current location : "))

#ORBIT=float(2*PI*((DIAMETER_EARTH/2)+ALTITUDE))

#print("According to Newton's and Einstein's Law , the distance of the satelite that orbits the Earth 1 cycle will be %.4f kilometres"%ORBIT)

#Step 5: Run the program
#Identify syntax and logic errors

#ubuntu@ubuntu:~$ /bin/python3 /home/ubuntu/python/L1PRAC2Q4-Q2.py
#Enter your altitude from ground to the sky at your current location : 100
#According to Newton's and Einstein's Law , the distance of the satelite that orbits the Earth 1 cycle will be 40620.7930 kilometres

#Step 6: Document and maintain your program 

#Name      : L1PRAC2Q4-Q2.py 
#Purpose   : Six steps program development 
#          : Solve Practical 2 question 4 Q2
#Modules   : math.pi 
#Date      : 4th July 2021 
#Programmer: Gawr Gura

#Accuracy need at the level of math.pi

import math

PI=math.pi
DIAMETER_EARTH=12730
ALTITUDE=float(input("Enter your altitude from ground to the sky at your current location : "))

ORBIT=float(2*PI*((DIAMETER_EARTH/2)+ALTITUDE))

print("According to Newton's and Einstein's Law , the distance of the satelite that orbits the Earth 1 cycle will be %.4f kilometres"%ORBIT)