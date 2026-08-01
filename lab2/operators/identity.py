#25341a05l1 vinay

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2) # same content
print(list1 is list2) # same object?
print(list1 is list3) # same object?
print(id(list1), id(list2), id(list3))

''' output
True
False
True
1835608684736 1835608567744 1835608684736
'''