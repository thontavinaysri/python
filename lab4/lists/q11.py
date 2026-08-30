#25341a05l1 vinay
numbers=[1,2,3,5,7,11,13,17,19,23,29,31,37]
print('original list is:',numbers)
#append
numbers.append(10)
print('after append :',numbers)
#insert
numbers.insert(3,110)
print('after insert :',numbers)
#extend
numbers.extend([33,12])
print('after extend :',numbers)
#remove
numbers.remove(17)
print('after removing :',numbers)
#pop
numbers.pop()
print('after pop :',numbers)
#sort
numbers.sort()
print('after sort :',numbers)
#reverse
numbers.reverse()
print('after reverse :',numbers)
#count
numbers.append(30)
print("After append(30):", numbers)
print("Count of 30:", numbers.count(30))
print("List after count():", numbers)
#index
print("Index of 30:", numbers.index(30))
print("List after index():", numbers)

'''output
original list is: [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
after append : [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 10]
after insert : [1, 2, 3, 110, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 10]
after extend : [1, 2, 3, 110, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 10, 33, 12]
after removing : [1, 2, 3, 110, 5, 7, 11, 13, 19, 23, 29, 31, 37, 10, 33, 12]
after pop : [1, 2, 3, 110, 5, 7, 11, 13, 19, 23, 29, 31, 37, 10, 33]
after sort : [1, 2, 3, 5, 7, 10, 11, 13, 19, 23, 29, 31, 33, 37, 110]
after reverse : [110, 37, 33, 31, 29, 23, 19, 13, 11, 10, 7, 5, 3, 2, 1]
After append(30): [110, 37, 33, 31, 29, 23, 19, 13, 11, 10, 7, 5, 3, 2, 1, 30]
Count of 30: 1
List after count(): [110, 37, 33, 31, 29, 23, 19, 13, 11, 10, 7, 5, 3, 2, 1, 30]
Index of 30: 15
List after index(): [110, 37, 33, 31, 29, 23, 19, 13, 11, 10, 7, 5, 3, 2, 1, 30]
'''