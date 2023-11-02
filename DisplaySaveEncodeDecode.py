while True:
    print("Menu:")
    print("1. Display Input")
    print("2. Save Input to File")
    print("3. Encode Input")
    print("4. Decode Input")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        break

    for num in choice:
        if num == "1":
            exec(open("Displayscript1.py").read())
        elif num == "2":
            exec(open("Savescript2.py").read())
        elif num == "3":
            exec(open("encodeby5script3.py").read())
        elif num == "4":
            exec(open("decodeby5script4.py").read())
        else:
            print("Invalid choice. Please choose a valid option.")
  
  
  


