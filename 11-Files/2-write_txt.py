text = input("Enter text to write into file: ")

with open("output.txt", "w") as file:
    file.write(text)

print("Text written successfully!")
