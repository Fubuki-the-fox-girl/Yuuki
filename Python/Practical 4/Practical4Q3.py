#Name      : Practical4Q3.py 
#Purpose   : 
#Modules   : 
#Date      : 7th July 2021 
#Programmer: Gawr Gura

#Kuala Lumpur sometimes has very hazy conditions, and this raises health concerns among
#its inhabitants. A pollutant hazard index has been developed. If the index rises above 100,
#the air is listed as “unhealthful”. If the index rises above 200, a “first-stage haze alert” is
#issued and certain activities are restricted. If an index goes over 275, a “second-stage alert”
#is called and more severe restrictions apply. Write a program that takes an input of the daily
#hazard index and identifies the alert situation.

hazardIndex=float(input("Enter today's hazard index : "))

if hazardIndex <= 100:
    print("Please feel free to breath outside :)")
elif 100 < hazardIndex <= 200:
    print("The air for today is unhealthful ...")
elif 200 < hazardIndex <= 275:
    print("!"*30)
    print("EMERGENCY !!!"*3)
    print("First-Stage Haze Alert !!!")
    print("ANNOUNCEMENT !!!")
    print("Certain Activities Are Restricted !!!")
elif hazardIndex > 275:
    print("!"*50)
    print("EMERGENCY !!!"*5)
    print("SECOND-Stage Haze Alert !!!")
    print("ANNOUNCEMENT !!!")
    print("More Severe Restrictions APPLIED !!!")