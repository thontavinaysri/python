#25341a05l1 vinay
import re

log_text = """2024-06-01 08:15:32 ERROR user=john msg=Disk full
2024-06-01 08:16:10 WARN user=alice msg=Low memory
2024-06-01 08:17:45 INFO user=bob msg=Backup started
2024-06-01 08:18:20 ERROR user=alice msg=Connection failed
2024-06-01 08:19:05 INFO user=john msg=Login successful
2024-06-01 08:20:11 WARN user=bob msg=CPU usage high
2024-06-01 08:21:30 ERROR user=bob msg=Database unavailable
2024-06-01 08:22:14 INFO user=alice msg=Report generated"""

redacted_log = re.sub(r"user=\w+", "user=<hidden>", log_text)

print(redacted_log)

'''output:
2024-06-01 08:15:32 ERROR user=<hidden> msg=Disk full
2024-06-01 08:16:10 WARN user=<hidden> msg=Low memory
2024-06-01 08:17:45 INFO user=<hidden> msg=Backup started
2024-06-01 08:18:20 ERROR user=<hidden> msg=Connection failed
2024-06-01 08:19:05 INFO user=<hidden> msg=Login successful
2024-06-01 08:20:11 WARN user=<hidden> msg=CPU usage high
2024-06-01 08:21:30 ERROR user=<hidden> msg=Database unavailable
2024-06-01 08:22:14 INFO user=<hidden> msg=Report generated
'''