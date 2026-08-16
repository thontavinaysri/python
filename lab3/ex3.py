#25341a05l1 vinay
a=int(input('enter the first side of triangle:'))
b=int(input('enter the second side of triangle:'))
c=int(input('enter the third side of triangle:'))
if a==b==c:
    print('equilateral triangle')
elif a==b or b==c or c==a:
    print('isosceles triangle')
elif a!=b and b!=c and c!=a:
    print('scalene triangle')
else:
    print('not a triangle')

    '''
    output
    enter the first side of triangle:3
enter the second side of triangle:2
enter the third side of triangle:5
scalene triangle
'''