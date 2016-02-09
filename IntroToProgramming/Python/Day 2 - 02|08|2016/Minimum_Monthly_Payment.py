'''


Author: Bienvenido Rodriguez

Description: Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment.

Use raw_input
Prompt for 3 floating numbers:
1. The outstanding balance of the credit card
2. The annual interest rate
3. The minimum monthly payment

Calculations:
Minimum monthly payment = Minimum monthly payment rate x Balance
Interest Paid = Annual interest rate / 12 months x Balance
Principal paid = Minimum monthly payment – Interest paid
Remaining balance = Balance – Principal paid

'''


def validInterestRate(annualInterestRate):
    if (annualInterestRate < 0):
        print ("%s is less than 0. Please, enter a positive interest rate." %annualInterestRate)
        return 0

'''
Function: validBalance
Description: Check if the balance is valid. So, for example, if someone enters -1.000, make them enter it again.
'''
def validBalance(balance):
    if (balance < 0):
        print ("%s is less than 0. Please, enter a positive balance." %balance)
        return 0


def main():
    while True:
        balance = raw_input("Please, enter your balance: ")
        remBalance = float(balance)
        if (validBalance(remBalance)):
            break
            
    while True:
        annualIR = float(raw_input("Please, enter the annual interest rate: "))
        
        
# 3.0 -> raw_input -> "3.0"