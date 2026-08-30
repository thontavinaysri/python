#25341a05l1 vinay


numbers = [10, -5, 20, -8, 15, -3, 0]

result = [0 if num < 0 else num for num in numbers]

print("Original list:", numbers)
print("Updated list:", result)

'''output
Original list: [10, -5, 20, -8, 15, -3, 0]
Updated list: [10, 0, 20, 0, 15, 0, 0]

'''