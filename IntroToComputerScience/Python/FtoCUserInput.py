# @author: Ben Rodriguez
# @description: Simple program converting F to C prompted by a user

def FtoCUserInput():

    farenheit = int(input("Please, enter a number to conver to Celsius: "))
    celsius = ((farenheit - 32) / 1.8)
    print(celsius)

FtoCUserInput()
     