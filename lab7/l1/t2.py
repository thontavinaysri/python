#25341a05l1 vinay
def simple_interest(principal, rate, time):
    """
    Calculates and returns the simple interest.
    """
    si = (principal * rate * time) / 100
    return si



principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

result = simple_interest(principal, rate, time)

print("Simple Interest =", result)


'''output :
Enter principal amount: 10000
Enter rate of interest: 5
Enter time in years: 2
Simple Interest = 1000.0
'''