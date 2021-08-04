#Name      : Practical5Q1.py 
#Purpose   : 
#Modules   : 
#Date      : 7th July 2021 
#Programmer: Gawr Gura

#Construct a program that will accept Fahrenheit temperature, convert it to Celsius and
#display the converted temperature to the screen. The program will continue to process
#until a sentinel of 999 is entered.

import os

loop=True
while loop:
    print("Enter 999 to quit the program ...")
    fahrenheit=(input("Enter the current temperature : (in Fahrenheit) "))
    if fahrenheit not in ("999"):
        fahrenheit=float(fahrenheit)
        celsius=(fahrenheit-32)*5/9
        print("Your current temperature is %.2f degree Celsius"%celsius)
        input("Press enter to continue ...")
        os.system('clear') #For Linux
        os.system('cls') #For Windows
    elif fahrenheit in ("999"):
        loop=False
        fahrenheit=float(fahrenheit)
        celsius=(fahrenheit-32)*5/9
        print("Your current temperature is %.2f degree Celsius"%celsius)
        print("Thanks for playing this temp converter")