#25341a05l1 vinay
n1=int(input('enter the first number:'))
n2=int(input('enter the second number:'))
n3=int(input('enter the third number:'))
if n1>n2 and n1>n3:
    print(n1,'is the largest number')
elif n2>n1 and n2>n3:
    print(n2,'is the largest number')
else:
    print(n3,'is the largest number')


    ''' output 
    enter the first number:4
enter the second number:54
enter the third number:3
54 is the largest number
'''