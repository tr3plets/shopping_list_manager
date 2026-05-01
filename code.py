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
                print("5. Search item.")

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

        elif choice == "2":
            old_item = input("Enter item to change: ")
            new_item = input("Enter new item: ")

            with open("shopping_list.txt", "r") as f:
                data = f.readlines()

            with open("shopping_list.txt", "w") as f:
                for line in data:
                    if line.strip() == old_item:
                        f.write(new_item + "\n")
                    else:
                        f.write(line)

            print("Item updated.")
            break

        elif choice == "3":
            delete_item = input("Enter item to delete: ")

            with open("shopping_list.txt", "r") as f:
                data = f.readlines()

            with open("shopping_list.txt", "w") as f:
                for line in data:
                    if line.strip() != delete_item:
                        f.write(line)

            print("Item deleted.")
            break

        elif choice == "5":
            search_item = input("Enter item to search: ")

            with open("shopping_list.txt", "r") as f:
                data = f.readlines()

            found = False

            for line in data:
                if search_item.lower() in line.lower():
                    print("Item found:", line.strip())
                    found = True

            if found == False:
                print("Item not found.")

            break

        elif choice == "4":
            print("Program ended.")
            break