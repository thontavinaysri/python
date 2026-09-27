#25341a05l1 vinay

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello! Welcome to Python")

greet()

'''output :
Hello! Welcome to Python
Hello! Welcome to Python
Hello! Welcome to Python
'''