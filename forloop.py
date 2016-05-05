sum = 0
range_input = int(input("What should the range be?"))
range(range_input)
for i in range(range_input):
    sum = sum + i
    print("The value of i is: ", i)
    print ("The sum is: ",sum-i," + ",i," = ", sum)
    input('')
