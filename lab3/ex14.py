#25341a05l1 vinay
n=int(input('enter the number:'))
fact=1
if n==0:
    print('factorial is 1')
else:
    for i in range(1,n+1):
        fact*=i

print('factorial of',n,'is',fact)

''' output
enter the number:4
factorial of 4 is 24
'''