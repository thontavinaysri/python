#25341a05l1 vinay
import re
text = "NASA and USA are working with ISRO on a new project."
for match in re.finditer(r"\b\w{7,}\b", text):
    print(match.group(), match.start())
'''output:
working 17
project 44
'''