#Name      : Practical4Q1.py 
#Purpose   : 
#Modules   : 
#Date      : 6th July 2021 
#Programmer: Gawr Gura

#A transaction record on a sales commission file contains the retail price of an item sold, a
#transaction code that indicates the sales commission category to which an item belongs, and
#the employee number of the person who sold the item. The transaction code can contain the
#values S, M or L, which indicates that the percentage commission will be 5%, 7% or 10%,
#respectively. An error message will be shown if the user enters other than the valid
#transaction codes. Construct a Python program that will read a record on the file, calculate
#the commission owing for that record, and print the retail price, commission and employee
#number on the screen. If error message occurs, the program will be terminated.

employeeNumber=input("Enter the employee number of the person who sold the item : ")
transactionCode=input("Enter the Transaction code : ")
retailPrice=float(input("Enter the retail price : "))

print("The employee id is :",employeeNumber)
if transactionCode[0] == "S":
    percentageCommision=0.05
    print("The percentage commission is %.2f"%percentageCommision)
    print("The retail price is RM%.2f"%retailPrice)
    print("The price after subtract from commision is RM%.2f"%(retailPrice-(retailPrice*percentageCommision)))
    print("The commision is RM%.2f"%(retailPrice*percentageCommision))
elif transactionCode[0] == "M":
    percentageCommision=0.07
    print("The percentage commission is %.2f"%percentageCommision)
    print("The retail price is RM%.2f"%retailPrice)
    print("The price after subtract from commision is RM%.2f"%(retailPrice-(retailPrice*percentageCommision)))
    print("The commision is RM%.2f"%(retailPrice*percentageCommision))
elif transactionCode[0] == "L":
    percentageCommision=0.10
    print("The percentage commission is %.2f"%percentageCommision)
    print("The retail price is RM%.2f"%retailPrice)
    print("The price after subtract from commision is RM%.2f"%(retailPrice-(retailPrice*percentageCommision)))
    print("The commision is RM%.2f"%(retailPrice*percentageCommision))