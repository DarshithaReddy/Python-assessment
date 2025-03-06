gender = input("Enter M or F: ").upper()
switch = {'M': "Male", 'F': "Female"}

print(switch.get(gender, "Invalid input"))
