#Name      : Practical2Q1.py 
#Purpose   : 
#Modules   : 
#Date      : 5th July 2021 
#Programmer: Gawr Gura

#Roger would like to know the average of his test scores. Write a program that can help
#him to calculate the average of 5 test scores from his input.

testScoresLIST=[]

testScores=float(input("Please enter your marks accordingly : "))
testScoresLIST.append(testScores)

testScores=float(input("Please enter your marks accordingly : "))
testScoresLIST.append(testScores)

testScores=float(input("Please enter your marks accordingly : "))
testScoresLIST.append(testScores)

testScores=float(input("Please enter your marks accordingly : "))
testScoresLIST.append(testScores)

testScores=float(input("Please enter your marks accordingly : "))
testScoresLIST.append(testScores)

averageMarks=(sum(testScoresLIST))/5

print("OWH Looks like your results very poor , you only get %.2f average marks ..."%averageMarks)