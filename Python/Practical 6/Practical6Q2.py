#Name      : Practical6Q2.py
#Purpose   : 
#Modules   : 
#Date      : 8th August 2021 
#Programmer: Gawr Gura


# Write a program that will output times table(s) whereby the user can control the starting and
# ending times table(s) to be displayed.

# Sample Output:
# (The sample output is incomplete; it is for demonstration purposes only.)
# START: 2
# END: 3
# 2 x 1 = 2
# …
# 2 x 12 = 24
# 3 x 1 = 3
# …
# 3 x 12 = 36

start = int(input("Please enter first number : "))
end = (int(input("Please enter second number : "))) + 1

numbers = range(start, end)

for x in numbers:
    print(x, "x 1 =", x * 1)
    print(x, "x 2 =", x * 2)
    print(x, "x 3 =", x * 3)
    print(x, "x 4 =", x * 4)
    print(x, "x 5 =", x * 5)
    print(x, "x 6 =", x * 6)
    print(x, "x 7 =", x * 7)
    print(x, "x 8 =", x * 8)
    print(x, "x 9 =", x * 9)
    print(x, "x 10 =", x * 10)
    print(x, "x 11 =", x * 11)
    print(x, "x 12 =", x * 12)
