#Name      : Practical3Q3.py 
#Purpose   : 
#Modules   : 
#Date      : 6th July 2021 
#Programmer: Gawr Gura

#An Admission charge for The Little Rep Theater varies according to the age of the person.
#Develop a program to print out the ticket charge given the age of the person. The charges are
#as follows:

#__________Age__________Fee___________
#__________>55__________RM7___________
#__________13-55________RM10__________
#__________3-12_________RM5___________
#__________<3___________FREE__________

def Q3():
    age=int(input("Please enter the customer age : "))

    if age > 55:
        print("The fees need to be paid are RM7")
    elif age >= 13 and age <= 55:
        print("The fees need to be paid are RM10")
    elif age >= 3 and age <= 12:
        print("The fees need to be paid are RM5")
    else:
        print("The fees NO NEED to be paid!!!!!")