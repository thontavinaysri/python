#25341a05l1 vinay
numbers=[12,54,21,54,67,54,32,7]
max=numbers[0]
min=numbers[0]
sum=0
for num in numbers:
    if num > max:
        max=num
    if num < min:
        min=num
    sum+=num
print('maximum number is :',max)
print('minimum number is :',min)
print('sum of numbers is :',sum)

''' output
maximum number is : 67
minimum number is : 7
sum of numbers is : 301
'''