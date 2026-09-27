#25341a05l1 vinay

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(15):
    print(fibonacci(i), end=" ")

count = 0

def fibonacci_count(n):
    global count
    if n <= 1:
        return n
    if n == 5:
        count += 1
    return fibonacci_count(n - 1) + fibonacci_count(n - 2)

fibonacci_count(10)

print("\n fibonacci(5) is recomputed", count, "times")

'''output :
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
fibonacci(5) is recomputed 5 times
'''