#This code will collect user name and age and validate the inputs

#Loop for name input validation
while True:
    try:
        name = input("Please enter your name: ")
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be empty")
        
        if not all(part.isalpha() for part in name.split()):
            raise ValueError("Invalid name. Only letters please")
        
        break

    except ValueError:
        print("Invalid input. Please enter a valid name")

#Loop for age input validation
while True:
    try:
        age = input("Please enter your age: ")
        age = age.strip()
        if not age.isdigit():
            raise ValueError("Age must be a positive integer")
        
        age = int(age)
        if age <= 0:
            raise ValueError("Age must be greater than zero")
        
        break

    except ValueError:
        print ("Invalid input. Please enter a valid age")

print(f"Hello, {name}. You are {age} years old.")

input("Press Enter to quit ")
