#25341a05l1 vinay

numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, numbers.split()))
print("Sum =", sum(numbers))
'''
output 
Enter numbers separated by spaces: 34 56  23 45 
Sum = 158
'''