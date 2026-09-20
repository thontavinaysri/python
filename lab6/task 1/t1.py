#25341a05l1 vinay
import re
sentence = "1024 requests were served in 3 seconds"
result = re.match(r"\d", sentence)
if result:
    print("Sentence starts with a digit")
else:
    print("Sentence does not start with a digit")

"""
 output :
Sentence starts with a digit
"""