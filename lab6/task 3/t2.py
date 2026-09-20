#25341a05l1 vinay
import re
names = "Doe, John"
result = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", names)
print(result)
'''output:
John Doe
'''