#25341a05l1 vinay
n = int(input("Enter the number of terms: "))
a = 0
b = 1
i = 1
while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1

    '''output 
    Enter the number of terms: 4
0 1 1 2 
'''