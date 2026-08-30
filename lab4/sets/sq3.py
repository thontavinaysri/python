#25341a05l1 vinay
numbers = {10, 20, 30}

print("Original set:", numbers)

numbers.add(40)
print("After add(40):", numbers)

numbers.update([50, 60, 70])
print("After update([50, 60, 70]):", numbers)

''' output
Original set: {10, 20, 30}
After add(40): {40, 10, 20, 30}
After update([50, 60, 70]): {70, 40, 10, 50, 20, 60, 30}
'''