num = int(input("Enter the number to check palindrome or not: "))
if str(num) == str(num)[::-1]:
    print(num, "is a Palindrome.")
else:
    print(num, "is not a Palindrome.")
