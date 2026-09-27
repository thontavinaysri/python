#25341a05l1 vinay

import time

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time =", end - start, "seconds")
        return result
    return wrapper

@log_call
@timer
def add(a, b):
    return a + b

result = add(10, 20)

'''output :
Calling add args=(10, 20) kwargs={}
Execution time = 0.000001 seconds
add returned 30
'''