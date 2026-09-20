#25341a05l1 vinay

import re
log = "2024-06-01 08:15:32 ERROR Disk full"
pattern = r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>\w+)\s+(?P<message>.*)"
match = re.match(pattern, log)
print("Date:", match.group("date"))
print("Time:", match.group("time"))
print("Level:", match.group("level"))
print("Message:", match.group("message"))
'''output:
Date: 2024-06-01                                                                                     
Time: 08:15:32                                                  
Level: ERROR
Message: Disk full'''