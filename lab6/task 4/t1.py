#25341a05l1 vinay
import re
pattern = r"[A-Za-z_][A-Za-z0-9_]*"
names = ["_count2", "2fast", "total_sum"]
for name in names:
    if re.fullmatch(pattern, name):
        print(name, "is valid")
    else:
        print(name, "is invalid")
'''output:
_count2 is valid
2fast is invalid
total_sum is valid
'''