#25341a05l1 vinay

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()

print("Count =", counter())
print("Count =", counter())
print("Count =", counter())
print("Count =", counter())
print("Count =", counter())

'''output :
Count = 1
Count = 2
Count = 3
Count = 4
Count = 5
'''