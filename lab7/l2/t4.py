#25341a05l1 vinay

def build_profile(**details):
    for key, value in details.items():
        print(key.capitalize(), ":", value)

build_profile(name="Vinay", age=19, city="Nellore", hobby="Coding")

build_profile(name="Rahul", age=20, city="Hyderabad")

'''output :
Name : Vinay
Age : 19
City : Nellore
Hobby : Coding
Name : Rahul
Age : 20
City : Hyderabad
'''