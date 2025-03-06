n = int(input('Enter a number to check if its armstrong or not: '))
sum = 0
temp = 0
temp = n
while temp > 0:
    r = temp % 10
    sum += r** 3
    temp //= 10
if n == sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")