while True:
    try:
        first_name = input("Enter your first name: ")
        if first_name.isalpha():
            #print(f"Hello, {first_name}!")    
            break  
        if not first_name.isalpha():
            print("Invalid input, please enter a valid name.")
    except ValueError:
        print("Invalid input, please enter a valid name.")


while True:
    try:
        uvId = input("Enter your UVU ID: ")
        if uvId.isdigit():
            #print(f"Your UVU ID is {uvId}.")
            break
        if not uvId.isdigit():
            print("Invalid input, please enter a valid UVU ID.")
    except ValueError:
        print("Invalid input, please enter a valid UVU ID.")

message = f"Hello, {first_name}! Your UVU ID is {uvId}."
print(message)
input("Press Enter to exit.")






