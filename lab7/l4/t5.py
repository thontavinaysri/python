#25341a05l1 vinay

items = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Headphones": 2000
}

sorted_items = sorted(items.items(), key=lambda x: x[1])

for item, price in sorted_items:
    print(item, ":", price)

'''output :
Mouse : 500
Keyboard : 1500
Headphones : 2000
Laptop : 50000
'''