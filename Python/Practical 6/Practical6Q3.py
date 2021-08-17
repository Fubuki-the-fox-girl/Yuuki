#Name      : Practical6Q3.py
#Purpose   : 
#Modules   : 
#Date      : 8th August 2021 
#Programmer: Gawr Gura


# Write a program that will display the following outputs. Total number of lines to be printed
# is determined by the user.

# (i) Lines: 3
#     *
#     **
#     ***

# (ii) Lines: 3
#         *
#        ***
#       *****

lines = int(input("How many lines you want ? : "))
times = 0
print("Lines :", lines)
loop = True
while loop:
    times = times ++ 1
    if times != lines:
        for i in range(0, 2, 1):
            for x in range(0, i+1, 1):
                print("*")
        

    else:
        loop = False
