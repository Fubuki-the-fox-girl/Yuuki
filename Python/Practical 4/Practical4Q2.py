#Name      : Practical4Q2.py 
#Purpose   : 
#Modules   : distutils.util
#Date      : 6th July 2021 
#Programmer: Gawr Gura 

#A university uses three criteria to determine if a first-year student athlete is eligible to play a
#sport during the first semester of college. Only two of the three criteria must be met to be
#eligible. The criteria are as follows:
#• scored 18 or higher on the ACT (American College Test),
#• graduated in the top half of their high school class, and
#• have a 2.0 grade point average or higher on a four-point scale.
#Develop a program that can show whether the user is eligible or not eligible to play a sport.

from distutils.util import strtobool

scoring = strtobool(input("Are your scored 18 or higher on the ACT ? : (y/N) "))
graduated = strtobool(input("Are you graduated in the top half of your high school class ? : (y/N) "))
grade = strtobool(input("Do you have a 2.0 grade point average or higher on a four-point scale ? (y/N) "))

if scoring+graduated+grade >= 2:
    print("CONGRATS !! You are eligible to play a sport !!")
else:
    print("Sorry , you are not eligible to play a sport ...")