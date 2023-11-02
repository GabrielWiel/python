def encoder(message, shift):
    shifted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            shifted_message += shifted_char
        else:
            shifted_message += char
    return shifted_message

message = input("Enter a message: ")
try:
    shift = 5
    encrypted_message = encoder(message, shift)
    print("Shifted message:", encrypted_message)
except ValueError:
    print("Please enter a valid number for the shift.")