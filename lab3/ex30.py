#25341a05l1 vinay
n=4
for i in range(1,n+1):
    if i==n:
        print("* "*(2*n))
    else:
        print("* "*i," "*(n+2-2*i),"* "*i)
for i in range(n-1,0,-1):
    print("* "*i," "*(n+2-2*i),"* "*i)


''' output
*       *
* *     * * 
* * *   * * * 
* * * * * * * * 
* * *   * * * 
* *     * * 
*       * 
'''