#25341a05l1 vinay
a=int(input('enter the first number:'))
b=int(input('enter the last number:'))
for i in range(a,b+1):
    if i>1:
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i,' ',end='')    

'''output
enter the first number:2
enter the last number:21
2  3  5  7  11  13  17  19 
'''