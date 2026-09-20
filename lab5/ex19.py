#25341a05l1 vinay
a = input("Enter first string: ")
b = input("Enter second string: ")
if sorted(a) == sorted(b):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


''' 
output
Enter first string: some
Enter second string: thing
The strings are not anagrams
'''