#25341a05l1 vinay

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def to_uppercase(s):
    return s.upper()

temperatures = [0, 10, 20, 30, 40]
words = ["python", "java", "c programming", "django"]

fahrenheit = list(map(celsius_to_fahrenheit, temperatures))
uppercase = list(map(to_uppercase, words))

print("Fahrenheit temperatures =", fahrenheit)
print("Uppercase strings =", uppercase)

'''output :
Fahrenheit temperatures = [32.0, 50.0, 68.0, 86.0, 104.0]
Uppercase strings = ['PYTHON', 'JAVA', 'C PROGRAMMING', 'DJANGO']
'''