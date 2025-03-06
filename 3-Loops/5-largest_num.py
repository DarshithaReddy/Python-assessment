a = int(input("Enter 1st number: "))
b = int(input("Enter 2rd number: "))
c = int(input("Enter 3rd number: "))
if a>=b and a>=c:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c
print("largest number is: ", largest)