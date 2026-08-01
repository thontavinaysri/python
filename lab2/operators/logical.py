#25341a05l1 vinay
percentage=int(input('Enter your percentage:'))
attendance=int(input('Enter your attendance:'))
if percentage>75 and attendance>=90:
    print('You are eligible for the schoalarship')  
else:
    print('You are not eligible for the schoalarship')

    '''
    output 
Enter your percentage:90
Enter your attendance:90
You are eligible for the schoalarship

Enter your percentage:50
Enter your attendance:89
You are not eligible for the schoalarship

'''