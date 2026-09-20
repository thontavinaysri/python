#25341a05l1 vinay
s = input("Enter a string: ")
if s.isdigit():
    print("The string contains only digits")
elif s.isalpha():
    print("The string contains only alphabets")
elif s.isalnum():
    print("The string is alphanumeric")
else:
    print("The string contains special characters")

'''
output
Enter a string: 1234567
The string contains only digits
'''