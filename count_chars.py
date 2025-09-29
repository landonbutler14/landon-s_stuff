#This function will count the number of a specific character in a given string.
def count_character(string, character):
    string = string.lower().strip()
    character = character.lower().strip()
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count


input_string = input("Please enter a string: ")

input_character = input("Enter a character to count: ")
result = count_character(input_string, input_character)
print(f"The character '{input_character}' appears {result} times in the string.")
input("Press Enter to exit")
