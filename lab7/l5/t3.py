#25341a05l1 vinay

counter = 0

def wrong_function():
    counter += 1
    print(counter)

try:
    wrong_function()
except UnboundLocalError as e:
    print("Error:", e)


def correct_function():
    global counter
    counter += 1
    print("Counter =", counter)

correct_function()

'''output :
Error: cannot access local variable 'counter' where it is not associated with a value
Counter = 1
'''