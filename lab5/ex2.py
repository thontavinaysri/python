#25341a05l1 vinay
a=input('enter the string:')
b=''
for ch in a:
    b=ch+b
print('reversed string is :',b)
#with slicing
print('reversed string is:',a[::-1])

''' 
output
enter the string:something
reversed string is : gnihtemos
reversed string is: gnihtemos
'''