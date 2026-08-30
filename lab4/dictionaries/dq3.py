#25341a05l1 vinay
products = {
    "P101": "Laptop",
    "P102": "Mouse",
    "P103": "Keyboard"
}

print("Before update:", products)

products["P102"] = "Wireless Mouse"

print("After update:", products)

'''output 
Before update: {'P101': 'Laptop', 'P102': 'Mouse', 'P103': 'Keyboard'}
After update: {'P101': 'Laptop', 'P102': 'Wireless Mouse', 'P103': 'Keyboard'}
'''