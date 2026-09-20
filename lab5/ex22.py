#25341a05l1 vinay
a=input('enter the string:')
b=''
for ch in a:
    if a.count(ch)>1 and ch not in b:
        print(ch,":",a.count(ch))
        b+=ch

''' 
output
enter the string:nothing
n : 2
'''