# print a message to prompt the user for input
def prompt():
    print("Please enter an integer value: ", end="")


# start of program
print("This program adds together two integers.")
# call the function
prompt()
value1 = int(input())
# call the function again
prompt()
value2 = int(input())
sum = value1 + value2
print(value1, "+", value2, "=", sum)
