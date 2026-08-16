#25341a05l1 vinay
a=input("enter the character:")
if a.isalpha():
    if a.lower in'aeiou':
        print("vowel")
    else:
        print("consonant")
elif a.isdigit():
    print("digit")
else:
    print("special character")

''' output 
enter the character:%
special character
'''