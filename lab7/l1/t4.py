#25341a05l1 vinay

def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


numbers = [10, 20, 30, 40, 50]

minimum, maximum, average = stats(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)

'''output :
Minimum = 10
Maximum = 50
Average = 30.0
'''