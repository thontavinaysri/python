#25341a05l1 vinay
n=int(input('enter a number:'))
if n==1 or n==2:
    print('prime number')
else:
    for i in range(2,n):
        if n%i==0:
            print('not a prime number')
            break

'''output
enter a number:4
not a prime number
'''