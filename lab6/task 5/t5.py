#25341a05l1 vinay
import re

def check_password(pw):
    failed = []

    if len(pw) < 8:
        failed.append("At least 8 characters")

    if not re.search(r"[A-Z]", pw):
        failed.append("At least one uppercase letter")

    if not re.search(r"[a-z]", pw):
        failed.append("At least one lowercase letter")

    if not re.search(r"\d", pw):
        failed.append("At least one digit")

    if not re.search(r"[!@#$%^&*]", pw):
        failed.append("At least one symbol (!@#$%^&*)")

    return failed


print(check_password("hello"))
print(check_password("Hello123"))
print(check_password("Hello@123"))
'''output:
['At least 8 characters', 'At least one uppercase letter', 'At least one digit', 'At least one symbol (!@#$%^&*)']
['At least one symbol (!@#$%^&*)']
[]'''