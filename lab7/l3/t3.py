#25341a05l1 vinay

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)


n = int(input("Enter a positive integer: "))

print("Sum of digits =", sum_of_digits(n))
print("Reversed number =", reverse_number(n))

'''output :
Enter a positive integer: 12345
Sum of digits = 15
Reversed number = 54321
'''