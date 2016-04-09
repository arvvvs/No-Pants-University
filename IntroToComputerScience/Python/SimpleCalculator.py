# @author: Ben Rodriguez
# @description: A simple calculator program that takes in two numbers and performs a specific operation on them (+, -, *, /)


def main():
    print("Welcome to the simple calculator!")
    print("Instructions: ")
    print("You will be prompted to input two numbers.")
    print("Then, you will be prompted for an operation noted as 1, 2, 3, or 4.")
    print("Once you have chosen, we will perform the operation.")
    
    user_interaction()
    
def user_interaction():
    
    number_1 = int(input("Please, enter a number: "))
    number_2 = int(input("Please, enter a second number: "))
    
    print("Select Operation: ")
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")
    
    user_input = input("Please, enter a choice: 1, 2, 3 or 4: ")
    
    if user_input == '1':
        print(number_1, "+", number_2, "=", addition(number_1, number_2))
    
    if user_input == '2':
        print(number_1, "-", number_2, "=", subtraction(number_1, number_2))
        
    if user_input == '3':
        print(number_1, "*", number_2, "=", multiplication(number_1, number_2))
        
    if user_input == '4':
        print(number_1, "/", number_2, "=", division(number_1, number_2))
        
def addition(num_1, num_2):
    return num_1 + num_2
    
def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2
    
def division(num_1, num_2):
    return num_1 / num_2
    
main()