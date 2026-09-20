#25341a05l1 vinay
import re

def is_valid_email(s):
    pattern = r"[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}"
    return re.fullmatch(pattern, s) is not None


valid_emails = [
    "john@gmail.com",
    "user.name@yahoo.com",
    "test123@college.edu",
    "a@b.co"
]

invalid_emails = [
    "a@b.c",
    "no-at-sign.com",
    "user@gmail",
    "@gmail.com"
]

for email in valid_emails:
    print(email, is_valid_email(email))

print()

for email in invalid_emails:
    print(email, is_valid_email(email))

'''output:

john@gmail.com True
user.name@yahoo.com True
test123@college.edu True
a@b.co True

a@b.c False
no-at-sign.com False
user@gmail False
@gmail.com False'''