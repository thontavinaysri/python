#25341a05l1 vinay
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)

'''
output
Enter a string: someone
String after removing duplicates: somen
'''