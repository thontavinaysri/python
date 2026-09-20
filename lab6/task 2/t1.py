#25341a05l1 vinay
import re
text = "NASA and USA are working with ISRO on a new project."
capital_words = re.findall(r"\b[A-Z]+\b", text)
print(capital_words)

'''output:
['NASA', 'USA', 'ISRO']
'''