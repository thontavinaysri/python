#25341a05l1 vinay

def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    discount_amount = price * discount / 100
    return price + tax - discount_amount

print("Final Price:", calculate_price(1000))
print("Final Price:", calculate_price(1000, 10))
print("Final Price:", calculate_price(1000, 10, 5))

'''output :
Final Price: 1180.0
Final Price: 1100.0
Final Price: 1050.0
'''