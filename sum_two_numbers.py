# This program takes two numbers and adds them.
def getInteger(prompt):
    var1 = ""
    while type(var1) is not int:
        try:
            var1 = input (prompt)
            var1 = int(var1)
            return var1
        except ValueError:
            print("Invalid input, please enter integers only.")
    
var1 = getInteger("Enter first number: ")
var2 = getInteger("Enter second number: ")
    
sum = var1 + var2
message = f"The sum of {var1} and {var2} is: {sum}"
print(message)


