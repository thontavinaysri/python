#25341a05l1 vinay
products = {
    "P101": "Laptop",
    "P102": "Mouse"
}

print("Original dictionary:", products)

products["P103"] = "Keyboard"
products["P104"] = "Monitor"
products["P105"] = "Printer"

print("Dictionary after adding 3 new pairs:", products)

''' output
Original dictionary: {'P101': 'Laptop', 'P102': 'Mouse'}
Dictionary after adding 3 new pairs: {'P101': 'Laptop', 'P102': 'Mouse', 'P103': 'Keyboard', 'P104': 'Monitor', 'P105': 'Printer'}
'''