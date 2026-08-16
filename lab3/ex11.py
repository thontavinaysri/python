#25341a05l1 vinay
n=int(input('enter the number'))
rev=0
num=n
while n>0:
    digit =n%10
    rev=rev*10 +digit
    n=n//10
if num==rev:
    print('palindrom')
else:
    print('not palindrom')

'''output 
enter the number123321
palindrom
'''