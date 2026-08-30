#25341a05l1 vinay
list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    n1=input('enter the element')
    list1.append(n1)
for index,element in enumerate(list1):
    print('index=',index," ",'Element=',element)

'''output
enter the number of elements5
enter the elementnothing
enter the element200
enter the element1.212121
enter the element543
enter the elementmaybe
index= 0   Element= nothing
index= 1   Element= 200
index= 2   Element= 1.212121
index= 3   Element= 543
index= 4   Element= maybe
'''