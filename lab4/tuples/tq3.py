#25341a05l1 vinay

# List to Tuple
my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)

print("Original List:", my_list)
print("Converted Tuple:", my_tuple)

# Tuple to List
another_tuple = (60, 70, 80, 90, 100)
another_list = list(another_tuple)

print("Original Tuple:", another_tuple)
print("Converted List:", another_list)

'''output 
Original List: [10, 20, 30, 40, 50]
Converted Tuple: (10, 20, 30, 40, 50)
Original Tuple: (60, 70, 80, 90, 100)
Converted List: [60, 70, 80, 90, 100]
'''