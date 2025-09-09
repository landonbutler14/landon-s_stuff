#This function will cound the number of a specific character in a given string.
def count_character(string, character):
    string = string.lower()
    character = character.lower()
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count


input_string = input("Enter a string: ".strip())

input_character = input("Enter a character to count: ".strip())
result = count_character(input_string, input_character)
print(f"The character '{input_character}' appears {result} times in the string.")
input("Press Enter to exit")
