#25341a05l1 vinay
import re
sentence = "I have a cat, a dog, and a bird. My dog likes the cat."
pattern = r"\b(cat|dog|bird)\b"
pets = re.findall(pattern, sentence)
print(pets)

'''output "
['cat', 'dog', 'bird', 'dog', 'cat']
'''