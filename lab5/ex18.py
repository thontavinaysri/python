#25341a05l1 vinay
s = input("Enter a sentence: ")
result = ""
for word in s.split():
    result += word[0].upper() + word[1:].lower() + " "
print(result)

'''
output
Enter a sentence: python is easy
Python Is Easy 
'''