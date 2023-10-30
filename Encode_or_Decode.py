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

def yes(encrypted_message, shift):
    return no(encrypted_message, -shift)

def no(message, shift):
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

Decision =  input("Input 1 to decode or 0 to encode. ")
if Decision == "0":
    message = input("Enter a message: ")
    try:
        shift = int(input("Enter the number to shift the message by: "))
        encrypted_message = encoder(message, shift)
        print("Shifted message:", encrypted_message)
    except ValueError:
        print("Please enter a valid number for the shift.")
elif Decision == "1":
    encrypted_message = input("Enter the encrypted message: ")
    try:
        shift = int(input("Enter the number used to shift the message during encryption: "))
        decrypted_message = yes(encrypted_message, shift)
        print("Decoded message:", decrypted_message)
    except ValueError:
        print("Please enter a valid number for the shift.")
else:
    print("Invalid input.")