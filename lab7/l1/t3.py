#25341a05l1 vinay

def is_even(n):
    return n % 2 == 0

for _ in range(5):
    num = int(input("Enter a number: "))
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")