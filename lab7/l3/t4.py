#25341a05l1 vinay

def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result =", power(base, exp))

'''output :
Enter base: 2
Enter exponent: -3
Result = 0.125
'''