#25341a05l1 vinay

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


n = int(input("Enter a number: "))

print("Recursive Factorial =", factorial(n))
print("Iterative Factorial =", factorial_iterative(n))

'''output :
Enter a number: 5
Recursive Factorial = 120
Iterative Factorial = 120
'''