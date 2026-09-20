#25341a05l1 vinay
import re
pattern = r"^#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?$"
colors = ["#FFAA00", "#000", "#12G", "#12345"]
for color in colors:
    if re.fullmatch(pattern, color):
        print(color, "is valid")
    else:
        print(color, "is invalid")

'''output :
#FFAA00 is valid
#000 is valid
#12G is invalid
#12345 is invalid
# '''