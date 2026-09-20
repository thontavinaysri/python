#25341a05l1 vinay
import re
text = "Wait!!! What??? Really!!!"
result, count = re.subn(r"([!?])\1+", r"\1", text)
print(result)
print("Replacements made:", count)

'''output :
Wait! What? Really!
Replacements made: 3'''