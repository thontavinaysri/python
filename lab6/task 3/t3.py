#25341a05l1 vinay
import re
def double_number(match):
    return str(int(match.group()) * 2)
text = "I have 3 apples and 5 oranges."
result = re.sub(r"\d+", double_number, text)
print(result)
'''output:
I have 6 apples and 10 oranges.
'''