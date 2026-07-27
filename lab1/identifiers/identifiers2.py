#25341a05l1 vinay
import keyword

identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(name, "-> Valid Identifier")
    else:
        print(name, "-> Invalid Identifier")

        '''Output:
        import keyword

identifiers = [
    "2value",
    "value_2",
    "_hidden",
    "class",
    "my-var",
    "MyClass",
    "total$"
]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(name, "-> Valid Identifier")
    else:
        print(name, "-> Invalid Identifier")
'''