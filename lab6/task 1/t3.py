#25341a05l1 vinay
import re
str1 = "12345"
str2 = "123a5"
result1 = re.fullmatch(r"\d+", str1)
result2 = re.fullmatch(r"\d+", str2)
if result1:
    print("12345 contains only digits")
else:
    print("12345 does not contain only digits")

if result2:
    print("123a5 contains only digits")
else:
    print("123a5 does not contain only digits")



'''output:
12345 contains only digits
123a5 does not contain only digits
'''