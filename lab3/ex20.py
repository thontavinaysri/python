#25341a05l1 vinay
n=5

for i in range(1, n + 1):
    spaces = n - i
    stars = 2*i-1

    print(" " * spaces + "*" * stars)

    ''' output
     *
   ***
  *****
 *******
*********
    '''