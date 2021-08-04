#Name      : Practical3Q2.py 
#Purpose   : 
#Modules   : 
#Date      : 6th July 2021 
#Programmer: Gawr Gura

#Write a program that reads an employee’s number, hours worked, and hourly rate and
#calculates his or her wages. All hours over 40 are paid at 1.5 times the regular hourly rate.
#An extra bonus RM200 will be given to those who worked more than 100 hours in total.

def Q2():
    employee=str(input("Enter your name : "))
    employeeNumber=input("Enter your employee number : ")
    hoursWorked=float(input("Enter your total working hours : "))
    hourlyRate=float(input("Enter your hourly rate : RM"))

    print("Your employee Number :",employeeNumber)
    if hoursWorked > 100:
        print("OMG Mr/Mrs",employee ,"JUST WORKED FOR OVER 100 HOURS !!!")
        print("CONGRATS AND HERE'S YOUR RM200 HERE YOU GO")
        print("Your total wages including the rewards are RM%.2f"%((hoursWorked*(hourlyRate*1.5))+200))
    elif hoursWorked > 40:
        print("Dear Mr/Mrs",employee)
        print("Your wages are RM%.2f"%(hoursWorked*(hourlyRate*1.5)))
    else:
        print("Dear Mr/Mrs",employee)
        print("Your wages are RM%.2f"%(hoursWorked*hourlyRate))