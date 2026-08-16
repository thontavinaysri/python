#25341a05l1 vinay
n = int(input("Enter the number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number is", rev)

''' output
Enter the number: 3456
Reversed number is 6543
'''