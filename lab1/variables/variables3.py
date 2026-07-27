#25341a05l1 vinay
#with using temp variable
x = 45
y = 90

print("Before swapping:")
print("x =", x)
print("y =", y)

temp = x
x = y
y = temp

print("\nAfter swapping using a temporary variable:")
print("x =", x)
print("y =", y)

# without using temp variable
m = 125
n = 275

print("\nBefore swapping:")
print("m =", m)
print("n =", n)

m, n = n, m

print("\nAfter swapping using tuple unpacking:")
print("m =", m)
print("n =", n)

'''output
After swapping using a temporary variable:
x = 90
y = 45

Before swapping:
m = 125
n = 275

After swapping using tuple unpacking:
m = 275
n = 125'''