#25341a05l1 vinay
import argparse

# creating parser
parser = argparse.ArgumentParser()

# taking two numbers
parser.add_argument("--num1", type=int, required=True)
parser.add_argument("--num2", type=int, required=True)

# reading values
args = parser.parse_args()

# adding numbers
sum = args.num1 + args.num2

# printing result
print("Sum =", sum)

''' output 
PS D:\python\command line arguments> python cmdcha.py --num1 15 --num2 25
Sum = 40
'''