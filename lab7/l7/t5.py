#25341a05l1 vinay

from functools import wraps

is_logged_in = False

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login first.")
    return wrapper

@require_login
def view_profile():
    print("Profile opened successfully")

print("When user is logged out:")
view_profile()

is_logged_in = True

print("\nWhen user is logged in:")
view_profile()

'''output :
When user is logged out:
Access denied. Please login first.

When user is logged in:
Profile opened successfully
'''