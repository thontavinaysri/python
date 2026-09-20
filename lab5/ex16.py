#25341a05l1 vinay
s = input("Enter a sentence: ")

words = s.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

''' 
output
Enter a sentence: nothing there
Longest word: nothing
'''