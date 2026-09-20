#25341a05l1 vinay
s = input("Enter a string: ")
ch = input("Enter character: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Count:", count)

'''
output
Enter a string: nothing there
Enter character: nothing
Count: 0
'''