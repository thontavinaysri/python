#25341a05l1 vinay

square = lambda x: x * x
even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b

print("Square =", square(5))
print("Even =", even(8))
print("Larger =", larger(10, 7))

'''output :
Square = 25
Even = True
Larger = 10
'''