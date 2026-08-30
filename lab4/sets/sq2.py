#25341a05l1 vinay
numbers = [10, 20, 30, 20, 40, 10]
text = "banana"

set_from_list = set(numbers)
set_from_string = set(text)

print("Original list:", numbers)
print("Set from list:", set_from_list)

print("Original string:", text)
print("Set from string:", set_from_string)

'''output
Original list: [10, 20, 30, 20, 40, 10]
Set from list: {40, 10, 20, 30}
Original string: banana
Set from string: {'b', 'a', 'n'}
'''