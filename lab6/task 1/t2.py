#25341a05l1 vinay
import re
sentence = "1024 requests were served in 3 seconds"
result = re.search(r"served", sentence)
if result:
    print(result.span())


'''output:
(19, 25)
'''