#This code will repeatedly ask the user to input a number and will determine if the number is even or odd. 
#The program will continue until the user types 'q'.
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
user_input = input('Enter option ("c" to check, "q" to quit): ').strip()
if user_input.lower() == 'c':
    user_input = input("Enter a number to check if it's even or odd (or 'q' to quit): ").strip()
while user_input.lower() != 'q':
    if user_input.lstrip('-').isdigit():
        number = int(user_input)
        result = check_even_odd(number)
        print(f"The number {number} is {result}.")
    else:
        print("Invalid input, please enter an integer or 'q' to quit.")
    user_input = input("Enter a number to check if it's even or odd (or 'q' to quit): ").strip()
input("Press Enter to exit")
