#Name      : Practical2Q5.py 
#Purpose   : 
#Modules   : 
#Date      : 5th July 2021 
#Programmer: Gawr Gura


#Write a program to read in a customer’s account balance at the beginning of the month, a
#total of all withdrawals for the month, and a total of all deposits made during the month.
#A federal tax charge of 1% is applied to all transactions made during the month. The
#program calculates the account balance at the end of the month by:
#(1) subtracting the total withdrawals from the account balance at the beginning of the
#month,
#(2) adding the total deposits to this new balance,
#(3) calculating the federal tax, which is 1% of the total transactions (total transactions =
#total withdrawals + total deposits), and
#(4) subtracting this federal tax from the new balance.
#After these calculations, print the final end-of-month balance.

initialAccountBalances=float(input("Please enter your initial account balances : "))
totalWithdrawals=float(input("Enter the amount of moneys that you want to withdraw : "))
totalDeposits=float(input("Please enter the amount of money you want to deposit : "))

finalAccountBalances=initialAccountBalances-(totalWithdrawals*1.01)+(totalDeposits*0.99)
print("OWH Looks like your final account balances left RM%.2f , that's pretty poor ..."%finalAccountBalances)