def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

def decode_message(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message

input_message = input("Enter a message: ")
shift_value = int(input("Enter shift value: "))
encode_or_decode = input("Choose (e)ncode or (d)ecode: ").lower()
while True:
    if encode_or_decode in ['e', 'd']:
        break
    encode_or_decode = input("Invalid choice. Please choose (e)ncode or (d)ecode: ").lower()
if encode_or_decode == 'e':
    result = encode_message(input_message, shift_value)
    print(f"Encoded Message: {result}")
elif encode_or_decode == 'd':
    result = decode_message(input_message, shift_value)
    print(f"Decoded Message: {result}")

input("Press Enter to quit ")



