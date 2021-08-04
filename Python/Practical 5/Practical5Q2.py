#Name      : Practical5Q2.py
#Purpose   : 
#Modules   : 
#Date      : 7th July 2021 
#Programmer: Gawr Gura

#Construct a program that will prompt for and receive the time expressed in 2400 format
#(e.g 2305 hours), convert it to 12-hour format (e.g 11.05pm) and display the new time to
#the screen. Your program is to repeat the processing until a sentinel time of 9999 is
#entered. 


import os
from datetime import datetime

loop = True
while loop:
    print("Enter 9999 to quit the program ....")
    twentyfour = input("Enter a 24-hour format to be convert to 12-hour format later on : (Exp : 2305) " )
    if twentyfour not in ("9999"):
        twelve = datetime.strptime(twentyfour, "%H%M")
        twelve = twelve.strftime("%I:%M %p")
        print("The 12-hour format of",twentyfour, "is",twelve)
        input("Press enter to continue ...")
        os.system('cls') #For Windows
        os.system('clear') #For Linux
    elif twentyfour in ("9999"):
        loop = False
        print("Thanks for playing the time ...")