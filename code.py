try:
    with open("shopping_list.txt", "x") as f:
        f.write("Created new file successfully.")
        
except FileExistsError:
    print("File already exists.")

    with open("shopping_list.txt", "w") as f:
        f.write("Overwritten existing file.")