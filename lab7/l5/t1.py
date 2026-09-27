#25341a05l1 vinay

counter = 0

def show_local():
    counter = 10
    print("Local counter =", counter)

show_local()
print("Global counter =", counter)

'''output :
Local counter = 10
Global counter = 0
'''