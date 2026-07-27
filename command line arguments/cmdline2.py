#25341a05l1 vinay

import sys

#check
if len(sys.argv) != 3:
    print("Usage: python cmdline1.py <number1> <number2>")
else:
    # Convert 
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # sum
    print("Sum =", num1 + num2)

    ''' output
     py cmdline2.py 15 25
Sum = 40
'''