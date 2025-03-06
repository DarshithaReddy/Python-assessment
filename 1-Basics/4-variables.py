# Global variable
name = "Global Darshitha"

def display_name():
    # Local variable
    name = "Local Darshitha"
    print("Inside function (Local Variable):", name)

# Calling function
display_name()

# Printing the global variable
print("Outside function (Global Variable):", name)
