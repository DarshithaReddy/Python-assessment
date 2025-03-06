with open("sample.txt", "r") as file:
    file.seek(15)  # Move cursor to index 15
    print(file.read())  # Read from index 15 to the end
