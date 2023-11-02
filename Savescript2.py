user_input = input("Enter a message to save to the file: ")
with open("DisplaySaveEncodeDecode.txt", "w") as file:
    file.write(user_input)
print("Message saved to DisplaySaveEncodeDecode.txt")
