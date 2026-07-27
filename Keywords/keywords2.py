#25341a05l1 vinay
import keyword
text = input("Type a word: ")
if keyword.iskeyword(text):
    print(text, "is a reserved Python keyword.")
else:
    print(text, "is not a reserved Python keyword.")

    ''' output
    Type a word: while
while is a reserved Python keyword.
'''