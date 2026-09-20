#25341a05l1 vinay
import re

text = "555-123-4567, (555) 123-4567, 555.123.4567"

pattern = r"\(?(\d{3})\)?[-.\s](\d{3})[-.](\d{4})"

result = re.sub(pattern, r"\1-\2-\3", text)

print(result)

'''output:
555-123-4567, 555-123-4567, 555-123-4567
'''