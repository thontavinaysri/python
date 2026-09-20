#25341a05l1 vinay
s = input("Enter a string: ")
# String to list
characters = list(s)
print("List:", characters)
# List back to string
result = "".join(characters)
print("String:", result)

''' 
output
Enter a string: hello
List: ['h', 'e', 'l', 'l', 'o']
String: hello
'''