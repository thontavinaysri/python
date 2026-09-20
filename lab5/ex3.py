#25341a05l1 vinay
a=input('enter the string:')
b=''
for ch in a:
    b=ch+b
if a==b:
    print('palindrome')
else:
    print('not a palindrome')

'''
output
enter the string:yoho
not a palindrome
'''