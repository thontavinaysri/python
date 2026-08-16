#25341a05l1 vinay
n=int(input("enter the number:"))
sum=0
num=n
while n>0:
    sum+=n
    n-=1
avg=sum/num
print('sum is',sum)
print('average is',avg)

''' output 
enter the number:7
sum is 28
average is 4.0
'''