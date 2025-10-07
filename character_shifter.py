#This function will shift each character in the string by a specified number of positions.
def shift_characters(chars, shift, direction):
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
    
string = input("Enter a string: ").strip()
shift = int(input("Enter the number of positions to shift: "))
direction = input("Enter the direction to shift (left/right): ").lower().strip()
result = shift_characters(string, shift, direction)
print(f"The shifted string is: {result}")
input("Press Enter to exit")
    