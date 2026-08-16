#25341a05l1 vinay
n=4
a=n
for i in range(1,n+1):
     print(" "*(n-i),end=" ")
     if i==1:
          print("*")
     else:
        print("*"," "*(2*i-4),"*")   
for i in range(n-1,0,-1):
    print(" "*(n-i),end=" ")
    if i==1:
         print("*")
    else:
         print("*"," "*(2*i-4),"*") 

''' output
    *
   *  *
  *    *
 *      *
  *    *
   *  *
    *
'''