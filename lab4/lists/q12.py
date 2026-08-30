#25341a05l1 vinay
numbers=[1,3,2,1,3,2,4,6,3,2,4,5]
numbers1=[]
for num in numbers:
    if num not in numbers1:
        numbers1.append(num)

print('original list is :',numbers)
print('list after removing duplicates :',numbers1)

'''output 
original list is : [1, 3, 2, 1, 3, 2, 4, 6, 3, 2, 4, 5]
list after removing duplicates : [1, 3, 2, 4, 6, 5]
'''