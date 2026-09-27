#25341a05l1 vinay

from functools import reduce

numbers = [2, 4, 6, 8, 10]
words = ["Python", "is", "easy", "to", "learn"]

product = reduce(lambda a, b: a * b, numbers)
maximum = reduce(lambda a, b: a if a > b else b, numbers)
sentence = reduce(lambda a, b: a + " " + b, words)

print("Product =", product)
print("Maximum =", maximum)
print("Sentence =", sentence)

'''output :
Product = 3840
Maximum = 10
Sentence = Python is easy to learn
'''