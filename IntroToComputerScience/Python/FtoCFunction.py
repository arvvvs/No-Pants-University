# Ben Rodriguez
# Description: A simple program to convert F to C using a function


# Function that takes in Farenheit as a parameter
def FtoC(farenheit):
    cel = ((farenheit - 32) / 1.8) # Formula
    print(cel) # Print Celsius conversion
 
# Invoke function with the argument 40   
FtoC(40)