#25341a05l1 vinay

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(word):
    return word == word[::-1]

numbers = list(range(1, 51))
words = ["madam", "hello", "level", "python", "radar", "world", "civic"]

prime_numbers = list(filter(is_prime, numbers))
palindromes = list(filter(is_palindrome, words))

print("Prime numbers =", prime_numbers)
print("Palindromes =", palindromes)

'''output :
Prime numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Palindromes = ['madam', 'level', 'radar', 'civic']
'''