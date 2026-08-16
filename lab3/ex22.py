#25341a05l1 vinay
n=4
a=n
for i in range(0,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(0,n+1):
    print(" "*i+"*"*(2*(n-i)-1))


''' output
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''