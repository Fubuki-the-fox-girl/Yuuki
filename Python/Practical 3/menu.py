#Name      : menu.py 
#Purpose   : 
#Modules   : 
#Date      : 5th July 2021 
#Programmer: Gawr Gura

import os
import Practical3Q1 as p1
import Practical3Q2 as p2
import Practical3Q3 as p3

def menu():
    print("\t","-"*40)
    print("\t","-"*15,"Menu","-"*19)
    print("\t","-"*40)

    print("\t","1. Practical 3 Q 1")
    print("\t","2. Practical 3 Q 2")
    print("\t","3. Practical 3 Q 3")
    print("\t","0. Exit")

loop=True
while loop:
    menu()
    choosen=input("Enter a number : ")
    if choosen in ("0","1","2","3"):
        if choosen == "1":
            p1.Q1()
            input("Press enter to continue ...")
            os.system('cls') #For Windows
            os.system('clear') #For Linux
        if choosen == "2":
            p2.Q2()
            input("Press enter to continue ...")
            os.system('cls') #For Windows
            os.system('clear') #For Linux
        if choosen == "3":
            p3.Q3()
            input("Press enter to continue ...")
            os.system('cls') #For Windows
            os.system('clear') #For Linux
        if choosen == "0":
            loop=False
            print("Thanks for playing")
    if choosen not in ("0","1","2","3"):
        print("Error, retry again by entering a number ...")
        input("Press enter to continue ...")
        os.system('cls') #For Windows
        os.system('clear') #For Linux
