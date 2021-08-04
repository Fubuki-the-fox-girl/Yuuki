#Name      : Practical3Q1.py 
#Purpose   : 
#Modules   : 
#Date      : 5th July 2021 
#Programmer: Gawr Gura

#Write a program that will receive two integer items from a terminal operator, and display to
#the screen their sum, difference, product and quotient. [Note that the quotient calculation
#(first integer divided by second integer) is only being performed if the second integer does
#not equal zero.]

def Q1():
    integerLIST=[]

    integer=int(input("Enter an integer : "))
    integerLIST.append(integer)

    integer=int(input("Enter an integer again : "))
    integerLIST.append(integer)

    #print(integerLIST)

    print("Sum of the integers are",sum(integerLIST))

    if integerLIST[0]>=integerLIST[1]:
        print("Difference of the integers are",integerLIST[0]-integerLIST[1])
    else:
        print("Difference of the integers are",integerLIST[1]-integerLIST[0])

    print("Product of the integers are",integerLIST[0]*integerLIST[1])

    if integerLIST[1]==0:
        print("Sorry the division gone wrong as the second integer equals to 0")
    else:
        print("Division of the integers are %.4f"%(integerLIST[0]/integerLIST[1]))
