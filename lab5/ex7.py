#25341a05l1 vinay
a=input('enter the string:')
b=''
for ch in a:
    if ch.isspace():
        continue
    else:
        b=b+ch
print('string without spaces is :',b)

'''
output
enter the string:gmritdu college
string without spaces is : gmritducollege
'''