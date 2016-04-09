# @author: Ben Rodriguez
# @description: Simple program that takes in user inputted numbers, compares them and outputs the larger number

def CompareTwo():
    number_1 = int(input("Please, enter a number: "))
    number_2 = int(input("Please, enter a second number: "))
    
    if (number_1 < number_2):
        print(number_2, " is larger.")
    
    elif (number_1 > number_2):
        print(number_1, " is larger.")
        
    else:
        print(number_1, " and ", number_2, " are equal.")
        
CompareTwo()