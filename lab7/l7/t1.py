#25341a05l1 vinay

def greet(name):
    return "Hello " + name

new_function = greet
print("Calling through new variable:", new_function("Vinay"))

def execute(func, value):
    return func(value)

print("Passing function as argument:", execute(greet, "Rahul"))

def create_function():
    def message():
        return "Function returned successfully"
    return message

returned_function = create_function()
print(returned_function())

'''output :
Calling through new variable: Hello Vinay
Passing function as argument: Hello Rahul
Function returned successfully
'''