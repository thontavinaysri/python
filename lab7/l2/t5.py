#25341a05l1 vinay

def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Items:")
    for item in items:
        print(item)
    print("Discount:", discount, "%")
    for key, value in extra.items():
        print(key.capitalize(), ":", value)

order_summary("Meera", "Laptop", "Mouse", discount=10,
              delivery_address="Hyderabad", gift_wrap=True)

'''output :
Customer: Meera
Items:
Laptop
Mouse
Discount: 10 %
Delivery_address : Hyderabad
Gift_wrap : True
'''