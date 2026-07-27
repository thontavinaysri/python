#25341a05l1 vinay
import keyword

# checking identifier
def is_valid_identifier(name):

    # empty string
    if len(name) == 0:
        return False

    # first character
    if not (name[0].isalpha() or name[0] == "_"):
        return False

    # remaining characters
    for ch in name:
        if not (ch.isalnum() or ch == "_"):
            return False

    # checking keyword
    if keyword.iskeyword(name):
        return False

    return True


# testing
word = input("Enter a name: ")

if is_valid_identifier(word):
    print("Valid Identifier")
else:
    print("Invalid Identifier")

    ''' output
    Enter a name: value_1
Valid Identifier
'''