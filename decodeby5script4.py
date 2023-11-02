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

encrypted_message = input("Enter the encrypted message: ")
try:
    shift = 5
    decrypted_message = yes(encrypted_message, shift)
    print("Decoded message:", decrypted_message)
except ValueError:
    print("Please enter a valid number for the shift.")
