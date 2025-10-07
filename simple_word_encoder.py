#This function will shift each character in the string by a specified number of positions.
def encode_word(chars, shift, direction):
    shifted_string = ""

    if not chars.isdigit() and direction == "right":
        for c in chars:
            stringnumber = ord(c) + shift
            shifted_string += chr(stringnumber)
    elif not chars.isdigit() and direction == "left":
        for c in chars:
            stringnumber = ord(c) - shift
            shifted_string += chr(stringnumber)
    else:
        shifted_string = chars
            
    return shifted_string
# interates throught the string and shifts each character by the specified number of positions then adds the strings together and assgings it to shfited_string variable.
string = input("Enter a string: ").strip()
shift = int(input("Enter the number of positions to shift: "))
direction = input("Enter the direction to shift (left/right): ").lower().strip()
result = encode_word(string, shift, direction)
print(f"The shifted string is: {result}")
input("Press Enter to exit")
    