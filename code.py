try:
    with open("shopping_list.txt", "x") as f:
        f.write("Created new file successfully.\n")
        
except FileExistsError:
    print("File already exists.")

    with open("shopping_list.txt", "a") as f:
        f.write("Program opened.\n")
        
        while True:
            
            try:
                print("Menu")
                print("1. Add an item.")
                print("2. Change an item.")
                print("3. Remove an item.")    
                print("R. Read file and count lines.")
                print("4. Exit.")

                choice = input("Enter a choice: ")
            
            except ValueError:
                print("Enter a valid choice.")
            
            break
    
    while True:
        if choice == "1":
            itemlist = input("Enter an item: ")
            
            with open("shopping_list.txt", "a") as f:
                f.write(itemlist + "\n")
                
            print("Item added.")
            break

        elif choice.upper() == "R":
            with open("shopping_list.txt", "r") as f:
                lines = f.readlines()

                print("File Contents:")
                
                for line in lines:
                    print(line.strip())

                print("Line Count:", len(lines))
                
            break

        elif choice == "4":
            print("Program ended.")
            break